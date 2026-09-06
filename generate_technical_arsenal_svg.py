import os
import re
import xml.etree.ElementTree as ET

def generate_technical_arsenal_svg():
    assets_dir = r"c:\Holidays\Arnim-Zola\assets"

    # Read base64 font from taglines.svg
    taglines_path = os.path.join(assets_dir, "taglines.svg")
    with open(taglines_path, "r", encoding="utf-8") as f:
        taglines_content = f.read()

    font_match = re.search(r"@font-face\s*\{[^}]*\}", taglines_content, re.DOTALL)
    font_face_css = font_match.group(0) if font_match else ""

    vbox_w = 920
    table_top = 0
    header_h = 46
    row_h = 88
    num_rows = 5
    total_table_h = header_h + num_rows * row_h  # 46 + 440 = 486
    total_svg_h = table_top + total_table_h + 4   # 490

    col1_w = 245
    col2_w = vbox_w - col1_w                      # 675
    col2_x = col1_w

    domains_data = [
        {
            "domain": "Languages &amp; Shaders",
            "badges": [
                [("Python 3.11", 86, True), ("TypeScript", 84, False), ("JavaScript (ES6+)", 124, False), ("GLSL Shaders", 98, True)],
                [("C++", 48, False), ("SQL", 46, False), ("Bash / Linux", 92, False)]
            ]
        },
        {
            "domain": "Applied AI, Vision &amp; NLP",
            "badges": [
                [("Google Gemini 2.0", 126, True), ("Meta Llama 3 (8B)", 126, True), ("PyTorch", 68, True), ("OpenCV", 68, False)],
                [("OpenAI Whisper", 108, False), ("EasyOCR", 74, False), ("pgvector (HNSW)", 118, True), ("LangChain", 86, False)]
            ]
        },
        {
            "domain": "Distributed Backend &amp; Scraping",
            "badges": [
                [("FastAPI", 68, True), ("Django", 66, False), ("Django REST", 92, False), ("Celery", 64, True)],
                [("Redis", 58, True), ("Playwright", 82, False), ("RESTful APIs", 96, False)]
            ]
        },
        {
            "domain": "Creative WebGL, 3D &amp; Frontend",
            "badges": [
                [("Next.js 15", 76, True), ("React 19", 70, False), ("Three.js", 68, True), ("@react-three/fiber", 126, False)],
                [("Web Audio API", 102, False), ("Plotly.js", 70, False), ("PDF.js", 60, False), ("Tailwind CSS", 94, False)]
            ]
        },
        {
            "domain": "Databases, DevOps &amp; Media",
            "badges": [
                [("PostgreSQL", 86, True), ("SQLite", 60, False), ("MongoDB", 76, False), ("Docker", 66, True)],
                [("Docker Compose", 114, False), ("Git", 46, False), ("GitHub Actions", 106, True), ("FFmpeg", 70, False)]
            ]
        }
    ]

    rows_svg = []
    for idx, r in enumerate(domains_data):
        y_top = table_top + header_h + idx * row_h
        y_mid = y_top + row_h / 2

        # Col 1: Domain Title (Crisp White with Glowing Emerald Dot)
        col1_svg = f'''<g>
      <circle cx="20" cy="{y_mid + 1}" r="3" fill="#00ff66" filter="drop-shadow(0 0 3px #00ff66)" />
      <circle cx="20" cy="{y_mid + 1}" r="1.5" fill="#ffffff" />
      <text x="32" y="{y_mid + 6}" class="domain-title">{r["domain"]}</text>
    </g>'''

        # Col 2: Badges (Balanced mix of White and Neon Green text)
        badge_rows = r["badges"]
        badge_svg_list = []
        b_start_y = y_top + 14
        for b_row_idx, b_list in enumerate(badge_rows):
            by = b_start_y + b_row_idx * 33
            bx = col2_x + 16
            for item in b_list:
                label = item[0]
                bw = item[1]
                is_hi = item[2] if len(item) > 2 else False
                text_cls = "badge-text-hi" if is_hi else "badge-text"
                badge_svg_list.append(f'''<g transform="translate({bx}, {by})">
        <rect width="{bw}" height="26" rx="6" class="badge-bg" />
        <text x="{bw/2}" y="17.5" class="{text_cls}">{label}</text>
      </g>''')
                bx += bw + 8
        col2_svg = "\n      ".join(badge_svg_list)

        rows_svg.append(f"""  <!-- Row {idx + 1}: {r['domain']} -->
  <g>
    {col1_svg}
    {col2_svg}
  </g>""")

    all_rows_str = "\n\n".join(rows_svg)

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vbox_w} {total_svg_h}" width="100%" height="{total_svg_h}" fill="none">
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
      .domain-title {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 16.5px;
        font-weight: 400;
        letter-spacing: 0.2px;
        fill: #ffffff;
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
        letter-spacing: 0.2px;
        fill: #ffffff;
        text-anchor: middle;
      }}
      .badge-text-hi {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 12.5px;
        font-weight: 400;
        letter-spacing: 0.2px;
        fill: #00ff66;
        text-anchor: middle;
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
    <text x="20" y="29" class="th-text">System Domain</text>
    <text x="{col2_x + 16}" y="29" class="th-text">Core Technologies &amp; Production Tooling</text>

    <!-- Horizontal Grid Lines -->
    <line x1="0" y1="{header_h}" x2="{vbox_w}" y2="{header_h}" class="grid-line" stroke="#184225" stroke-width="1.2" />
    <line x1="0" y1="{header_h + row_h}" x2="{vbox_w}" y2="{header_h + row_h}" class="grid-line" />
    <line x1="0" y1="{header_h + row_h * 2}" x2="{vbox_w}" y2="{header_h + row_h * 2}" class="grid-line" />
    <line x1="0" y1="{header_h + row_h * 3}" x2="{vbox_w}" y2="{header_h + row_h * 3}" class="grid-line" />
    <line x1="0" y1="{header_h + row_h * 4}" x2="{vbox_w}" y2="{header_h + row_h * 4}" class="grid-line" />

    <!-- Vertical Column Line -->
    <line x1="{col2_x}" y1="0" x2="{col2_x}" y2="{total_table_h}" class="grid-line" />
  </g>

  <!-- Table Rows Content -->
{all_rows_str}
</svg>"""

    for fname in ["technical-arsenal-table.svg", "technical-arsenal-table-v1.svg", "technical-arsenal-table-v2.svg"]:
        out_path = os.path.join(assets_dir, fname)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(svg_content)
    ET.fromstring(svg_content)
    print(f"Generated & Validated: technical-arsenal-table.svg, v1, v2")

if __name__ == "__main__":
    generate_technical_arsenal_svg()
