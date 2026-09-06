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
    header_h = 44

    col1_w = 210
    col2_w = vbox_w - col1_w                      # 710
    col2_x = col1_w

    domains_data = [
        {
            "domain": "Languages &amp; Shaders",
            "row_h": 64,
            "badges": [
                [("Python 3.11", 80), ("TypeScript", 76), ("JavaScript (ES6+)", 116), ("GLSL Shaders", 92), ("C++", 42), ("SQL", 42), ("Bash / Linux", 88)]
            ]
        },
        {
            "domain": "Applied AI, Vision &amp; NLP",
            "row_h": 92,
            "badges": [
                [("Google Gemini 2.0", 118), ("Meta Llama 3 (8B)", 120), ("PyTorch", 62), ("OpenCV", 62), ("OpenAI Whisper", 104), ("EasyOCR", 68)],
                [("pgvector (HNSW)", 112), ("LangChain", 78)]
            ]
        },
        {
            "domain": "Distributed Backend &amp; Scraping",
            "row_h": 64,
            "badges": [
                [("FastAPI", 62), ("Django", 60), ("Django REST Framework", 144), ("Celery", 58), ("Redis", 52), ("Playwright", 78), ("RESTful APIs", 92)]
            ]
        },
        {
            "domain": "Creative WebGL, 3D &amp; Frontend",
            "row_h": 92,
            "badges": [
                [("Next.js 15", 70), ("React 19", 64), ("Three.js", 64), ("@react-three/fiber", 122), ("Web Audio API", 98), ("Plotly.js", 66), ("PDF.js", 54)],
                [("Tailwind CSS", 88)]
            ]
        },
        {
            "domain": "Databases, DevOps &amp; Media",
            "row_h": 64,
            "badges": [
                [("PostgreSQL", 78), ("SQLite", 56), ("MongoDB", 72), ("Docker", 60), ("Docker Compose", 106), ("Git", 40), ("GitHub Actions", 98), ("FFmpeg", 64)]
            ]
        }
    ]

    total_table_h = header_h + sum(d["row_h"] for d in domains_data)
    total_svg_h = table_top + total_table_h + 4

    rows_svg = []
    current_y = table_top + header_h
    h_lines = []

    for idx, r in enumerate(domains_data):
        y_top = current_y
        row_h = r["row_h"]
        y_mid = y_top + row_h / 2

        # Col 1: Domain Title (Emerald Green text matching screenshot)
        col1_svg = f'<text x="18" y="{y_mid + 5}" class="domain-title">{r["domain"]}</text>'

        # Col 2: Badges
        badge_rows = r["badges"]
        badge_svg_list = []
        if len(badge_rows) == 1:
            b_start_y = y_mid - 13
        else:
            b_start_y = y_top + 14

        for b_row_idx, b_list in enumerate(badge_rows):
            by = b_start_y + b_row_idx * 33
            bx = col2_x + 14
            for label, bw in b_list:
                badge_svg_list.append(f'''<g transform="translate({bx}, {by})">
        <rect width="{bw}" height="26" rx="6" class="badge-bg" />
        <text x="{bw/2}" y="17.5" class="badge-text">{label}</text>
      </g>''')
                bx += bw + 6
        col2_svg = "\n      ".join(badge_svg_list)

        rows_svg.append(f"""  <!-- Row {idx + 1}: {r['domain']} -->
  <g>
    {col1_svg}
    {col2_svg}
  </g>""")

        current_y += row_h
        if idx < len(domains_data) - 1:
            h_lines.append(f'<line x1="0" y1="{current_y}" x2="{vbox_w}" y2="{current_y}" class="grid-line" />')

    all_rows_str = "\n\n".join(rows_svg)
    all_h_lines = "\n    ".join(h_lines)

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vbox_w} {total_svg_h}" width="100%" height="{total_svg_h}" fill="none">
  <defs>
    <style>
      {font_face_css}

      .th-text {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 16px;
        font-weight: 400;
        letter-spacing: 0.5px;
        fill: #ffffff;
      }}
      .domain-title {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 15px;
        font-weight: 400;
        letter-spacing: 0.3px;
        fill: #00ff66;
        filter: drop-shadow(0 1px 2px rgba(0,0,0,0.8));
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
        fill: #39d353;
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
    <text x="18" y="28" class="th-text">System Domain</text>
    <text x="{col2_x + 14}" y="28" class="th-text">Core Technologies &amp; Production Tooling</text>

    <!-- Horizontal Grid Lines -->
    <line x1="0" y1="{header_h}" x2="{vbox_w}" y2="{header_h}" class="grid-line" stroke="#184225" stroke-width="1.2" />
    {all_h_lines}

    <!-- Vertical Column Line -->
    <line x1="{col2_x}" y1="0" x2="{col2_x}" y2="{total_table_h}" class="grid-line" />
  </g>

  <!-- Table Rows Content -->
{all_rows_str}
</svg>"""

    for fname in ["technical-arsenal-table.svg", "technical-arsenal-table-v1.svg", "technical-arsenal-table-v2.svg", "technical-arsenal-table-v3.svg", "technical-arsenal-table-v4.svg"]:
        out_path = os.path.join(assets_dir, fname)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(svg_content)
    ET.fromstring(svg_content)
    print(f"Generated & Validated: technical-arsenal-table.svg, v1..v4")

if __name__ == "__main__":
    generate_technical_arsenal_svg()
