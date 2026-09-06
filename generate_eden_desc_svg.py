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
    font_size  = 17
    line_h     = 27
    top_pad    = 24
    bot_pad    = 20
    num_lines  = 3

    box_height = top_pad + (num_lines - 1) * line_h + bot_pad   # 24 + 54 + 20 = 98
    svg_height = box_height + 4                                  # 102

    y1 = top_pad
    y2 = top_pad + line_h
    y3 = top_pad + 2 * line_h

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vbox_w} {svg_height}" width="100%" height="{svg_height}" fill="none">
  <defs>
    <style>
      {font_face_css}

      .bt {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: {font_size}px;
        font-weight: 400;
        letter-spacing: 0.2px;
        fill: #e6edf3;
      }}
      .hi {{
        fill: #39d353;
      }}
      .brand {{
        fill: #00ff66;
      }}
    </style>
  </defs>

  <!-- Quote Box Container (Identical to About Me) -->
  <g transform="translate(0, 2)">
    <!-- Subtle green tint background -->
    <rect x="0" y="0" width="{vbox_w}" height="{box_height}" rx="6" ry="6" fill="rgba(57,211,83,0.05)"/>
    <!-- Left emerald accent bar -->
    <rect x="0" y="0" width="4" height="{box_height}" rx="2" ry="2" fill="#39d353"/>

    <!-- Line 1 (147 chars, justified) -->
    <text x="20" y="{y1}" textLength="880" lengthAdjust="spacing" class="bt"><tspan class="brand">Eden</tspan><tspan> is a state-of-the-art </tspan><tspan class="hi">forensic media fact-checking &amp; multimodal analysis terminal</tspan><tspan>. It ingests short-form social media content (</tspan><tspan class="hi">Instagram Reels,</tspan></text>

    <!-- Line 2 (146 chars, justified) -->
    <text x="20" y="{y2}" textLength="880" lengthAdjust="spacing" class="bt"><tspan class="hi">posts, &amp; direct video uploads</tspan><tspan>), decomposes </tspan><tspan class="hi">visual &amp; auditory streams</tspan><tspan> into </tspan><tspan class="hi">discrete temporal artifacts</tspan><tspan>, detects </tspan><tspan class="hi">political bias &amp; narrative agendas,</tspan></text>

    <!-- Line 3 (138 chars, justified) -->
    <text x="20" y="{y3}" textLength="880" lengthAdjust="spacing" class="bt"><tspan>cross-references claims against </tspan><tspan class="hi">real-time authoritative news sources</tspan><tspan> via </tspan><tspan class="hi">OSINT pipelines</tspan><tspan>, and computes a comprehensive </tspan><tspan class="hi">forensic truth index</tspan><tspan>.</tspan></text>
  </g>
</svg>"""

    for fname in ["eden-desc-v3.svg", "eden-desc-v2.svg", "eden-desc.svg"]:
        out_path = os.path.join(assets_dir, fname)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(svg_content)
        ET.fromstring(svg_content)
        print(f"Generated & Validated: {out_path}")

if __name__ == "__main__":
    generate_eden_desc_svg()
