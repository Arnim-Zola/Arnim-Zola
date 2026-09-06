import os
import re
import xml.etree.ElementTree as ET

def generate_eden_innovations_svg():
    assets_dir = r"c:\Holidays\Arnim-Zola\assets"

    # Read base64 font from taglines.svg
    taglines_path = os.path.join(assets_dir, "taglines.svg")
    with open(taglines_path, "r", encoding="utf-8") as f:
        taglines_content = f.read()

    font_match = re.search(r"@font-face\s*\{[^}]*\}", taglines_content, re.DOTALL)
    font_face_css = font_match.group(0) if font_match else ""

    vbox_w = 920
    table_top = 40
    text_len = 860
    text_x = 38

    items_data = [
        {
            "title": "Multimodal Perception",
            "lines": [
                ('<tspan>Synchronized </tspan><tspan class="hi">EasyOCR</tspan><tspan> (on-screen caption OCR) + </tspan><tspan class="hi">OpenAI Whisper</tspan><tspan> (speech-to-text) + </tspan><tspan class="hi">OpenCV</tspan><tspan> (4fps keyframe extraction)—</tspan>',),
                ('<tspan>watching video frames, reading on-screen captions, and transcribing spoken dialogue simultaneously to match words with visuals.</tspan>',)
            ]
        },
        {
            "title": "Political Agenda &amp; Bias Analysis",
            "lines": [
                ('<tspan>Quantifies narrative framing, manipulative bias, and partisan spin using specialized </tspan><tspan class="hi">agentic LLM reasoning engines</tspan><tspan> to detect</tspan>',),
                ('<tspan>whether content is pushing biased propaganda, one-sided spin, or intentional exaggeration instead of verified objective truth.</tspan>',)
            ]
        },
        {
            "title": "Real-Time OSINT News Verification",
            "lines": [
                ('<tspan>Dynamically queries live news search APIs and cross-checks authoritative source evidence for every </tspan><tspan class="hi">extracted claim assertion</tspan><tspan>,</tspan>',),
                ('<tspan>instantly verifying claims against real-time breaking news, verified knowledge repositories, and reputable investigative news.</tspan>',)
            ]
        },
        {
            "title": "Dual-Path Fallback Orchestration",
            "lines": [
                ('<tspan>Asynchronous task chaining via </tspan><tspan class="hi">Celery + Redis</tspan><tspan> with graceful degradation under API quota limits and GPU hardware constraints,</tspan>',),
                ('<tspan>preventing server crashes or slowdowns during viral traffic spikes by queueing worker requests and dynamically rerouting jobs.</tspan>',)
            ]
        },
        {
            "title": "Sub-120ms Vector Retrieval",
            "lines": [
                ('<tspan>Forensic claim embeddings indexed in </tspan><tspan class="hi">PostgreSQL (pgvector)</tspan><tspan> with high-speed </tspan><tspan class="hi">HNSW indexing graphs</tspan><tspan> for rapid similarity search,</tspan>',),
                ('<tspan>scanning massive databases of historical claims, debunked narratives, and viral hoaxes in under 120ms to detect exact patterns.</tspan>',)
            ]
        },
        {
            "title": "Forensic Command HUD &amp; Dossier",
            "lines": [
                ('<tspan>Threat index telemetry, ⌘K command palette, and one-click PDF intelligence dossier generation with </tspan><tspan class="hi">verifiable claim citations</tspan><tspan>,</tspan>',),
                ('<tspan>packaging the entire forensic investigation into an exportable, shareable summary report with clickable cryptographic proofs.</tspan>',)
            ]
        },
        {
            "title": "Containerized Infrastructure",
            "lines": [
                ('<tspan>Fully containerized multi-container deployment architecture with </tspan><tspan class="hi">Docker Compose</tspan><tspan>, </tspan><tspan class="hi">FastAPI / Django REST</tspan><tspan>, and </tspan><tspan class="hi">React 18</tspan><tspan>,</tspan>',),
                ('<tspan>isolating backend APIs, database services, and frontend client interfaces into self-contained Docker networks for safe scaling.</tspan>',)
            ]
        }
    ]

    items_svg = []
    item_y = 30
    for idx, it in enumerate(items_data):
        # Single glowing tech bullet point
        bullet_svg = f'''<circle cx="24" cy="{item_y - 4.5}" r="3" fill="#00ff66" filter="drop-shadow(0 0 3px #00ff66)" />
      <circle cx="24" cy="{item_y - 4.5}" r="1.5" fill="#ffffff" />'''

        t_svg = f'<text x="{text_x}" y="{item_y}" class="item-title">{it["title"]}</text>'

        # Balanced justified description lines matching About Me
        line1_svg = f'<text x="{text_x}" y="{item_y + 24}" textLength="{text_len}" lengthAdjust="spacing" class="item-desc">{it["lines"][0][0]}</text>'
        line2_svg = f'<text x="{text_x}" y="{item_y + 49}" textLength="{text_len}" lengthAdjust="spacing" class="item-desc">{it["lines"][1][0]}</text>'
        
        # Subtle divider between items (except last)
        div_svg = ""
        if idx < len(items_data) - 1:
            div_svg = f'<line x1="20" y1="{item_y + 64}" x2="{vbox_w - 20}" y2="{item_y + 64}" stroke="#102618" stroke-width="0.8" stroke-dasharray="4 4" />'

        items_svg.append(f"""  <!-- Item {idx + 1}: {it['title']} -->
  <g>
    {bullet_svg}
    {t_svg}
    {line1_svg}
    {line2_svg}
    {div_svg}
  </g>""")

        item_y += 80

    card_h = item_y + 6
    total_svg_h = table_top + card_h + 4

    all_items_str = "\n\n".join(items_svg)

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
      .item-title {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 16.5px;
        font-weight: 400;
        letter-spacing: 0.3px;
        fill: #00ff66;
        filter: drop-shadow(0 1px 2px rgba(0,0,0,0.8));
      }}
      .item-desc {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 16px;
        font-weight: 400;
        letter-spacing: 0.2px;
        fill: #e6edf3;
      }}
      .hi {{
        fill: #00ff66;
      }}
    </style>
  </defs>

  <!-- Section Title -->
  <text x="0" y="24" class="section-headline">Eden Architectural Innovations</text>

  <!-- Container Box -->
  <g transform="translate(0, {table_top})">
    <rect x="0" y="0" width="{vbox_w}" height="{card_h}" rx="10" fill="#040906" stroke="#163d22" stroke-width="1.5" />
    
    <!-- Left Neon Accent Bar -->
    <rect x="0" y="10" width="4" height="{card_h - 20}" rx="2" fill="#00ff66" />

    <!-- Items Content -->
{all_items_str}
  </g>
</svg>"""

    for fname in ["eden-innovations.svg", "eden-innovations-v2.svg", "eden-innovations-v3.svg", "eden-innovations-v4.svg"]:
        out_path = os.path.join(assets_dir, fname)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(svg_content)
    ET.fromstring(svg_content)
    print(f"Generated & Validated: eden-innovations.svg, v2, v3, v4")

if __name__ == "__main__":
    generate_eden_innovations_svg()
