import os
import re
import xml.etree.ElementTree as ET

def generate_secondary_projects_svg():
    assets_dir = r"c:\Holidays\Arnim-Zola\assets"

    # Read base64 font from taglines.svg
    taglines_path = os.path.join(assets_dir, "taglines.svg")
    with open(taglines_path, "r", encoding="utf-8") as f:
        taglines_content = f.read()

    font_match = re.search(r"@font-face\s*\{[^}]*\}", taglines_content, re.DOTALL)
    font_face_css = font_match.group(0) if font_match else ""

    vbox_w = 920
    table_top = 0
    header_h = 50
    row_h = 122
    num_rows = 4
    total_table_h = header_h + num_rows * row_h  # 50 + 488 = 538
    total_svg_h = table_top + total_table_h + 4   # 542

    col1_w = 175
    col2_w = 415
    col3_w = 180
    col4_w = vbox_w - (col1_w + col2_w + col3_w) # 150

    col2_x = col1_w
    col3_x = col1_w + col2_w
    col4_x = col1_w + col2_w + col3_w

    projects_data = [
        {
            "name": "CampusCart",
            "domain": "Campus Logistics",
            "domain_w": 118,
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
            "url": "https://github.com/Arnim-Zola/CampusCart",
            "active": False
        },
        {
            "name": "Zemo",
            "domain": "E-Commerce Intel",
            "domain_w": 114,
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
            "url": "https://github.com/Arnim-Zola/Zemo",
            "active": False
        },
        {
            "name": "Brainiac",
            "domain": "Cognitive AI",
            "domain_w": 90,
            "desc": [
                ('Renders cognitive burnout states into a living 3D simulation featuring an interactive',),
                ('<tspan class="hi">@react-three/fiber</tspan> cortical mesh, computing 30-factor psychometric scoring',),
                ('vectors via <tspan class="hi">PyTorch</tspan>, and generating personalized AI cognitive protocols.',)
            ],
            "badges": [
                [("React 18", 60), ("@react-three/fiber", 112)],
                [("Three.js", 60), ("PyTorch", 60), ("FastAPI", 58)]
            ],
            "repo": "Brainiac",
            "url": "https://github.com/Arnim-Zola/Brainiac",
            "active": False
        },
        {
            "name": "Quantum OS",
            "domain": "Interactive Portfolio",
            "domain_w": 132,
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
            "url": "https://github.com/Arnim-Zola/Portfolio",
            "active": True
        }
    ]

    rows_svg = []
    for idx, r in enumerate(projects_data):
        y_top = table_top + header_h + idx * row_h
        y_mid = y_top + row_h / 2

        # Col 1: Project Name & Domain Pill
        name_y = y_top + 42
        dom_y = y_top + 64
        col1_svg = f'''<g>
      <text x="18" y="{name_y}" class="project-name">{r["name"]}</text>
      <g transform="translate(18, {dom_y})">
        <rect width="{r['domain_w']}" height="22" rx="5" class="domain-bg" />
        <text x="{r['domain_w']/2}" y="15" class="domain-text">{r["domain"]}</text>
      </g>
    </g>'''

        # Col 2: Architecture Highlights Description
        desc_start_y = y_top + 34
        d_svg_list = []
        for d_idx, d_line in enumerate(r["desc"]):
            dy = desc_start_y + d_idx * 26
            d_svg_list.append(f'<text x="{col2_x + 14}" y="{dy}" class="desc-text">{d_line[0]}</text>')
        col2_svg = "\n      ".join(d_svg_list)

        # Col 3: Tech Stack Badges
        badge_rows = r["badges"]
        badge_svg_list = []
        b_start_y = y_top + 28
        for b_row_idx, b_list in enumerate(badge_rows):
            by = b_start_y + b_row_idx * 34
            bx = col3_x + 10
            for label, bw in b_list:
                badge_svg_list.append(f'''<g transform="translate({bx}, {by})">
        <rect width="{bw}" height="26" rx="6" class="badge-bg" />
        <text x="{bw/2}" y="17.5" class="badge-text">{label}</text>
      </g>''')
                bx += bw + 6
        col3_svg = "\n      ".join(badge_svg_list)

        # Col 4: Source Code Button & Status
        btn_w = 130
        btn_h = 32
        btn_x = col4_x + 10
        btn_y = y_top + (30 if r["active"] else 45)
        active_svg = ""
        if r["active"]:
            active_svg = f'''<g transform="translate({btn_x}, {btn_y + 40})">
        <rect width="{btn_w}" height="20" rx="4" fill="#041208" stroke="#1b4d2e" stroke-width="0.8" />
        <circle cx="12" cy="10" r="3" fill="#00ff66" />
        <text x="22" y="14" class="active-text">Active Build</text>
      </g>'''

        col4_svg = f'''<a href="{r['url']}" target="_blank">
      <g transform="translate({btn_x}, {btn_y})" class="btn-group">
        <rect width="{btn_w}" height="{btn_h}" rx="6" class="btn-bg" />
        <text x="{btn_w/2 - 7}" y="20.5" class="btn-text">Arnim-Zola/{r['repo']}</text>
        <text x="{btn_w - 14}" y="20" class="btn-arrow">↗</text>
      </g>
      {active_svg}
    </a>'''

        rows_svg.append(f"""  <!-- Row {idx + 1}: {r['name']} -->
  <g>
    {col1_svg}
    {col2_svg}
    {col3_svg}
    {col4_svg}
  </g>""")

    all_rows_str = "\n\n".join(rows_svg)

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {vbox_w} {total_svg_h}" width="100%" height="{total_svg_h}" fill="none">
  <defs>
    <style>
      {font_face_css}

      .th-text {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 17px;
        font-weight: 400;
        letter-spacing: 0.6px;
        fill: #7ee787;
      }}
      .project-name {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 18px;
        font-weight: 400;
        letter-spacing: 0.4px;
        fill: #00ff66;
        filter: drop-shadow(0 1px 2px rgba(0,0,0,0.8));
      }}
      .domain-bg {{
        fill: #06170d;
        stroke: #164d27;
        stroke-width: 1;
      }}
      .domain-text {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 12px;
        font-weight: 400;
        letter-spacing: 0.3px;
        fill: #7ee787;
        text-anchor: middle;
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
        font-size: 12.5px;
        font-weight: 400;
        letter-spacing: 0.3px;
        fill: #39d353;
        text-anchor: middle;
      }}
      .btn-bg {{
        fill: #05140a;
        stroke: #00ff66;
        stroke-width: 1.2;
        transition: all 0.2s ease;
      }}
      .btn-group:hover .btn-bg {{
        fill: #00ff66;
      }}
      .btn-text {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 11.5px;
        font-weight: 400;
        letter-spacing: 0.2px;
        fill: #ffffff;
        text-anchor: middle;
      }}
      .btn-arrow {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 13px;
        font-weight: 400;
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
    </style>
  </defs>

  <!-- Table Container Box -->
  <g transform="translate(0, {table_top})">
    <rect x="0" y="0" width="{vbox_w}" height="{total_table_h}" rx="10" fill="#040906" stroke="#163d22" stroke-width="1.5" />

    <!-- Table Header Background -->
    <path d="M 0 10 Q 0 0 10 0 L {vbox_w - 10} 0 Q {vbox_w} 0 {vbox_w} 10 L {vbox_w} {header_h} L 0 {header_h} Z" fill="#07150c" />

    <!-- Header Column Titles -->
    <text x="18" y="31" class="th-text">Project &amp; Domain</text>
    <text x="{col2_x + 14}" y="31" class="th-text">Architecture &amp; Systems Highlights</text>
    <text x="{col3_x + 10}" y="31" class="th-text">Core Stack</text>
    <text x="{col4_x + 10}" y="31" class="th-text">Source Code</text>

    <!-- Horizontal Grid Lines -->
    <line x1="0" y1="{header_h}" x2="{vbox_w}" y2="{header_h}" class="grid-line" stroke="#184225" stroke-width="1.2" />
    <line x1="0" y1="{header_h + row_h}" x2="{vbox_w}" y2="{header_h + row_h}" class="grid-line" />
    <line x1="0" y1="{header_h + row_h * 2}" x2="{vbox_w}" y2="{header_h + row_h * 2}" class="grid-line" />
    <line x1="0" y1="{header_h + row_h * 3}" x2="{vbox_w}" y2="{header_h + row_h * 3}" class="grid-line" />

    <!-- Vertical Column Lines -->
    <line x1="{col2_x}" y1="0" x2="{col2_x}" y2="{total_table_h}" class="grid-line" />
    <line x1="{col3_x}" y1="0" x2="{col3_x}" y2="{total_table_h}" class="grid-line" />
    <line x1="{col4_x}" y1="0" x2="{col4_x}" y2="{total_table_h}" class="grid-line" />
  </g>

  <!-- Table Rows Content -->
{all_rows_str}
</svg>"""

    for fname in ["secondary-projects-table.svg", "secondary-projects-table-v1.svg"]:
        out_path = os.path.join(assets_dir, fname)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(svg_content)
    ET.fromstring(svg_content)
    print(f"Generated & Validated: secondary-projects-table.svg")

if __name__ == "__main__":
    generate_secondary_projects_svg()
