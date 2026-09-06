import os
import re
import xml.etree.ElementTree as ET

def generate_eden_desc_svg():
    assets_dir = r"c:\Holidays\Arnim-Zola\assets"

    # Read base64 font from taglines.svg
    taglines_path = os.path.join(assets_dir, "taglines.svg")
    with open(taglines_path, "r", encoding="utf-8") as f:
        taglines_content = f.read()

    font_match = re.search(r"@font-face\s*\{[^}]*\}", taglines_content, re.DOTALL)
    font_face_css = font_match.group(0) if font_match else ""

    vbox_w     = 920
    font_size  = 18
    line_h     = 30
    top_pad    = 30
    bot_pad    = 24
    num_lines  = 4

    box_height = top_pad + (num_lines - 1) * line_h + bot_pad   # 30 + 90 + 24 = 144
    svg_height = box_height + 4                                  # 148

    y1 = top_pad
    y2 = top_pad + line_h
    y3 = top_pad + 2 * line_h
    y4 = top_pad + 3 * line_h

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vbox_w} {svg_height}" width="100%" height="{svg_height}" fill="none">
  <defs>
    <style>
      {font_face_css}

      .bt {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: {font_size}px;
        font-weight: 400;
        letter-spacing: 0.3px;
        fill: #e6edf3;
      }}
      .hi {{
        fill: #39d353;
      }}
      .brand {{
        fill: #00ff66;
        font-weight: 400;
      }}
    </style>
  </defs>

  <!-- Quote Box Container -->
  <g transform="translate(0, 2)">
    <!-- Card background with subtle green glow and border -->
    <rect x="0" y="0" width="{vbox_w}" height="{box_height}" rx="8" fill="rgba(57,211,83,0.05)" stroke="#1b4d2e" stroke-width="1"/>
    
    <!-- Left emerald accent bar -->
    <rect x="0" y="0" width="5" height="{box_height}" rx="2.5" fill="#00ff66"/>

    <!-- Line 1: Natural Left Aligned -->
    <text x="26" y="{y1}" class="bt"><tspan class="brand">Eden</tspan><tspan> is a state-of-the-art </tspan><tspan class="hi">forensic media fact-checking &amp; multimodal analysis terminal</tspan><tspan>. It ingests short-form</tspan></text>

    <!-- Line 2: Natural Left Aligned -->
    <text x="26" y="{y2}" class="bt"><tspan>social media content (</tspan><tspan class="hi">Instagram Reels, posts, &amp; direct uploads</tspan><tspan>), decomposes </tspan><tspan class="hi">visual &amp; auditory streams</tspan><tspan> into</tspan></text>

    <!-- Line 3: Natural Left Aligned -->
    <text x="26" y="{y3}" class="bt"><tspan class="hi">discrete temporal artifacts</tspan><tspan>, detects </tspan><tspan class="hi">political bias &amp; narrative agendas</tspan><tspan>, cross-references claims against </tspan><tspan class="hi">real-time</tspan></text>

    <!-- Line 4: Natural Left Aligned -->
    <text x="26" y="{y4}" class="bt"><tspan class="hi">authoritative news sources</tspan><tspan> via </tspan><tspan class="hi">OSINT pipelines</tspan><tspan>, and computes a comprehensive </tspan><tspan class="hi">forensic truth index</tspan><tspan>.</tspan></text>
  </g>
</svg>"""

    out_path = os.path.join(assets_dir, "eden-desc.svg")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    ET.fromstring(svg_content)
    print(f"Generated and validated XML: {out_path}")

if __name__ == "__main__":
    generate_eden_desc_svg()
