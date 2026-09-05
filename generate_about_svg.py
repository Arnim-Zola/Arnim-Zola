import os
import re

def generate_about_me_svg():
    assets_dir = r"c:\Holidays\Arnim-Zola\assets"
    os.makedirs(assets_dir, exist_ok=True)

    # Read base64 font from taglines.svg
    taglines_path = os.path.join(assets_dir, "taglines.svg")
    with open(taglines_path, "r", encoding="utf-8") as f:
        taglines_content = f.read()

    font_match = re.search(r"@font-face\s*\{[^}]*\}", taglines_content, re.DOTALL)
    font_face_css = font_match.group(0) if font_match else ""

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 175" width="100%" height="175" fill="none">
  <defs>
    <style>
      {font_face_css}

      .section-heading {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 19px;
        font-weight: 400;
        letter-spacing: 1px;
        fill: #7ee787;
      }}
      .quote-bg {{
        fill: rgba(57, 211, 83, 0.06);
        stroke: none;
      }}
      .quote-border {{
        fill: #39d353;
      }}
      .bio-text {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 15px;
        font-weight: 400;
        letter-spacing: 0.5px;
        fill: #e6edf3;
      }}
      .highlight {{
        fill: #39d353;
      }}
    </style>
  </defs>

  <!-- Section Title -->
  <text x="0" y="20" class="section-heading">ABOUT ME &amp; IDENTITY</text>

  <!-- Quote Box Container (y=36 to y=170) -->
  <g transform="translate(0, 36)">
    <!-- Subtle Green Tint Background -->
    <rect x="0" y="0" width="900" height="130" rx="6" ry="6" class="quote-bg"/>

    <!-- Left Emerald Accent Bar -->
    <rect x="0" y="0" width="4" height="130" rx="2" ry="2" class="quote-border"/>

    <!-- Formatted Bio Lines with Green & White Interleaved Highlights -->
    <!-- Line 1 -->
    <text x="20" y="28" class="bio-text">
      <tspan>I am a 3rd-year Computer Science &amp; Engineering undergraduate at </tspan>
      <tspan class="highlight">DSATM, Bengaluru (Class of 2028)</tspan>
      <tspan>, building at</tspan>
    </text>

    <!-- Line 2 -->
    <text x="20" y="52" class="bio-text">
      <tspan>the intersection of </tspan>
      <tspan class="highlight">core CS systems (DSA, OS, DBMS, Networks)</tspan>
      <tspan> and </tspan>
      <tspan class="highlight">production-grade GenAI &amp; Full-Stack</tspan>
    </text>

    <!-- Line 3 -->
    <text x="20" y="76" class="bio-text">
      <tspan class="highlight">engineering</tspan>
      <tspan>. My work bridges resilient, low-latency agentic workflows (</tspan>
      <tspan class="highlight">FastAPI, Celery, Redis, pgvector</tspan>
      <tspan>)</tspan>
    </text>

    <!-- Line 4 -->
    <text x="20" y="100" class="bio-text">
      <tspan>with interactive, high-performance web applications (</tspan>
      <tspan class="highlight">TypeScript, React, Next.js, Three.js</tspan>
      <tspan>).</tspan>
    </text>
  </g>
</svg>
"""

    with open(os.path.join(assets_dir, "about-me.svg"), "w", encoding="utf-8") as f:
        f.write(svg_content)

    print("Created assets/about-me.svg successfully!")

if __name__ == "__main__":
    generate_about_me_svg()
