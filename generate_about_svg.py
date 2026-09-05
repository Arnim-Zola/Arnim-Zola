import os
import re

def generate_balanced_about_me_svg():
    assets_dir = r"c:\Holidays\Arnim-Zola\assets"
    
    # Read base64 font from taglines.svg
    taglines_path = os.path.join(assets_dir, "taglines.svg")
    with open(taglines_path, "r", encoding="utf-8") as f:
        taglines_content = f.read()

    font_match = re.search(r"@font-face\s*\{[^}]*\}", taglines_content, re.DOTALL)
    font_face_css = font_match.group(0) if font_match else ""

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 155" width="100%" height="155" fill="none">
  <defs>
    <style>
      {font_face_css}

      .section-heading {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 18px;
        font-weight: 400;
        letter-spacing: 1px;
        fill: #7ee787;
      }}
      .quote-bg {{
        fill: rgba(57, 211, 83, 0.05);
      }}
      .quote-border {{
        fill: #39d353;
      }}
      .bio-text {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 15px;
        font-weight: 400;
        letter-spacing: 0.4px;
        fill: #e6edf3;
      }}
      .highlight {{
        fill: #39d353;
      }}
    </style>
  </defs>

  <!-- Section Title -->
  <text x="0" y="20" class="section-heading">ABOUT ME &amp; IDENTITY</text>

  <!-- Quote Box Container -->
  <g transform="translate(0, 34)">
    <!-- Subtle Green Tint Background filling the entire 900px width -->
    <rect x="0" y="0" width="900" height="114" rx="6" ry="6" class="quote-bg"/>

    <!-- Left Emerald Accent Bar -->
    <rect x="0" y="0" width="4" height="114" rx="2" ry="2" class="quote-border"/>

    <!-- Well-Distributed Full-Width Text Lines -->
    <!-- Line 1 -->
    <text x="18" y="27" class="bio-text">
      <tspan>I am a 3rd-year Computer Science &amp; Engineering undergraduate at </tspan>
      <tspan class="highlight">DSATM, Bengaluru (Class of 2028)</tspan>
      <tspan>, building at the intersection of</tspan>
    </text>

    <!-- Line 2 -->
    <text x="18" y="51" class="bio-text">
      <tspan class="highlight">core CS systems (DSA, OS, DBMS, Networks)</tspan>
      <tspan> and </tspan>
      <tspan class="highlight">production-grade GenAI &amp; Full-Stack engineering</tspan>
      <tspan>. My work bridges resilient,</tspan>
    </text>

    <!-- Line 3 -->
    <text x="18" y="75" class="bio-text">
      <tspan>low-latency agentic workflows (</tspan>
      <tspan class="highlight">FastAPI, Celery, Redis, pgvector</tspan>
      <tspan>) with interactive, high-performance web applications (</tspan>
      <tspan class="highlight">TypeScript, React,</tspan>
    </text>

    <!-- Line 4 -->
    <text x="18" y="99" class="bio-text">
      <tspan class="highlight">Next.js, Three.js</tspan>
      <tspan>).</tspan>
    </text>
  </g>
</svg>
"""

    for fname in ["about-me.svg", "about-me-v2.svg"]:
        with open(os.path.join(assets_dir, fname), "w", encoding="utf-8") as f:
            f.write(svg_content)

    print("Created balanced full-width about-me-v2.svg successfully!")

if __name__ == "__main__":
    generate_balanced_about_me_svg()
