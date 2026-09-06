import os
import re
import xml.etree.ElementTree as ET

def generate_eden_pipeline_table_svg():
    assets_dir = r"c:\Holidays\Arnim-Zola\assets"

    # Read base64 font from taglines.svg
    taglines_path = os.path.join(assets_dir, "taglines.svg")
    with open(taglines_path, "r", encoding="utf-8") as f:
        taglines_content = f.read()

    font_match = re.search(r"@font-face\s*\{[^}]*\}", taglines_content, re.DOTALL)
    font_face_css = font_match.group(0) if font_match else ""

    vbox_w = 920
    table_top = 40
    header_h = 50
    row_h = 104
    num_rows = 6
    total_table_h = header_h + num_rows * row_h  # 50 + 624 = 674
    total_svg_h = table_top + total_table_h + 4   # 718

    col1_w = 125
    col2_w = 180
    col3_w = 415
    col4_w = vbox_w - (col1_w + col2_w + col3_w) # 200

    col2_x = col1_w
    col3_x = col1_w + col2_w
    col4_x = col1_w + col2_w + col3_w

    rows_data = [
        {
            "stage": "Stage 01",
            "name": "Stream Ingestion",
            "desc": [
                ('Ingests <tspan class="hi">Instagram Reels</tspan>, carousel posts, and raw video files without',),
                ('crashing the server via asynchronous <tspan class="hi">Celery + Redis</tspan> queues.',)
            ],
            "badges": [[("Celery", 60), ("Redis", 54)], [("FastAPI", 66)]]
        },
        {
            "stage": "Stage 02A",
            "name": "Visual Perception",
            "desc": [
                ('Extracts clean image frames (<tspan class="hi">4 frames/sec</tspan>) and uses OCR to scan',),
                ('and read all on-screen captions, headlines, and overlay text.',)
            ],
            "badges": [[("OpenCV", 64), ("EasyOCR", 68)]]
        },
        {
            "stage": "Stage 02B",
            "name": "Auditory Perception",
            "desc": [
                ('Slices audio track, transcribes spoken speech to text using <tspan class="hi">Whisper</tspan>,',),
                ('and breaks long audio into time-stamped factual claim sentences.',)
            ],
            "badges": [[("Whisper", 64), ("FFmpeg", 64)]]
        },
        {
            "stage": "Stage 03",
            "name": "Temporal Fusion",
            "desc": [
                ('Synchronizes spoken words with on-screen visual text at the exact',),
                ('millisecond so every claim is tied to its precise visual context.',)
            ],
            "badges": [[("Cross-Modal", 88), ("FFmpeg", 62)], [("Temporal Sync", 94), ("Asyncio", 62)]]
        },
        {
            "stage": "Stage 04",
            "name": "OSINT Engine",
            "desc": [
                ('Autonomous AI agents query live news search APIs and cross-check',),
                ('verified knowledge bases using sub-120ms <tspan class="hi">pgvector</tspan> retrieval.',)
            ],
            "badges": [[("Multi-Agent RAG", 122)], [("pgvector", 70), ("LangChain", 78)]]
        },
        {
            "stage": "Stage 05",
            "name": "Forensic Truth Dossier",
            "desc": [
                ('Evaluates political bias and manipulative framing, calculates an authenticity',),
                ('score (<tspan class="hi">Truth Index %</tspan>), and compiles a 1-click PDF dossier.',)
            ],
            "badges": [[("LLM Reasoners", 106)], [("PDF Dossier", 86)]]
        }
    ]

    rows_svg = []
    for idx, r in enumerate(rows_data):
        y_top = table_top + header_h + idx * row_h
        y_mid = y_top + row_h / 2

        # Col 1: Stage
        stage_svg = f'<text x="18" y="{y_mid + 5}" class="stage-text">{r["stage"]}</text>'

        # Col 2: Name
        name_svg = f'<text x="{col2_x + 14}" y="{y_mid + 5}" class="name-text">{r["name"]}</text>'

        # Col 3: Desc
        desc_start_y = y_top + 38
        d_svg_list = []
        for d_idx, d_line in enumerate(r["desc"]):
            dy = desc_start_y + d_idx * 26
            d_svg_list.append(f'<text x="{col3_x + 14}" y="{dy}" class="desc-text">{d_line[0]}</text>')
        desc_svg = "\n      ".join(d_svg_list)

        # Col 4: Badges
        badge_rows = r["badges"]
        badge_svg_list = []
        if len(badge_rows) == 1:
            b_start_y = y_mid - 13
        else:
            b_start_y = y_top + 22

        for b_row_idx, b_list in enumerate(badge_rows):
            by = b_start_y + b_row_idx * 34
            bx = col4_x + 10
            for label, bw in b_list:
                badge_svg_list.append(f'''<g transform="translate({bx}, {by})">
        <rect width="{bw}" height="26" rx="6" class="badge-bg" />
        <text x="{bw/2}" y="17.5" class="badge-text">{label}</text>
      </g>''')
                bx += bw + 6
        badges_svg = "\n      ".join(badge_svg_list)

        rows_svg.append(f"""  <!-- Row {idx + 1}: {r['stage']} -->
  <g>
    {stage_svg}
    {name_svg}
    {desc_svg}
    {badges_svg}
  </g>""")

    all_rows_str = "\n\n".join(rows_svg)

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vbox_w} {total_svg_h}" width="100%" height="{total_svg_h}" fill="none">
  <defs>
    <style>
      {font_face_css}

      .section-headline {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 26px;
        font-weight: 400;
        letter-spacing: 0.8px;
        fill: #7ee787;
      }}
      .th-text {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 17px;
        font-weight: 400;
        letter-spacing: 0.6px;
        fill: #7ee787;
      }}
      .stage-text {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 16px;
        font-weight: 400;
        letter-spacing: 0.3px;
        fill: #00ff66;
        filter: drop-shadow(0 1px 2px rgba(0,0,0,0.8));
      }}
      .name-text {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 16px;
        font-weight: 400;
        letter-spacing: 0.2px;
        fill: #ffffff;
      }}
      .desc-text {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 15px;
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
        font-size: 13px;
        font-weight: 400;
        letter-spacing: 0.3px;
        fill: #39d353;
        text-anchor: middle;
      }}
      .grid-line {{
        stroke: #102618;
        stroke-width: 1;
      }}
    </style>
  </defs>

  <!-- Section Title -->
  <text x="0" y="24" class="section-headline">Multimodal Pipeline Execution (Stage-by-Stage)</text>

  <!-- Table Container Box -->
  <g transform="translate(0, {table_top})">
    <rect x="0" y="0" width="{vbox_w}" height="{total_table_h}" rx="10" fill="#040906" stroke="#163d22" stroke-width="1.5" />

    <!-- Table Header Background -->
    <path d="M 0 10 Q 0 0 10 0 L {vbox_w - 10} 0 Q {vbox_w} 0 {vbox_w} 10 L {vbox_w} {header_h} L 0 {header_h} Z" fill="#07150c" />

    <!-- Header Column Titles -->
    <text x="18" y="31" class="th-text">Stage &amp; Node</text>
    <text x="{col2_x + 14}" y="31" class="th-text">Name</text>
    <text x="{col3_x + 14}" y="31" class="th-text">Plain English Breakdown (What Happens Here)</text>
    <text x="{col4_x + 10}" y="31" class="th-text">Core Stack</text>

    <!-- Horizontal Grid Lines -->
    <line x1="0" y1="{header_h}" x2="{vbox_w}" y2="{header_h}" class="grid-line" stroke="#184225" stroke-width="1.2" />
    <line x1="0" y1="{header_h + row_h}" x2="{vbox_w}" y2="{header_h + row_h}" class="grid-line" />
    <line x1="0" y1="{header_h + row_h * 2}" x2="{vbox_w}" y2="{header_h + row_h * 2}" class="grid-line" />
    <line x1="0" y1="{header_h + row_h * 3}" x2="{vbox_w}" y2="{header_h + row_h * 3}" class="grid-line" />
    <line x1="0" y1="{header_h + row_h * 4}" x2="{vbox_w}" y2="{header_h + row_h * 4}" class="grid-line" />
    <line x1="0" y1="{header_h + row_h * 5}" x2="{vbox_w}" y2="{header_h + row_h * 5}" class="grid-line" />

    <!-- Vertical Column Lines -->
    <line x1="{col2_x}" y1="0" x2="{col2_x}" y2="{total_table_h}" class="grid-line" />
    <line x1="{col3_x}" y1="0" x2="{col3_x}" y2="{total_table_h}" class="grid-line" />
    <line x1="{col4_x}" y1="0" x2="{col4_x}" y2="{total_table_h}" class="grid-line" />
  </g>

  <!-- Table Rows Content -->
{all_rows_str}
</svg>"""

    out_path = os.path.join(assets_dir, "eden-pipeline-table.svg")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    ET.fromstring(svg_content)
    print(f"Generated & Validated: {out_path}")

if __name__ == "__main__":
    generate_eden_pipeline_table_svg()
