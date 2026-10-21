"""Quick static-site checks; no third-party dependencies."""
from datetime import datetime, timezone, timedelta
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re

ROOT = Path(__file__).resolve().parents[1]
errors = []

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
    def handle_starttag(self, tag, attrs):
        self.links.extend(value for key, value in attrs if value and key in ('href', 'src'))

def check_link(source, link):
    url = urlsplit(link)
    if url.scheme or url.netloc or not url.path:
        return
    target = (ROOT / unquote(url.path).lstrip('/')) if url.path.startswith('/') else source.parent / unquote(url.path)
    if not target.exists():
        errors.append(f'{source.relative_to(ROOT)}: missing {link}')

for source in [ROOT / 'index.html', ROOT / 'security/index.html']:
    parser = Links()
    parser.feed(source.read_text(encoding='utf-8'))
    for link in parser.links:
        check_link(source, link)
for source in (ROOT / 'assets/css').glob('*.css'):
    for link in re.findall(r'url\([\"\']?([^\)\"\']+)', source.read_text(encoding='utf-8')):
        check_link(source, link)

primary = ROOT / '.well-known/security.txt'
text = primary.read_text(encoding='utf-8')
if primary.read_bytes() != (ROOT / 'security.txt').read_bytes():
    errors.append('The two security.txt files differ.')
fields = {}
for line in text.splitlines():
    if line and not line.startswith('#'):
        key, value = line.split(':', 1)
        fields.setdefault(key, []).append(value.strip())
if fields.get('Contact') != ['mailto:security@cortisci.com']:
    errors.append('Unexpected reporting address.')
if fields.get('Policy') != ['https://www.cortisci.com/security/']:
    errors.append('Unexpected policy URL.')
try:
    expires = datetime.fromisoformat(fields['Expires'][0].replace('Z', '+00:00'))
    if len(fields['Expires']) != 1 or not datetime.now(timezone.utc) < expires <= datetime.now(timezone.utc) + timedelta(days=366):
        errors.append('Review security.txt expiry: it must be future-dated and within one year.')
except (KeyError, ValueError, TypeError):
    errors.append('Invalid or missing Expires field.')
if not (ROOT / '.nojekyll').exists():
    errors.append('Missing .nojekyll for static publication.')
if (ROOT / 'CNAME').read_text().strip() != 'www.cortisci.com':
    errors.append('Unexpected custom domain.')
if errors:
    raise SystemExit('\n'.join(errors))
print('PASS: local page/CSS assets, security.txt copies, contact, policy, expiry, custom domain and static publication marker.')
