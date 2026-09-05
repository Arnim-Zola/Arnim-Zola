import os
import random

def generate_bookshelf_svg():
    assets_dir = r"c:\Holidays\Arnim-Zola\assets"
    
    # 900x180 2-tier bookshelf
    width = 900
    height = 180
    
    # Color palette from Uiverse.io by Cobp + cyberpunk emerald accents
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

    # Generate books for Shelf 1 (y: 10 to 85) and Shelf 2 (y: 95 to 170)
    random.seed(42) # deterministic
    
    def make_shelf_books(shelf_y, shelf_h):
        books = []
        cur_x = 15
        while cur_x < width - 25:
            b_w = random.randint(12, 26)
            b_h = random.randint(int(shelf_h * 0.7), shelf_h - 4)
            b_y = shelf_y + (shelf_h - b_h)
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
            cur_x += b_w + random.choice([2, 3, 4, 6])
        return books

    shelf1_books = make_shelf_books(10, 75)
    shelf2_books = make_shelf_books(95, 75)
    all_books = shelf1_books + shelf2_books

    # Build dark layer
    dark_rects = []
    for b in all_books:
        dark_rects.append(f'<rect x="{b["x"]}" y="{b["y"]}" width="{b["w"]}" height="{b["h"]}" rx="{b["rx"]}" fill="{b["dark"]}" stroke="#0d1117" stroke-width="1"/>')
        if b["w"] > 16:
            dark_rects.append(f'<line x1="{b["x"]+4}" y1="{b["y"]+6}" x2="{b["x"]+b["w"]-4}" y2="{b["y"]+6}" stroke="#30363d" stroke-width="1"/>')

    # Build color layer (revealed by torch)
    color_rects = []
    for b in all_books:
        color_rects.append(f'<rect x="{b["x"]}" y="{b["y"]}" width="{b["w"]}" height="{b["h"]}" rx="{b["rx"]}" fill="{b["color"]}" stroke="rgba(0,0,0,0.4)" stroke-width="1"/>')
        if b["w"] > 16:
            color_rects.append(f'<line x1="{b["x"]+4}" y1="{b["y"]+8}" x2="{b["x"]+b["w"]-4}" y2="{b["y"]+8}" stroke="rgba(255,255,255,0.4)" stroke-width="1.5"/>')
            color_rects.append(f'<line x1="{b["x"]+4}" y1="{b["y"]+12}" x2="{b["x"]+b["w"]-4}" y2="{b["y"]+12}" stroke="rgba(255,255,255,0.2)" stroke-width="1"/>')

    dark_books_svg = "\n    ".join(dark_rects)
    color_books_svg = "\n    ".join(color_rects)

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="{height}" fill="none">
  <defs>
    <style>
      @keyframes flashlight {{
        0% {{ transform: translate(-150px, 40px); }}
        35% {{ transform: translate(500px, 30px); }}
        39% {{ transform: translate(540px, 120px); opacity: 1; }}
        40% {{ transform: translate(540px, 120px); opacity: 0; }}
        41% {{ transform: translate(540px, 120px); opacity: 1; }}
        42% {{ transform: translate(540px, 120px); opacity: 0; }}
        54% {{ transform: translate(540px, 120px); opacity: 0; }}
        55% {{ transform: translate(540px, 120px); opacity: 1; }}
        59% {{ transform: translate(540px, 120px); opacity: 1; }}
        64% {{ transform: translate(360px, 110px); }}
        68% {{ transform: translate(720px, 125px); }}
        72% {{ transform: translate(540px, 120px); }}
        75% {{ transform: translate(540px, 120px); }}
        100% {{ transform: translate(1050px, 60px); }}
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
        transform-origin: 549px 125px;
        animation: eyes-glow 20s infinite;
      }}
    </style>

    <!-- ClipPath for the moving flashlight -->
    <clipPath id="torch-clip">
      <g class="torch-beam">
        <circle cx="0" cy="0" r="140" fill="#ffffff" />
      </g>
    </clipPath>

    <!-- Soft radial glow for torch light beam -->
    <radialGradient id="torch-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="rgba(255, 255, 230, 0.25)" />
      <stop offset="60%" stop-color="rgba(57, 211, 83, 0.12)" />
      <stop offset="100%" stop-color="rgba(0, 0, 0, 0)" />
    </radialGradient>
  </defs>

  <!-- Bookshelf Background / Wall -->
  <rect width="{width}" height="{height}" rx="8" fill="#0d1117" stroke="rgba(57,211,83,0.25)" stroke-width="1.5" />

  <!-- Shelf 1 & 2 Base Planks -->
  <rect x="8" y="85" width="{width-16}" height="8" rx="2" fill="#161b22" stroke="#30363d" stroke-width="1" />
  <rect x="8" y="170" width="{width-16}" height="8" rx="2" fill="#161b22" stroke="#30363d" stroke-width="1" />

  <!-- Layer 1: Dark Bookshelf in Shadow -->
  <g>
    {dark_books_svg}
  </g>

  <!-- Layer 2: Colorful Books Lit by Flashlight -->
  <g clip-path="url(#torch-clip)">
    {color_books_svg}
  </g>

  <!-- Moving Ambient Torch Glow Overlay -->
  <g class="torch-beam" pointer-events="none">
    <circle cx="0" cy="0" r="140" fill="url(#torch-glow)" />
  </g>

  <!-- Spooky Eyes Hidden between Books on Shelf 2 -->
  <g class="spooky-eye-pair">
    <circle cx="544" cy="125" r="3.5" fill="#fff" />
    <circle cx="554" cy="125" r="3.5" fill="#fff" />
  </g>
</svg>
"""

    out_path = os.path.join(assets_dir, "bookshelf-torch.svg")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated: {out_path}")

if __name__ == "__main__":
    generate_bookshelf_svg()
