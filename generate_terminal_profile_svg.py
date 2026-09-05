import os
import random
import re

def generate_terminal_svg():
    assets_dir = r"c:\Holidays\Arnim-Zola\assets"
    
    # Read font from taglines.svg
    taglines_path = os.path.join(assets_dir, "taglines.svg")
    with open(taglines_path, "r", encoding="utf-8") as f:
        taglines_content = f.read()

    font_match = re.search(r"@font-face\s*\{[^}]*\}", taglines_content, re.DOTALL)
    font_face_css = font_match.group(0) if font_match else ""

    # Dimensions
    vbox_w = 920
    
    # Terminal text lines
    term_lines = [
        ("Engineer:", '"Mohammed Sahil (@Arnim-Zola)"'),
        ("Institution:", '"3rd Year B.E. Computer Science & Engineering @ DSATM (Class of 2028)"'),
        ("Location:", '"Bengaluru, Karnataka, India"'),
        ("Target Roles:", '"Full-Stack AI Developer / GenAI Engineer • SDE"'),
        ("Core Pillars:", '"DSA • OS & Systems • DBMS • Computer Networks • OOP"'),
        ("Daily Drivers:", '"FastAPI, pgvector, OpenCV, Whisper RAG, Next.js 15, Docker"'),
        ("Active Pursuits:", '"Competitive Hackathons, Research Papers, Problem Solving & Full-Stack Projects"')
    ]
    
    # Build text rows
    text_start_y = 52
    text_line_h = 24
    text_svg_list = []
    
    for i, (k, v) in enumerate(term_lines):
        y = text_start_y + i * text_line_h
        text_svg_list.append(f"""    <text x="24" y="{y}" class="t-line">
      <tspan class="t-key">{k:<16}</tspan> <tspan class="t-val">{v}</tspan>
    </text>""")
    
    text_content = "\n".join(text_svg_list)
    
    # Bookshelf position inside terminal
    shelf_top = text_start_y + len(term_lines) * text_line_h + 14
    shelf_w = vbox_w - 48  # 872px
    shelf_h = 130
    shelf_x = 24
    
    # Generate books
    colors = [
        "#b22222", "#871a1a", "#ff6347", "#556b2f", "#39481f",
        "#fa8072", "#008080", "#004d4d", "#bdb76b", "#989244",
        "#808000", "#8b4513", "#2f4f4f", "#cd5c5c", "#bc8f8f",
        "#a52a2a", "#00ff66", "#39d353", "#38bdf8", "#6366f1"
    ]
    
    dark_colors = [
        "#1a1f26", "#21262d", "#282e36", "#1c2128", "#161b22",
        "#24292f", "#2d333b", "#1f242c", "#252b33", "#1b2027"
    ]

    random.seed(42)
    def make_shelf_books(s_y, s_h):
        books = []
        cur_x = 8
        while cur_x < shelf_w - 20:
            b_w = random.randint(12, 24)
            b_h = random.randint(int(s_h * 0.65), s_h - 4)
            b_y = s_y + (s_h - b_h)
            c_idx = random.randint(0, len(colors) - 1)
            d_idx = random.randint(0, len(dark_colors) - 1)
            books.append({
                "x": cur_x,
                "y": b_y,
                "w": b_w,
                "h": b_h,
                "color": colors[c_idx],
                "dark": dark_colors[d_idx],
                "rx": 2
            })
            cur_x += b_w + random.choice([2, 3, 4, 5])
        return books

    tier1 = make_shelf_books(6, 56)
    tier2 = make_shelf_books(68, 56)
    all_books = tier1 + tier2

    dark_rects = []
    color_rects = []
    for b in all_books:
        dark_rects.append(f'<rect x="{b["x"]}" y="{b["y"]}" width="{b["w"]}" height="{b["h"]}" rx="{b["rx"]}" fill="{b["dark"]}" stroke="#0d1117" stroke-width="1"/>')
        color_rects.append(f'<rect x="{b["x"]}" y="{b["y"]}" width="{b["w"]}" height="{b["h"]}" rx="{b["rx"]}" fill="{b["color"]}" stroke="rgba(0,0,0,0.4)" stroke-width="1"/>')
        if b["w"] > 16:
            dark_rects.append(f'<line x1="{b["x"]+4}" y1="{b["y"]+5}" x2="{b["x"]+b["w"]-4}" y2="{b["y"]+5}" stroke="#30363d" stroke-width="1"/>')
            color_rects.append(f'<line x1="{b["x"]+4}" y1="{b["y"]+6}" x2="{b["x"]+b["w"]-4}" y2="{b["y"]+6}" stroke="rgba(255,255,255,0.4)" stroke-width="1.5"/>')

    dark_books_svg = "\n        ".join(dark_rects)
    color_books_svg = "\n        ".join(color_rects)

    total_svg_h = shelf_top + shelf_h + 20

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vbox_w} {total_svg_h}" width="100%" height="{total_svg_h}" fill="none">
  <defs>
    <style>
      {font_face_css}

      .t-win-title {{
        font-family: 'JetBrains Mono', 'Fira Code', monospace;
        font-size: 13px;
        font-weight: 600;
        fill: #8b949e;
      }}
      .t-line {{
        font-family: 'JetBrains Mono', 'Fira Code', monospace;
        font-size: 13px;
        font-weight: 500;
        letter-spacing: 0.2px;
      }}
      .t-key {{
        fill: #39d353;
        font-weight: 700;
      }}
      .t-val {{
        fill: #e6edf3;
      }}
      .t-sub-title {{
        font-family: 'JetBrains Mono', 'Fira Code', monospace;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 1px;
        fill: #7ee787;
      }}

      @keyframes flashlight {{
        0% {{ transform: translate(-100px, 30px); }}
        35% {{ transform: translate(450px, 20px); }}
        39% {{ transform: translate(490px, 85px); opacity: 1; }}
        40% {{ transform: translate(490px, 85px); opacity: 0; }}
        41% {{ transform: translate(490px, 85px); opacity: 1; }}
        42% {{ transform: translate(490px, 85px); opacity: 0; }}
        54% {{ transform: translate(490px, 85px); opacity: 0; }}
        55% {{ transform: translate(490px, 85px); opacity: 1; }}
        59% {{ transform: translate(490px, 85px); opacity: 1; }}
        64% {{ transform: translate(300px, 75px); }}
        68% {{ transform: translate(650px, 90px); }}
        72% {{ transform: translate(490px, 85px); }}
        75% {{ transform: translate(490px, 85px); }}
        100% {{ transform: translate(980px, 50px); }}
      }}

      @keyframes eyes-glow {{
        0%, 38% {{ opacity: 0; transform: scaleY(0); }}
        39%, 40.5% {{ opacity: 1; transform: scaleY(1); fill: #ffffff; filter: drop-shadow(0 0 4px #ffffff); }}
        41% {{ opacity: 0; transform: scaleY(0); }}
        41.5%, 43% {{ opacity: 1; transform: scaleY(1); fill: #ff0033; filter: drop-shadow(0 0 6px #ff0033); }}
        43.5%, 100% {{ opacity: 0; transform: scaleY(0); }}
      }}

      .torch-beam {{
        animation: flashlight 20s ease-in-out infinite;
      }}

      .spooky-eye-pair {{
        transform-origin: 499px 92px;
        animation: eyes-glow 20s infinite;
      }}
    </style>

    <!-- ClipPath for the moving flashlight inside terminal bookshelf -->
    <clipPath id="term-torch-clip">
      <g class="torch-beam">
        <circle cx="0" cy="0" r="110" fill="#ffffff" />
      </g>
    </clipPath>

    <!-- Soft radial glow for torch light beam -->
    <radialGradient id="term-torch-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="rgba(255, 255, 230, 0.28)" />
      <stop offset="60%" stop-color="rgba(57, 211, 83, 0.15)" />
      <stop offset="100%" stop-color="rgba(0, 0, 0, 0)" />
    </radialGradient>
  </defs>

  <!-- Main Terminal Window Container -->
  <rect x="0" y="0" width="{vbox_w}" height="{total_svg_h}" rx="8" fill="#0d1117" stroke="rgba(57,211,83,0.3)" stroke-width="1.5" />

  <!-- Terminal Top Bar -->
  <path d="M0 8a8 8 0 0 1 8-8h{vbox_w-16}a8 8 0 0 1 8 8v22H0Z" fill="#161b22" />
  <line x1="0" y1="30" x2="{vbox_w}" y2="30" stroke="rgba(57,211,83,0.2)" stroke-width="1" />

  <!-- Window Dots -->
  <circle cx="20" cy="15" r="5.5" fill="#ff5f56" stroke="#e0443e" stroke-width="0.5" />
  <circle cx="36" cy="15" r="5.5" fill="#ffbd2e" stroke="#dea123" stroke-width="0.5" />
  <circle cx="52" cy="15" r="5.5" fill="#27c93f" stroke="#1aab29" stroke-width="0.5" />

  <!-- Terminal Header Title -->
  <text x="{vbox_w // 2}" y="19" text-anchor="middle" class="t-win-title">Terminal Profile: @Arnim-Zola ~ zsh</text>

  <!-- Terminal Profile Body (Text Fields) -->
{text_content}

  <!-- Section Divider with HUD label -->
  <line x1="24" y1="{shelf_top - 8}" x2="{vbox_w - 24}" y2="{shelf_top - 8}" stroke="rgba(57,211,83,0.2)" stroke-width="1" stroke-dasharray="4 4" />
  <text x="24" y="{shelf_top - 14}" class="t-sub-title">MIDNIGHT ARCHIVES &amp; RESEARCH VAULT // FL_SCAN_ACTIVE</text>

  <!-- Bookshelf Section inside Terminal -->
  <g transform="translate({shelf_x}, {shelf_top})">
    <!-- Bookshelf Frame -->
    <rect x="0" y="0" width="{shelf_w}" height="{shelf_h}" rx="6" fill="#090d13" stroke="rgba(57,211,83,0.2)" stroke-width="1" />

    <!-- Shelves Base Planks -->
    <rect x="4" y="60" width="{shelf_w - 8}" height="6" rx="1" fill="#161b22" stroke="#30363d" stroke-width="1" />
    <rect x="4" y="122" width="{shelf_w - 8}" height="6" rx="1" fill="#161b22" stroke="#30363d" stroke-width="1" />

    <!-- Layer 1: Dark Books in Shadow -->
    <g>
      {dark_books_svg}
    </g>

    <!-- Layer 2: Colorful Books Lit by Flashlight -->
    <g clip-path="url(#term-torch-clip)">
      {color_books_svg}
    </g>

    <!-- Moving Ambient Torch Glow Overlay -->
    <g class="torch-beam" pointer-events="none">
      <circle cx="0" cy="0" r="110" fill="url(#term-torch-glow)" />
    </g>

    <!-- Spooky Eyes Hidden on Shelf 2 -->
    <g class="spooky-eye-pair">
      <circle cx="494" cy="92" r="3" fill="#fff" />
      <circle cx="503" cy="92" r="3" fill="#fff" />
    </g>
  </g>
</svg>
"""

    out_path = os.path.join(assets_dir, "terminal-profile-torch.svg")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated: {out_path}")

if __name__ == "__main__":
    generate_terminal_svg()
