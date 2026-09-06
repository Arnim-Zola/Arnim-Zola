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
    vbox_h = 32

    # 1. PRIMARY FLAGSHIP: EDEN (Autonomous Misinformation Analysis Engine)
    eden_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vbox_w} {vbox_h}" width="100%" height="{vbox_h}" fill="none">
  <defs>
    <style>
      {font_face_css}
      .heading-green {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 19px;
        font-weight: 400;
        letter-spacing: 0.8px;
        fill: #00ff66;
      }}
      .dim-green {{
        fill: #7ee787;
        font-size: 17px;
        letter-spacing: 0.5px;
      }}
    </style>
  </defs>
  <text x="0" y="22" class="heading-green">PRIMARY FLAGSHIP: EDEN <tspan class="dim-green">(Autonomous Misinformation Analysis Engine)</tspan></text>
</svg>"""

    eden_path = os.path.join(assets_dir, "heading-eden.svg")
    with open(eden_path, "w", encoding="utf-8") as f:
        f.write(eden_svg)
    print(f"Generated: {eden_path}")

    # Also generate full solid green version
    eden_solid_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vbox_w} {vbox_h}" width="100%" height="{vbox_h}" fill="none">
  <defs>
    <style>
      {font_face_css}
      .heading-green {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 19px;
        font-weight: 400;
        letter-spacing: 0.8px;
        fill: #00ff66;
      }}
    </style>
  </defs>
  <text x="0" y="22" class="heading-green">PRIMARY FLAGSHIP: EDEN (Autonomous Misinformation Analysis Engine)</text>
</svg>"""

    eden_solid_path = os.path.join(assets_dir, "heading-eden-solid.svg")
    with open(eden_solid_path, "w", encoding="utf-8") as f:
        f.write(eden_solid_svg)
    print(f"Generated: {eden_solid_path}")

    # 2. Secondary Arsenal Heading
    secondary_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vbox_w} {vbox_h}" width="100%" height="{vbox_h}" fill="none">
  <defs>
    <style>
      {font_face_css}
      .heading-green {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 19px;
        font-weight: 400;
        letter-spacing: 0.8px;
        fill: #00ff66;
      }}
    </style>
  </defs>
  <text x="0" y="22" class="heading-green">SECONDARY ARSENAL &amp; CREATIVE WEBGL LABS</text>
</svg>"""
    sec_path = os.path.join(assets_dir, "heading-secondary.svg")
    with open(sec_path, "w", encoding="utf-8") as f:
        f.write(secondary_svg)
    print(f"Generated: {sec_path}")

    # 3. Technical Arsenal Heading
    tech_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vbox_w} {vbox_h}" width="100%" height="{vbox_h}" fill="none">
  <defs>
    <style>
      {font_face_css}
      .heading-green {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 19px;
        font-weight: 400;
        letter-spacing: 0.8px;
        fill: #00ff66;
      }}
    </style>
  </defs>
  <text x="0" y="22" class="heading-green">TECHNICAL ARSENAL</text>
</svg>"""
    tech_path = os.path.join(assets_dir, "heading-technical.svg")
    with open(tech_path, "w", encoding="utf-8") as f:
        f.write(tech_svg)
    print(f"Generated: {tech_path}")

    # 4. Telemetry & Stats Heading
    telemetry_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vbox_w} {vbox_h}" width="100%" height="{vbox_h}" fill="none">
  <defs>
    <style>
      {font_face_css}
      .heading-green {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 19px;
        font-weight: 400;
        letter-spacing: 0.8px;
        fill: #00ff66;
      }}
    </style>
  </defs>
  <text x="0" y="22" class="heading-green">REAL-TIME TELEMETRY &amp; CODING STATS</text>
</svg>"""
    telemetry_path = os.path.join(assets_dir, "heading-telemetry.svg")
    with open(telemetry_path, "w", encoding="utf-8") as f:
        f.write(telemetry_svg)
    print(f"Generated: {telemetry_path}")

if __name__ == "__main__":
    generate_heading_svgs()
