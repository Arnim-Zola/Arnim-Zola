import os
import re

def generate_architecture_matrix_svg():
    assets_dir = r"c:\Holidays\Arnim-Zola\assets"
    
    # Read font from taglines.svg
    taglines_path = os.path.join(assets_dir, "taglines.svg")
    with open(taglines_path, "r", encoding="utf-8") as f:
        taglines_content = f.read()

    font_match = re.search(r"@font-face\s*\{[^}]*\}", taglines_content, re.DOTALL)
    font_face_css = font_match.group(0) if font_match else ""

    vbox_w = 920
    header_h = 52
    row_h = 114
    total_h = header_h + row_h * 5  # 52 + 570 = 622

    col1_w = 205
    col2_w = 475
    col3_w = vbox_w - (col1_w + col2_w)  # 240
    col2_x = col1_w
    col3_x = col1_w + col2_w

    # Table rows definition
    rows_data = [
        {
            "pillar": ["Distributed Systems &amp;", "Async Tasks"],
            "desc": [
                ('In <tspan class="hi">Eden</tspan>, video ingestion and frame extraction are offloaded to asynchronous',),
                ('background worker pools via <tspan class="hi">Celery + Redis</tspan>, preventing HTTP server bottlenecks',),
                ('with rate-limit resilient retry fallbacks.',)
            ],
            "badges": [
                [("FastAPI", 62), ("Celery", 56), ("Redis", 50)],
                [("Asyncio", 60)]
            ]
        },
        {
            "pillar": ["Relational &amp; Vector Search", "Architecture"],
            "desc": [
                ('In <tspan class="hi">Eden</tspan>, forensic claims are embedded and indexed in <tspan class="hi">PostgreSQL (pgvector)</tspan>',),
                ('using <tspan class="hi">HNSW graphs</tspan> for sub-120ms nearest-neighbor retrieval, paired with <tspan class="hi">Redis</tspan>',),
                ('caching for high-frequency queries.',)
            ],
            "badges": [
                [("PostgreSQL", 84), ("pgvector", 68)],
                [("HNSW", 50), ("Redis", 50)]
            ]
        },
        {
            "pillar": ["Multimodal Perception &amp;", "Fact RAG"],
            "desc": [
                ('In <tspan class="hi">Eden</tspan>, parallel streams demux visual frames (<tspan class="hi">OpenCV</tspan>) for OCR scanning and',),
                ('audio (<tspan class="hi">OpenAI Whisper</tspan>) for speech transcription, synthesized by deep reasoning',),
                ('LLM agents into an authenticity truth index.',)
            ],
            "badges": [
                [("OpenCV", 60), ("Whisper", 60), ("EasyOCR", 64)],
                [("Multi-Agent RAG", 120)]
            ]
        },
        {
            "pillar": ["Full-Stack &amp; 60FPS 3D", "WebGL"],
            "desc": [
                ('In <tspan class="hi">Quantum OS (In Progress / Active Build)</tspan>, architecting an interactive cyberpunk',),
                ('terminal portfolio with <tspan class="hi">Next.js 15</tspan> and <tspan class="hi">Three.js</tspan>, running custom GPU <tspan class="hi">GLSL fragment</tspan>',),
                ('<tspan class="hi">shaders</tspan> at 60FPS alongside Web Audio API synthesis.',)
            ],
            "badges": [
                [("Next.js 15", 72), ("React 19", 66)],
                [("Three.js", 66), ("GLSL Shaders", 92)]
            ]
        },
        {
            "pillar": ["Containerization &amp;", "Multi-Service Infra"],
            "desc": [
                ('Orchestrated the full multi-service architecture with <tspan class="hi">Docker Compose</tspan>, isolating',),
                ('FastAPI/Django API layers, Celery workers, Redis brokers, and React frontends',),
                ('into reproducible networks.',)
            ],
            "badges": [
                [("Docker Compose", 108), ("Linux/Bash", 82)],
                [("Nginx", 52), ("Git", 40)]
            ]
        }
    ]

    # Generate row SVG markup
    rows_svg = []
    for idx, r in enumerate(rows_data):
        y_top = header_h + idx * row_h
        y_mid = y_top + row_h / 2
        
        # Pillar text (Col 1)
        p_lines = r["pillar"]
        if len(p_lines) == 1:
            p_svg = f'<text x="20" y="{y_mid + 5}" class="pillar-text">{p_lines[0]}</text>'
        else:
            p_y1 = y_mid - 9
            p_y2 = y_mid + 15
            p_svg = f'<text x="20" y="{p_y1}" class="pillar-text">{p_lines[0]}</text>\n      <text x="20" y="{p_y2}" class="pillar-text">{p_lines[1]}</text>'

        # Desc lines (Col 2)
        desc_start_y = y_top + 32
        d_svg_list = []
        for d_idx, d_line in enumerate(r["desc"]):
            dy = desc_start_y + d_idx * 25
            d_svg_list.append(f'<text x="{col2_x + 18}" y="{dy}" class="desc-text">{d_line[0]}</text>')
        desc_svg = "\n      ".join(d_svg_list)

        # Badges (Col 3)
        badge_rows = r["badges"]
        badge_svg_list = []
        b_start_y = y_top + 28
        for b_row_idx, b_list in enumerate(badge_rows):
            by = b_start_y + b_row_idx * 36
            bx = col3_x + 12
            for label, bw in b_list:
                badge_svg_list.append(f'''<g transform="translate({bx}, {by})">
        <rect width="{bw}" height="26" rx="6" class="badge-bg" />
        <text x="{bw/2}" y="17.5" class="badge-text">{label}</text>
      </g>''')
                bx += bw + 6
        badges_svg = "\n      ".join(badge_svg_list)

        rows_svg.append(f"""  <!-- Row {idx + 1} -->
  <g>
    <!-- Col 1: Pillar -->
    <g>
      {p_svg}
    </g>

    <!-- Col 2: Real-World Architecture -->
    <g>
      {desc_svg}
    </g>

    <!-- Col 3: Core Stack Badges -->
    <g>
      {badges_svg}
    </g>
  </g>""")

    all_rows_str = "\n\n".join(rows_svg)

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vbox_w} {total_h}" width="100%" height="{total_h}" fill="none">
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
      .pillar-text {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 16px;
        font-weight: 400;
        letter-spacing: 0.2px;
        fill: #00ff66;
        filter: drop-shadow(0 1px 2px rgba(0,0,0,0.8));
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
        transition: all 0.2s ease;
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

  <!-- Container Box -->
  <rect x="0" y="0" width="{vbox_w}" height="{total_h}" rx="10" fill="#040906" stroke="#163d22" stroke-width="1.5" />

  <!-- Table Header Background -->
  <path d="M 0 10 Q 0 0 10 0 L {vbox_w - 10} 0 Q {vbox_w} 0 {vbox_w} 10 L {vbox_w} {header_h} L 0 {header_h} Z" fill="#07150c" />

  <!-- Header Titles -->
  <text x="20" y="32" class="th-text">Pillar &amp; Domain</text>
  <text x="{col2_x + 18}" y="32" class="th-text">Real-World Architecture &amp; Integration (Eden &amp; Portfolio)</text>
  <text x="{col3_x + 12}" y="32" class="th-text">Core Stack</text>

  <!-- Horizontal Grid Lines -->
  <line x1="0" y1="{header_h}" x2="{vbox_w}" y2="{header_h}" class="grid-line" stroke="#184225" stroke-width="1.2" />
  <line x1="0" y1="{header_h + row_h}" x2="{vbox_w}" y2="{header_h + row_h}" class="grid-line" />
  <line x1="0" y1="{header_h + row_h * 2}" x2="{vbox_w}" y2="{header_h + row_h * 2}" class="grid-line" />
  <line x1="0" y1="{header_h + row_h * 3}" x2="{vbox_w}" y2="{header_h + row_h * 3}" class="grid-line" />
  <line x1="0" y1="{header_h + row_h * 4}" x2="{vbox_w}" y2="{header_h + row_h * 4}" class="grid-line" />

  <!-- Vertical Column Lines -->
  <line x1="{col2_x}" y1="0" x2="{col2_x}" y2="{total_h}" class="grid-line" />
  <line x1="{col3_x}" y1="0" x2="{col3_x}" y2="{total_h}" class="grid-line" />

  <!-- Rows Content -->
{all_rows_str}
</svg>
"""

    for fname in ["architecture-matrix.svg", "architecture-matrix-v2.svg", "architecture-matrix-v3.svg"]:
        out_path = os.path.join(assets_dir, fname)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(svg_content)
        print(f"Generated: {out_path}")

if __name__ == "__main__":
    generate_architecture_matrix_svg()
