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

    # Strategy: viewBox="0 0 920 ..." with width="100%"
    # → On an 850px GitHub container, 20px font renders at ~18-19px actual (big!)
    # → At 20px Caacupe One, avg char ~7.6px → (920-20)/7.6 ≈ 118 chars per line
    #
    # 4 balanced lines — keeps "intersection of" + "core CS systems" on the SAME line:
    # L1 (~99):  "I am a 3rd-year ... DSATM, Bengaluru (Class of 2028),"
    # L2 (~102): "building at the intersection of core CS systems ... production-grade GenAI &"
    # L3 (~104): "Full-Stack engineering. My work bridges ... (FastAPI, Celery, Redis,"
    # L4 (~101): "pgvector) with interactive ... (TypeScript, React, Next.js, Three.js)."

    vbox_w     = 920
    font_size  = 19
    line_h     = 28    # line height in px
    top_pad    = 24    # first line y from box top
    bot_pad    = 20    # padding below last line
    num_lines  = 4

    box_height = top_pad + (num_lines - 1) * line_h + bot_pad   # 24+84+20 = 128
    heading_y  = 22
    box_top    = 36
    svg_height = box_top + box_height + 2                        # 36+128+2 = 166

    # line y positions (relative to the box group)
    y1 = top_pad
    y2 = top_pad + line_h
    y3 = top_pad + 2 * line_h
    y4 = top_pad + 3 * line_h

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vbox_w} {svg_height}" width="100%" height="{svg_height}" fill="none">
  <defs>
    <style>
      {font_face_css}

      .sh {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 20px;
        font-weight: 400;
        letter-spacing: 1px;
        fill: #7ee787;
      }}
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
    </style>
  </defs>

  <!-- Section Heading -->
  <text x="0" y="{heading_y}" class="sh">ABOUT ME &amp; IDENTITY</text>

  <!-- Quote Box -->
  <g transform="translate(0, {box_top})">
    <!-- Subtle green tint background -->
    <rect x="0" y="0" width="{vbox_w}" height="{box_height}" rx="6" ry="6" fill="rgba(57,211,83,0.05)"/>
    <!-- Left emerald accent bar -->
    <rect x="0" y="0" width="5" height="{box_height}" rx="2" ry="2" fill="#39d353"/>

    <!-- Line 1: ~110 chars -->
    <text x="20" y="{y1}" class="bt"><tspan>I am a 3rd-year Computer Science &amp; Engineering undergraduate at </tspan><tspan class="hi">DSATM, Bengaluru (Class of 2028)</tspan><tspan>, building at</tspan></text>

    <!-- Line 2: ~101 chars -->
    <text x="20" y="{y2}" class="bt"><tspan>the intersection of </tspan><tspan class="hi">core CS systems (DSA, OS, DBMS, Networks)</tspan><tspan> and </tspan><tspan class="hi">production-grade GenAI &amp; Full-Stack</tspan></text>

    <!-- Line 3: ~104 chars -->
    <text x="20" y="{y3}" class="bt"><tspan class="hi">engineering</tspan><tspan>. My work bridges resilient, low-latency agentic workflows (</tspan><tspan class="hi">FastAPI, Celery, Redis, pgvector</tspan><tspan>)</tspan></text>

    <!-- Line 4: ~91 chars -->
    <text x="20" y="{y4}" class="bt"><tspan>with interactive, high-performance web applications (</tspan><tspan class="hi">TypeScript, React, Next.js, Three.js</tspan><tspan>).</tspan></text>
  </g>
</svg>
"""

    for fname in ["about-me.svg", "about-me-v2.svg", "about-me-v3.svg"]:
        path = os.path.join(assets_dir, fname)
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg_content)
        print(f"  Written: {fname}")

    print(f"\nDone — viewBox {vbox_w}x{svg_height}, font {font_size}px, {num_lines} balanced lines")
    print("Matches localhost blockquote 3-line natural wrap distribution.")

if __name__ == "__main__":
    generate_about_me_svg()
