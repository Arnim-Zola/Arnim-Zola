import os
import re
import xml.etree.ElementTree as ET

def generate_secondary_projects_rows():
    assets_dir = r"c:\Holidays\Arnim-Zola\assets"

    # Read base64 font from taglines.svg
    taglines_path = os.path.join(assets_dir, "taglines.svg")
    with open(taglines_path, "r", encoding="utf-8") as f:
        taglines_content = f.read()

    font_match = re.search(r"@font-face\s*\{[^}]*\}", taglines_content, re.DOTALL)
    font_face_css = font_match.group(0) if font_match else ""

    vbox_w = 920
    header_h = 46
    row_h = 122

    col1_w = 165
    col2_w = 405
    col3_w = 210
    col4_w = vbox_w - (col1_w + col2_w + col3_w) # 140

    col2_x = col1_w
    col3_x = col1_w + col2_w
    col4_x = col1_w + col2_w + col3_w

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
        font-size: 14px;
        font-weight: 400;
        letter-spacing: 0.2px;
        fill: #7ee787;
      }}
      .desc-text {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 14.5px;
        font-weight: 400;
        letter-spacing: 0.2px;
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

    # 1. Header SVG
    header_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vbox_w} {header_h}" width="100%" height="{header_h}" fill="none">
  <defs>
    <style>{shared_css}</style>
  </defs>
  <rect x="0" y="0" width="{vbox_w}" height="{header_h}" rx="8" fill="#07150c" stroke="#163d22" stroke-width="1.5" />
  
  <text x="18" y="29" class="th-text">Project &amp; Domain</text>
  <text x="{col2_x + 14}" y="29" class="th-text">Architecture &amp; Systems Highlights</text>
  <text x="{col3_x + 10}" y="29" class="th-text">Core Stack</text>
  <text x="{col4_x + 10}" y="29" class="th-text">Source Code</text>

  <line x1="{col2_x}" y1="0" x2="{col2_x}" y2="{header_h}" class="grid-line" />
  <line x1="{col3_x}" y1="0" x2="{col3_x}" y2="{header_h}" class="grid-line" />
  <line x1="{col4_x}" y1="0" x2="{col4_x}" y2="{header_h}" class="grid-line" />
</svg>"""

    for fname in ["secondary-table-header.svg", "secondary-table-header-v2.svg"]:
        with open(os.path.join(assets_dir, fname), "w", encoding="utf-8") as f:
            f.write(header_svg)
    ET.fromstring(header_svg)
    print("Generated: secondary-table-header.svg, v2")

    # 2. Individual Rows Data
    projects_data = [
        {
            "id": "campuscart",
            "name": "CampusCart",
            "domain": "Campus Logistics",
            "desc": [
                ('Zero-queue campus print utility eliminating lines before submission deadlines;',),
                ('powered by client-side <tspan class="hi">PDF.js</tspan> parsing &amp; dynamic pricing calculus,',),
                ('3s <tspan class="hi">Django REST</tspan> polling queues, and real-time vendor dashboards in <tspan class="hi">Next.js 14</tspan>.',)
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
                ('Autonomous radar exposing fake hype and predatory price hikes by automating',),
                ('headless <tspan class="hi">Playwright</tspan> scraping, synthesizing 100+ raw customer reviews into',),
                ('sentiment vectors via <tspan class="hi">Meta Llama 3 8B</tspan>, and plotting trends with <tspan class="hi">Plotly.js</tspan>.',)
            ],
            "badges": [
                [("Meta Llama 3", 88), ("FastAPI", 58)],
                [("Playwright", 76), ("Plotly.js", 64)]
            ],
            "repo": "Zemo",
            "active": False
        },
        {
            "id": "brainiac",
            "name": "Brainiac",
            "domain": "Cognitive AI",
            "desc": [
                ('Renders cognitive burnout states into a living 3D simulation featuring an interactive',),
                ('<tspan class="hi">@react-three/fiber</tspan> cortical mesh, computing 30-factor psychometric scoring',),
                ('vectors via <tspan class="hi">PyTorch</tspan>, and generating personalized AI cognitive protocols.',)
            ],
            "badges": [
                [("React 18", 62), ("@react-three/fiber", 120)],
                [("Three.js", 58), ("PyTorch", 58), ("FastAPI", 56)]
            ],
            "repo": "Brainiac",
            "active": False
        },
        {
            "id": "quantum",
            "name": "Quantum OS",
            "domain": "Interactive Portfolio",
            "desc": [
                ('Personal portfolio transformed into a sci-fi cybernetic desktop operating system;',),
                ('powered by custom GPU <tspan class="hi">GLSL fragment shaders</tspan> locked at 60FPS, <tspan class="hi">Web Audio API</tspan>',),
                ('acoustic feedback synthesis, and a streaming edge AI terminal shell.',)
            ],
            "badges": [
                [("Next.js 15", 66), ("GLSL Shaders", 86)],
                [("Three.js", 60), ("Web Audio", 74)]
            ],
            "repo": "Portfolio",
            "active": True
        }
    ]

    for p in projects_data:
        # Col 1: Project Name & Domain
        col1_svg = f'''<text x="18" y="52" class="project-name">{p["name"]}</text>
    <text x="18" y="76" class="domain-text">{p["domain"]}</text>'''

        # Col 2: Desc
        d_svg_list = []
        for d_idx, d_line in enumerate(p["desc"]):
            dy = 34 + d_idx * 26
            d_svg_list.append(f'<text x="{col2_x + 14}" y="{dy}" class="desc-text">{d_line[0]}</text>')
        col2_svg = "\n    ".join(d_svg_list)

        # Col 3: Badges
        badge_svg_list = []
        b_start_y = 28
        for b_row_idx, b_list in enumerate(p["badges"]):
            by = b_start_y + b_row_idx * 34
            bx = col3_x + 10
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
        btn_y = 30 if p["active"] else 45
        active_svg = ""
        if p["active"]:
            active_svg = f'''<g transform="translate({btn_x}, {btn_y + 38})">
      <rect width="{btn_w}" height="20" rx="4" fill="#041208" stroke="#1b4d2e" stroke-width="0.8" />
      <circle cx="12" cy="10" r="3" fill="#00ff66" />
      <text x="22" y="14" class="active-text">Active Build</text>
    </g>'''

        col4_svg = f'''<g transform="translate({btn_x}, {btn_y})">
      <rect width="{btn_w}" height="{btn_h}" rx="6" class="btn-bg" />
      <text x="{btn_w/2}" y="19.5" class="btn-text">Arnim-Zola/{p['repo']} <tspan class="btn-arrow">↗</tspan></text>
    </g>
    {active_svg}'''

        row_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vbox_w} {row_h}" width="100%" height="{row_h}" fill="none">
  <defs>
    <style>{shared_css}</style>
  </defs>
  
  <!-- Container Box -->
  <rect x="0" y="0" width="{vbox_w}" height="{row_h}" rx="8" fill="#040906" stroke="#163d22" stroke-width="1.5" />

  <!-- Vertical Column Lines -->
  <line x1="{col2_x}" y1="0" x2="{col2_x}" y2="{row_h}" class="grid-line" />
  <line x1="{col3_x}" y1="0" x2="{col3_x}" y2="{row_h}" class="grid-line" />
  <line x1="{col4_x}" y1="0" x2="{col4_x}" y2="{row_h}" class="grid-line" />

  <!-- Columns Content -->
  <g>
    {col1_svg}
    {col2_svg}
    {col3_svg}
    {col4_svg}
  </g>
</svg>"""

        for ver in ["", "-v1", "-v2"]:
            fname = f"secondary-row-{p['id']}{ver}.svg"
            out_path = os.path.join(assets_dir, fname)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(row_svg)
            ET.fromstring(row_svg)
            print(f"Generated: {fname}")

if __name__ == "__main__":
    generate_secondary_projects_rows()
