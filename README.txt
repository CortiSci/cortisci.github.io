CortiSci website
===============

Repository: https://github.com/CortiSci/cortisci.github.io
Live site: https://www.cortisci.com/
Local checkout: C:\Users\Jeremy\www.cortisci.com

Hosting
-------
Already hosted by GitHub Pages from main, repository root. HTTPS is enforced.
CNAME retains www.cortisci.com. No hosting migration, framework, package install,
or application server is needed. .nojekyll makes this a plain static deployment,
including .well-known/security.txt.

Local changes are not published until pushed to origin/main.

Preview: python -m http.server 8080 --bind 127.0.0.1
Then open http://127.0.0.1:8080/ or http://127.0.0.1:8080/security/.
Quick verification: python tools/check_site.py

Security publication
--------------------
The homepage #security panel and security/index.html contain the same policy.
Keep their policy text in sync when editing; the quick check verifies this.
.well-known/security.txt is the standard discovery file; security.txt is an
identical root-level copy. Update both together. These public documents cover
CortiPix software and device firmware; internal risk records, vulnerability
reports, the report tracker, and engineering documents do not belong here.

Before publishing the security additions:
- Set up security@cortisci.com and test external receipt and read/reply access.
- Confirm Geoff's backup access and handoff; establish report tracking and
  monitoring for the agreed acknowledgment/update commitments.
- Align PLN005 with the approved policy decisions: older drafting notes cite
  three-day acknowledgment and fixed disclosure timing; this policy uses the
  subsequently agreed five business days and case-by-case disclosure.
- Check the expiry is still appropriate. The prepared security.txt expires
  2027-10-20 at 23:59:59 UTC. Jeremy owns review/renewal before that date;
  review by 2027-09-20 is suggested. No reminder has been scheduled.

The existing HTTPS hostname is www.cortisci.com, so published policy links use
https://www.cortisci.com/security/. Verify apex-domain forwarding separately if
https://cortisci.com/security is also circulated.

After publication, verify /security, /security/, /.well-known/security.txt and
/security.txt over HTTPS, including text/plain for the TXT files. GitHub serves
security/index.html at the directory route; /security redirects to /security/.
Review annually and whenever contact details or procedures change. Do not renew
Expires automatically without checking the contact and policy.

Sources
-------
Existing homepage and linked assets compared with https://www.cortisci.com/ on
2026-10-21; source matches apart from checkout line endings. Original appearance,
content, assets and attribution are retained. Security content follows Jeremy's
approved decision register in sw-requirements-testing/docs/cybersecurity/.
Format reference: https://www.rfc-editor.org/rfc/rfc9116.html
Hosting: https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages

Original template credits
-------------------------
Dimension by HTML5 UP
html5up.net | @ajlkn
Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)


This is Dimension, a fun little one-pager with modal-ized (is that a word?) "pages"
and a cool depth effect (click on a menu item to see what I mean). Simple, fully
responsive, and kitted out with all the usual pre-styled elements you'd expect.
Hope you dig it :)

Demo images* courtesy of Unsplash, a radtastic collection of CC0 (public domain) images
you can use for pretty much whatever.

(* = not included)

AJ
aj@lkn.io | @ajlkn


Credits:

	Demo Images:
		Unsplash (unsplash.com)

	Icons:
		Font Awesome (fontawesome.io)

	Other:
		jQuery (jquery.com)
		Responsive Tools (github.com/ajlkn/responsive-tools)