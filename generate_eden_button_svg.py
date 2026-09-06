import os
import re

def generate_eden_button_svg():
    assets_dir = r"c:\Holidays\Arnim-Zola\assets"

    # Read base64 font from taglines.svg
    taglines_path = os.path.join(assets_dir, "taglines.svg")
    with open(taglines_path, "r", encoding="utf-8") as f:
        taglines_content = f.read()

    font_match = re.search(r"@font-face\s*\{[^}]*\}", taglines_content, re.DOTALL)
    font_face_css = font_match.group(0) if font_match else ""

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 150 150" width="150" height="150" fill="none">
  <defs>
    <clipPath id="buttonCardClip">
      <rect x="5" y="5" width="134" height="134" rx="16" />
    </clipPath>
  </defs>

  <style><![CDATA[
    {font_face_css}

    /* Outer Card Drop Shadow (Brutalist) */
    .brutalist-shadow {{
      fill: #000000;
    }}

    /* Brutalist Card Background and Color Shift */
    .card-bg {{
      animation: cardColorShift 6s cubic-bezier(0.4, 0, 0.2, 1) infinite;
      stroke: #000000;
      stroke-width: 3.5;
    }}

    @keyframes cardColorShift {{
      0%, 40% {{
        fill: #1b4d2e;
      }}
      48%, 90% {{
        fill: #238636;
      }}
      96%, 100% {{
        fill: #1b4d2e;
      }}
    }}

    /* Circular Badge Transform and Move */
    .logo-badge-group {{
      animation: badgeMoveScale 6s cubic-bezier(0.68, -0.55, 0.265, 1.55) infinite;
    }}

    @keyframes badgeMoveScale {{
      0%, 40% {{
        transform: translate(72px, 72px) scale(1);
      }}
      48%, 90% {{
        transform: translate(72px, 44px) scale(0.62);
      }}
      96%, 100% {{
        transform: translate(72px, 72px) scale(1);
      }}
    }}

    /* Icon Continuous Spin in Active State */
    .icon-spin-group {{
      animation: iconContinuousSpin 6s cubic-bezier(0.68, -0.55, 0.265, 1.55) infinite;
    }}

    @keyframes iconContinuousSpin {{
      0%, 40% {{
        transform: rotate(0deg);
      }}
      48%, 90% {{
        transform: rotate(360deg);
      }}
      96%, 100% {{
        transform: rotate(0deg);
      }}
    }}

    /* Reveal Text Animation */
    .button-text-group {{
      animation: textSlideReveal 6s cubic-bezier(0.68, -0.55, 0.265, 1.55) infinite;
    }}

    @keyframes textSlideReveal {{
      0%, 40% {{
        opacity: 0;
        transform: translateY(18px);
      }}
      48%, 90% {{
        opacity: 1;
        transform: translateY(0px);
      }}
      96%, 100% {{
        opacity: 0;
        transform: translateY(18px);
      }}
    }}

    .sub-label {{
      font-family: 'Caacupe One', cursive, sans-serif;
      font-size: 11.5px;
      font-weight: 400;
      letter-spacing: 1.2px;
      fill: #a3e635;
      text-anchor: middle;
    }}

    .main-label {{
      font-family: 'Caacupe One', cursive, sans-serif;
      font-size: 15px;
      font-weight: 400;
      letter-spacing: 2px;
      fill: #ffffff;
      text-anchor: middle;
    }}
  ]]></style>

  <!-- Brutalist Hard Shadow -->
  <rect x="11" y="11" width="134" height="134" rx="16" class="brutalist-shadow" />

  <!-- Brutalist Card Box -->
  <rect x="7" y="7" width="134" height="134" rx="16" class="card-bg" />

  <!-- Animated Circular Logo Badge -->
  <g class="logo-badge-group">
    <!-- Badge Shadow -->
    <circle cx="2" cy="2" r="38" fill="#000000" />
    
    <!-- Badge Circle -->
    <circle cx="0" cy="0" r="38" fill="#07150c" stroke="#000000" stroke-width="2.5" />

    <!-- Spinning Instagram / Camera Icon -->
    <g class="icon-spin-group">
      <!-- Centered SVG Icon (Instagram Glyph) -->
      <g transform="translate(-20, -20) scale(1.66)">
        <path fill="#ffffff" d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
      </g>
    </g>
  </g>

  <!-- Animated Revealed Text (SYNTHETIC LIES / PURGE) -->
  <g class="button-text-group">
    <text x="74" y="98" class="sub-label">SYNTHETIC LIES</text>
    <text x="74" y="118" class="main-label">PURGE</text>
  </g>
</svg>"""

    for fname in ["eden-button.svg", "eden-logo.svg", "btn-eden.svg"]:
        out_path = os.path.join(assets_dir, fname)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(svg_content)
        print(f"Generated: {out_path}")

if __name__ == "__main__":
    generate_eden_button_svg()
