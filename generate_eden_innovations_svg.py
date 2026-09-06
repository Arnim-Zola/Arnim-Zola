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

    items_data = [
        {
            "title": "Multimodal Perception",
            "lines": [
                ('Synchronized <tspan class="hi">EasyOCR</tspan> (on-screen text) + <tspan class="hi">OpenAI Whisper</tspan> (speech transcription) + <tspan class="hi">OpenCV</tspan> (4fps keyframes)—',),
                ('watching video frames, reading captions, and transcribing spoken dialogue simultaneously to match words with visuals.',)
            ]
        },
        {
            "title": "Political Agenda &amp; Bias Analysis",
            "lines": [
                ('Quantifies narrative framing, manipulative bias, and partisan spin using specialized agentic LLM reasoning to detect',),
                ('whether content is pushing biased propaganda, one-sided spin, or intentional exaggeration instead of objective truth.',)
            ]
        },
        {
            "title": "Real-Time OSINT News Verification",
            "lines": [
                ('Dynamically queries live news search APIs and cross-checks authoritative source evidence for every extracted assertion,',),
                ('instantly verifying claims against real-time breaking news and reputable journalism.',)
            ]
        },
        {
            "title": "Dual-Path Fallback Orchestration",
            "lines": [
                ('Asynchronous task chaining via <tspan class="hi">Celery + Redis</tspan> with graceful degradation under API quota limits and GPU constraints,',),
                ('preventing server crashes and slowdowns during viral traffic spikes by queueing requests and rerouting models.',)
            ]
        },
        {
            "title": "Sub-120ms Vector Retrieval",
            "lines": [
                ('Forensic claim embeddings indexed in <tspan class="hi">PostgreSQL (pgvector)</tspan> with <tspan class="hi">HNSW graphs</tspan> for high-speed similarity search,',),
                ('scanning massive databases of past claims and hoaxes in under 120 milliseconds to find matching patterns.',)
            ]
        },
        {
            "title": "Forensic Command HUD &amp; Dossier",
            "lines": [
                ('Threat index telemetry, ⌘K command palette, and one-click PDF intelligence dossier generation with verifiable citations,',),
                ('packaging the entire forensic investigation into an exportable, shareable summary report with clickable proof links.',)
            ]
        },
        {
            "title": "Containerized Infrastructure",
            "lines": [
                ('Fully containerized multi-container deployment with <tspan class="hi">Docker Compose</tspan>, <tspan class="hi">FastAPI / Django REST</tspan>, and <tspan class="hi">React 18</tspan>,',),
                ('isolating APIs, database services, and frontend interfaces into self-contained Docker networks for rapid scaling.',)
            ]
        }
    ]

    items_svg = []
    item_y = 28
    for idx, it in enumerate(items_data):
        t_svg = f'<text x="42" y="{item_y}" class="item-title">▸ {it["title"]}</text>'
        
        # Flanking glowing bullet
        bullet_svg = f'''<circle cx="24" cy="{item_y - 4.5}" r="3" fill="#00ff66" filter="drop-shadow(0 0 3px #00ff66)" />
      <circle cx="24" cy="{item_y - 4.5}" r="1.5" fill="#ffffff" />'''

        line1_svg = f'<text x="42" y="{item_y + 20}" class="item-desc">{it["lines"][0][0]}</text>'
        line2_svg = f'<text x="42" y="{item_y + 40}" class="item-desc">{it["lines"][1][0]}</text>'
        
        # Subtle divider between items (except last)
        div_svg = ""
        if idx < len(items_data) - 1:
            div_svg = f'<line x1="20" y1="{item_y + 54}" x2="{vbox_w - 20}" y2="{item_y + 54}" stroke="#102618" stroke-width="0.8" stroke-dasharray="4 4" />'

        items_svg.append(f"""  <!-- Item {idx + 1}: {it['title']} -->
  <g>
    {bullet_svg}
    {t_svg}
    {line1_svg}
    {line2_svg}
    {div_svg}
  </g>""")

        item_y += 70

    card_h = item_y + 10
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
        font-size: 16px;
        font-weight: 400;
        letter-spacing: 0.4px;
        fill: #00ff66;
        filter: drop-shadow(0 1px 2px rgba(0,0,0,0.8));
      }}
      .item-desc {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 14.5px;
        font-weight: 400;
        letter-spacing: 0.15px;
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

    out_path = os.path.join(assets_dir, "eden-innovations.svg")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    ET.fromstring(svg_content)
    print(f"Generated & Validated: {out_path}")

if __name__ == "__main__":
    generate_eden_innovations_svg()
