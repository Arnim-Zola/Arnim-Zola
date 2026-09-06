import os
import re

def generate_heading_svgs():
    assets_dir = r"c:\Holidays\Arnim-Zola\assets"

    # Read base64 font from taglines.svg
    taglines_path = os.path.join(assets_dir, "taglines.svg")
    with open(taglines_path, "r", encoding="utf-8") as f:
        taglines_content = f.read()

    font_match = re.search(r"@font-face\s*\{[^}]*\}", taglines_content, re.DOTALL)
    font_face_css = font_match.group(0) if font_match else ""

    vbox_w = 920
    vbox_h = 36

    headings = {
        "heading-eden.svg": "PRIMARY FLAGSHIP: EDEN (Autonomous Misinformation Analysis Engine)",
        "heading-eden-solid.svg": "PRIMARY FLAGSHIP: EDEN (Autonomous Misinformation Analysis Engine)",
        "heading-secondary.svg": "SECONDARY ARSENAL &amp; CREATIVE WEBGL LABS",
        "heading-technical.svg": "TECHNICAL ARSENAL",
        "heading-telemetry.svg": "REAL-TIME TELEMETRY &amp; CODING STATS"
    }

    for fname, text in headings.items():
        svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vbox_w} {vbox_h}" width="100%" height="{vbox_h}" fill="none">
  <defs>
    <style>
      {font_face_css}
      .h3-text {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 23px;
        font-weight: 400;
        letter-spacing: 0.8px;
        fill: #7ee787;
      }}
    </style>
  </defs>
  <text x="0" y="26" class="h3-text">{text}</text>
</svg>"""
        out_path = os.path.join(assets_dir, fname)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(svg_content)
        print(f"Generated: {out_path}")

if __name__ == "__main__":
    generate_heading_svgs()
