"""Patches index.html to display project thumbnail images in project cards."""
import re

HTML = r"C:\Users\Doaa Eladly\eslam-portfolio\index.html"

with open(HTML, 'r', encoding='utf-8') as f:
    html = f.read()

# ── 1. Insert the PROJ_THUMBS map before renderProjects() ──────────────────
thumbs_map = (
    "const PROJ_THUMBS={"
    "'shoglana':'images/sho8lana.png',"
    "'cipher-case':'images/cipher-case.png',"
    "'deep-data-dive':'images/deep-data-dive.png',"
    "'pawkicks':'images/pawkicks.png',"
    "'aero-pulse':'images/aero-pulse.png',"
    "'space-mission':'images/ai-space.png',"
    "'hybrid-athlete':'images/hybrid-athlete.png',"
    "'masr-ledger':'images/masr-ledger.png',"
    "'campus-care':'images/campus-care.png',"
    "'enterprise-bi':'images/enterprise-bi.png'"
    "};\n"
)

MARKER = 'function renderProjects() {'
assert MARKER in html, 'renderProjects not found'
if 'PROJ_THUMBS' not in html:
    html = html.replace(MARKER, thumbs_map + MARKER, 1)
    print('  Inserted PROJ_THUMBS map')
else:
    print('  PROJ_THUMBS already present — skipping insert')

# ── 2. Replace grid card proj-visual (one-liner in the source) ─────────────
OLD_VISUAL = (
    '<div class="proj-visual" style="background:${p.color}">'
    '<div class="proj-monogram">${p.name.charAt(0)}</div>'
    '<div class="proj-code-overlay">'
    '<div class="proj-code-line" style="width:78%"></div>'
    '<div class="proj-code-line" style="width:52%"></div>'
    '<div class="proj-code-line" style="width:66%"></div>'
    '<div class="proj-code-line" style="width:40%"></div>'
    '</div></div>'
)

NEW_VISUAL = (
    '${PROJ_THUMBS[p.id]'
    '?`<div class="proj-visual" style="background:${p.color}">'
    '<img src="${PROJ_THUMBS[p.id]}" alt="${p.name}" loading="lazy" '
    'style="width:100%;height:100%;object-fit:cover;display:block;">'
    '</div>`'
    ':`<div class="proj-visual" style="background:${p.color}">'
    '<div class="proj-monogram">${p.name.charAt(0)}</div>'
    '</div>`}'
)

if OLD_VISUAL in html:
    html = html.replace(OLD_VISUAL, NEW_VISUAL, 1)
    print('  Replaced grid proj-visual')
elif NEW_VISUAL in html:
    print('  Grid proj-visual already patched — skipping')
else:
    print('  WARNING: grid proj-visual not found — check source')

# ── 3. Replace featured card feat-visual (multi-line in the source) ─────────
OLD_FEAT = (
    '        <div class="feat-visual" style="background:${feat.color}">\n'
    '          <div class="feat-monogram">${feat.name.charAt(0)}</div>\n'
    '          <div class="feat-mockup">\n'
    '            <div class="feat-mock-bar" style="width:80%"></div>\n'
    '            <div class="feat-mock-bar" style="width:60%"></div>\n'
    '            <div class="feat-mock-bar" style="width:70%"></div>\n'
    '          </div>\n'
    '        </div>'
)

NEW_FEAT = (
    '        ${PROJ_THUMBS[feat.id]\n'
    '          ?`<div class="feat-visual" style="background:${feat.color};position:relative;">'
    '<img src="${PROJ_THUMBS[feat.id]}" alt="${feat.name}" '
    'style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block;">'
    '</div>`\n'
    '          :`<div class="feat-visual" style="background:${feat.color}">'
    '<div class="feat-monogram">${feat.name.charAt(0)}</div>'
    '</div>`}'
)

if OLD_FEAT in html:
    html = html.replace(OLD_FEAT, NEW_FEAT, 1)
    print('  Replaced featured feat-visual')
elif 'PROJ_THUMBS[feat.id]' in html:
    print('  Featured feat-visual already patched — skipping')
else:
    print('  WARNING: featured feat-visual not matched — trying relaxed search')
    # Try with \r\n
    OLD_FEAT_CRLF = OLD_FEAT.replace('\n', '\r\n')
    if OLD_FEAT_CRLF in html:
        html = html.replace(OLD_FEAT_CRLF, NEW_FEAT.replace('\n', '\r\n'), 1)
        print('    Fixed with CRLF line endings')
    else:
        print('    Still not found — manual fix needed')

# ── 4. Write back ────────────────────────────────────────────────────────────
with open(HTML, 'w', encoding='utf-8') as f:
    f.write(html)

print('\nPatch complete! index.html updated.')
