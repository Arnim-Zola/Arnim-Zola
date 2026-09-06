import os
import re
import xml.etree.ElementTree as ET

def generate_unified_secondary_table():
    assets_dir = r"c:\Holidays\Arnim-Zola\assets"

    # Read base64 font from taglines.svg
    taglines_path = os.path.join(assets_dir, "taglines.svg")
    with open(taglines_path, "r", encoding="utf-8") as f:
        taglines_content = f.read()

    font_match = re.search(r"@font-face\s*\{[^}]*\}", taglines_content, re.DOTALL)
    font_face_css = font_match.group(0) if font_match else ""

    vbox_w = 920
    header_h = 46
    row_h = 128
    total_h = header_h + row_h * 4  # 46 + 512 = 558

    col1_w = 140
    col2_w = 435
    col3_w = 205
    col4_w = vbox_w - (col1_w + col2_w + col3_w) # 140

    col2_x = col1_w                      # 140
    col3_x = col1_w + col2_w             # 575
    col4_x = col1_w + col2_w + col3_w     # 780
    
    # Exact justified width matching right column margin (575 - 14 - 154 = 407)
    text_x = col2_x + 14                 # 154
    text_len = 407

    shared_css = f"""
      {font_face_css}

      .th-text {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 16px;
        font-weight: 400;
        letter-spacing: 0.5px;
        fill: #ffffff;
      }}
      .project-name {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 18px;
        font-weight: 400;
        letter-spacing: 0.4px;
        fill: #00ff66;
        filter: drop-shadow(0 1px 2px rgba(0,0,0,0.8));
      }}
      .domain-text {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 13.5px;
        font-weight: 400;
        letter-spacing: 0.2px;
        fill: #7ee787;
      }}
      .desc-text {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 13.3px;
        font-weight: 400;
        letter-spacing: -0.05px;
        fill: #ffffff;
      }}
      .hi {{
        fill: #00ff66;
      }}
      .badge-bg {{
        fill: #06170d;
        stroke: #164d27;
        stroke-width: 1.2;
      }}
      .badge-text {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 12px;
        font-weight: 400;
        letter-spacing: 0.2px;
        fill: #7ee787;
        text-anchor: middle;
      }}
      .btn-bg {{
        fill: #05140a;
        stroke: #00ff66;
        stroke-width: 1.2;
      }}
      .btn-text {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 11px;
        font-weight: 400;
        letter-spacing: 0.15px;
        fill: #ffffff;
        text-anchor: middle;
      }}
      .btn-arrow {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 12px;
        font-weight: 700;
        fill: #00ff66;
      }}
      .active-text {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 11px;
        font-weight: 400;
        letter-spacing: 0.3px;
        fill: #00ff66;
      }}
      .grid-line {{
        stroke: #102618;
        stroke-width: 1;
      }}
    """

    projects_data = [
        {
            "id": "campuscart",
            "name": "CampusCart",
            "domain": "Campus Logistics",
            "desc": [
                ('Standing in a 20-person line at 8:55 AM just to print two pages before deadline?',),
                ('CampusCart kills the campus queue forever with an instantaneous zero-queue',),
                ('utility powered by client-side <tspan class="hi">PDF.js</tspan> parsing &amp; dynamic pricing calculus, 3s',),
                ('automated <tspan class="hi">Django REST</tspan> polling queues, and live <tspan class="hi">Next.js 14</tspan> vendor dashboards.',)
            ],
            "badges": [
                [("Next.js 14", 66), ("PostgreSQL", 76)],
                [("Django REST", 84), ("PDF.js", 54)]
            ],
            "repo": "CampusCart",
            "active": False
        },
        {
            "id": "zemo",
            "name": "Zemo",
            "domain": "E-Commerce Intel",
            "desc": [
                ('That "50% OFF Limited Deal" with 4.8 stars written by bots? We called its bluff.',),
                ('Zemo is an autonomous radar built to expose fake hype and predatory price hikes',),
                ('by automating headless <tspan class="hi">Playwright</tspan> scraping across dynamic e-commerce DOMs, and',),
                ('synthesizing 100+ customer reviews via <tspan class="hi">Meta Llama 3 8B</tspan> into <tspan class="hi">Plotly.js</tspan> charts.',)
            ],
            "badges": [
                [("Meta Llama 3", 84), ("FastAPI", 56)],
                [("Playwright", 74), ("Plotly.js", 62)]
            ],
            "repo": "Zemo",
            "active": False
        },
        {
            "id": "brainiac",
            "name": "Brainiac",
            "domain": "Cognitive AI",
            "desc": [
                ('Ever wondered what 3 AM caffeine-fueled burnout looks like inside your head?',),
                ('Brainiac renders your brain\'s cognitive chaos into a living 3D simulation,',),
                ('featuring an interactive <tspan class="hi">@react-three/fiber</tspan> cortical mesh, computing 30-factor',),
                ('psychometric scoring vectors via <tspan class="hi">PyTorch</tspan>, and personalized AI protocols.',)
            ],
            "badges": [
                [("React 18", 54), ("@react-three/fiber", 110)],
                [("Three.js", 52), ("PyTorch", 52), ("FastAPI", 52)]
            ],
            "repo": "Brainiac",
            "active": False
        },
        {
            "id": "quantum",
            "name": "Quantum OS",
            "domain": "Interactive Portfolio",
            "desc": [
                ('Why should developer portfolios look like another generic resume from 2015?',),
                ('Quantum OS turns my portfolio into a sci-fi cybernetic desktop operating system,',),
                ('powered by custom GPU <tspan class="hi">GLSL fragment shaders</tspan> at 60FPS, <tspan class="hi">Web Audio API</tspan> acoustic',),
                ('feedback sound synthesis, and a live real-time streaming edge AI terminal shell.',)
            ],
            "badges": [
                [("Next.js 15", 66), ("GLSL Shaders", 84)],
                [("Three.js", 58), ("Web Audio", 72)]
            ],
            "repo": "Portfolio",
            "active": True
        }
    ]

    # Generate row markup inside group transformed to row position
    all_rows_markup = []
    h_lines = []

    for idx, p in enumerate(projects_data):
        y_offset = header_h + idx * row_h
        
        # Horizontal divider line above row (except header line which is drawn separately)
        if idx > 0:
            h_lines.append(f'<line x1="0" y1="{y_offset}" x2="{vbox_w}" y2="{y_offset}" class="grid-line" />')

        # Col 1: Project Name & Domain
        col1_svg = f'''<text x="18" y="54" class="project-name">{p["name"]}</text>
    <text x="18" y="78" class="domain-text">{p["domain"]}</text>'''

        # Col 2: Desc (Cleanly justified flush to right margin)
        d_svg_list = []
        for d_idx, d_line in enumerate(p["desc"]):
            dy = 26 + d_idx * 24
            d_svg_list.append(f'<text x="{text_x}" y="{dy}" textLength="{text_len}" lengthAdjust="spacing" class="desc-text">{d_line[0]}</text>')
        col2_svg = "\n    ".join(d_svg_list)

        # Col 3: Badges
        badge_svg_list = []
        b_start_y = 32
        for b_row_idx, b_list in enumerate(p["badges"]):
            by = b_start_y + b_row_idx * 34
            bx = col3_x + 8
            for label, bw in b_list:
                badge_svg_list.append(f'''<g transform="translate({bx}, {by})">
      <rect width="{bw}" height="26" rx="6" class="badge-bg" />
      <text x="{bw/2}" y="17.5" class="badge-text">{label}</text>
    </g>''')
                bx += bw + 6
        col3_svg = "\n    ".join(badge_svg_list)

        # Col 4: Button
        btn_w = 124
        btn_h = 30
        btn_x = col4_x + 8
        btn_y = 34 if p["active"] else 48
        active_svg = ""
        if p["active"]:
            active_svg = f'''<g transform="translate({btn_x}, {btn_y + 36})">
      <rect width="{btn_w}" height="20" rx="4" fill="#041208" stroke="#1b4d2e" stroke-width="0.8" />
      <circle cx="12" cy="10" r="3" fill="#00ff66" />
      <text x="22" y="14" class="active-text">Active Build</text>
    </g>'''

        col4_svg = f'''<g transform="translate({btn_x}, {btn_y})">
      <rect width="{btn_w}" height="{btn_h}" rx="6" class="btn-bg" />
      <text x="{btn_w/2}" y="19.5" class="btn-text">Arnim-Zola/{p['repo']} <tspan class="btn-arrow">↗</tspan></text>
    </g>
    {active_svg}'''

        row_group = f"""  <!-- Row {idx + 1}: {p['name']} -->
  <g transform="translate(0, {y_offset})">
    {col1_svg}
    {col2_svg}
    {col3_svg}
    {col4_svg}
  </g>"""
        all_rows_markup.append(row_group)

    all_rows_str = "\n".join(all_rows_markup)
    all_h_lines_str = "\n  ".join(h_lines)

    unified_table_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vbox_w} {total_h}" width="100%" height="{total_h}" fill="none">
  <defs>
    <style>{shared_css}</style>
  </defs>

  <!-- Seamless Table Container Box (Unified, No Row Gaps) -->
  <rect x="0" y="0" width="{vbox_w}" height="{total_h}" rx="10" fill="#040906" stroke="#163d22" stroke-width="1.5" />

  <!-- Table Header Background with Rounded Top Corners -->
  <path d="M 0 10 Q 0 0 10 0 L {vbox_w - 10} 0 Q {vbox_w} 0 {vbox_w} 10 L {vbox_w} {header_h} L 0 {header_h} Z" fill="#07150c" />

  <!-- Header Titles -->
  <text x="18" y="29" class="th-text">Project &amp; Domain</text>
  <text x="{col2_x + 14}" y="29" class="th-text">Architecture &amp; Systems Highlights</text>
  <text x="{col3_x + 10}" y="29" class="th-text">Core Stack</text>
  <text x="{col4_x + 10}" y="29" class="th-text">Source Code</text>

  <!-- Horizontal Grid Lines -->
  <line x1="0" y1="{header_h}" x2="{vbox_w}" y2="{header_h}" class="grid-line" stroke="#184225" stroke-width="1.2" />
  {all_h_lines_str}

  <!-- Vertical Column Lines Spanning Entire Table -->
  <line x1="{col2_x}" y1="0" x2="{col2_x}" y2="{total_h}" class="grid-line" />
  <line x1="{col3_x}" y1="0" x2="{col3_x}" y2="{total_h}" class="grid-line" />
  <line x1="{col4_x}" y1="0" x2="{col4_x}" y2="{total_h}" class="grid-line" />

  <!-- Rows Content -->
{all_rows_str}
</svg>"""

    # Validate SVG XML
    ET.fromstring(unified_table_svg)

    for fname in ["secondary-arsenal-table.svg", "secondary-arsenal-table-v6.svg"]:
        out_path = os.path.join(assets_dir, fname)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(unified_table_svg)
        print(f"Generated & Validated: {fname}")

if __name__ == "__main__":
    generate_unified_secondary_table()
