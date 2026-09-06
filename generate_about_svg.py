import os
import re

def generate_about_me_svg():
    assets_dir = r"c:\Holidays\Arnim-Zola\assets"

    # Read base64 font from taglines.svg
    taglines_path = os.path.join(assets_dir, "taglines.svg")
    with open(taglines_path, "r", encoding="utf-8") as f:
        taglines_content = f.read()

    font_match = re.search(r"@font-face\s*\{[^}]*\}", taglines_content, re.DOTALL)
    font_face_css = font_match.group(0) if font_match else ""

    vbox_w     = 920
    font_size  = 17
    line_h     = 27    # line height in px
    top_pad    = 24    # first line y from box top
    bot_pad    = 20    # padding below last line
    num_lines  = 3

    box_height = top_pad + (num_lines - 1) * line_h + bot_pad   # 24+54+20 = 98
    heading_y  = 25
    box_top    = 42
    svg_height = box_top + box_height + 4                        # 42+98+4 = 144

    # line y positions (relative to the box group)
    y1 = top_pad
    y2 = top_pad + line_h
    y3 = top_pad + 2 * line_h

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vbox_w} {svg_height}" width="100%" height="{svg_height}" fill="none">
  <defs>
    <style>
      {font_face_css}

      .sh {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 28px;
        font-weight: 400;
        letter-spacing: 0.8px;
        fill: #7ee787;
      }}
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
    </style>
  </defs>

  <!-- Section Heading -->
  <text x="0" y="{heading_y}" class="sh">ABOUT ME &amp; IDENTITY</text>

  <!-- Quote Box -->
  <g transform="translate(0, {box_top})">
    <!-- Subtle green tint background -->
    <rect x="0" y="0" width="{vbox_w}" height="{box_height}" rx="6" ry="6" fill="rgba(57,211,83,0.05)"/>
    <!-- Left emerald accent bar -->
    <rect x="0" y="0" width="4" height="{box_height}" rx="2" ry="2" fill="#39d353"/>

    <!-- Line 1 (137 chars, justified) -->
    <text x="20" y="{y1}" textLength="880" lengthAdjust="spacing" class="bt"><tspan>I am a 3rd-year Computer Science &amp; Engineering undergraduate at </tspan><tspan class="hi">DSATM, Bengaluru (Class of 2028)</tspan><tspan>, building at the intersection of </tspan><tspan class="hi">core CS</tspan></text>

    <!-- Line 2 (133 chars, justified) -->
    <text x="20" y="{y2}" textLength="880" lengthAdjust="spacing" class="bt"><tspan class="hi">systems (DSA, OS, DBMS, Networks)</tspan><tspan> and </tspan><tspan class="hi">production-grade GenAI &amp; Full-Stack engineering</tspan><tspan>. My work bridges resilient, low-latency agentic</tspan></text>

    <!-- Line 3 (136 chars, justified) -->
    <text x="20" y="{y3}" textLength="880" lengthAdjust="spacing" class="bt"><tspan>workflows (</tspan><tspan class="hi">FastAPI, Celery, Redis, pgvector</tspan><tspan>) with interactive, high-performance web applications (</tspan><tspan class="hi">TypeScript, React, Next.js, Three.js</tspan><tspan>).</tspan></text>
  </g>
</svg>
"""

    for fname in ["about-me.svg", "about-me-v2.svg", "about-me-v3.svg", "about-me-centered.svg", "about-me-justified.svg", "about-me-v5.svg", "about-me-v6.svg", "about-me-justified-final.svg", "about-me-compact.svg", "about-me-sleek-small.svg", "about-me-perfect.svg"]:
        path = os.path.join(assets_dir, fname)
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg_content)
        print(f"  Written: {fname}")

    print(f"\nDone — viewBox {vbox_w}x{svg_height}, headline 28px #7ee787")

if __name__ == "__main__":
    generate_about_me_svg()
