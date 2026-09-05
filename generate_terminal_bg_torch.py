import os
import random
import re

def generate_terminal_bookshelf_bg_svg():
    assets_dir = r"c:\Holidays\Arnim-Zola\assets"
    
    # Read font from taglines.svg
    taglines_path = os.path.join(assets_dir, "taglines.svg")
    with open(taglines_path, "r", encoding="utf-8") as f:
        taglines_content = f.read()

    font_match = re.search(r"@font-face\s*\{[^}]*\}", taglines_content, re.DOTALL)
    font_face_css = font_match.group(0) if font_match else ""

    # Dimensions
    vbox_w = 920
    vbox_h = 240
    
    # Generate background books across full height (2 tiers: tier 1 y:10-115, tier 2 y:125-230)
    # Emerald & Cyberpunk Color palette
    colors = [
        "#00ff66", "#39d353", "#238636", "#2ea043", "#1f6feb",
        "#38bdf8", "#008080", "#00b4d8", "#2dd4bf", "#10b981",
        "#059669", "#556b2f", "#4ade80", "#a3e635", "#34d399",
        "#0284c7", "#0d9488", "#16a34a", "#22c55e", "#065f46"
    ]
    
    dark_colors = [
        "#0a0f0d", "#0d1410", "#0f1a14", "#08100b", "#050a07",
        "#071209", "#0b1710", "#09140c", "#0c1811", "#060e08"
    ]

    random.seed(42)
    def make_shelf_books(shelf_y, shelf_h):
        books = []
        cur_x = 12
        while cur_x < vbox_w - 20:
            b_w = random.randint(14, 28)
            b_h = random.randint(int(shelf_h * 0.65), shelf_h - 4)
            b_y = shelf_y + (shelf_h - b_h)
            c_idx = random.randint(0, len(colors) - 1)
            d_idx = random.randint(0, len(dark_colors) - 1)
            
            # horizontal stack books occasionally
            if random.random() < 0.15 and cur_x < vbox_w - 70:
                stack_w = random.randint(35, 50)
                stack_count = random.randint(2, 4)
                for s in range(stack_count):
                    books.append({
                        "x": cur_x,
                        "y": shelf_y + shelf_h - (s + 1) * 11,
                        "w": stack_w,
                        "h": 9,
                        "color": colors[random.randint(0, len(colors) - 1)],
                        "dark": dark_colors[random.randint(0, len(dark_colors) - 1)],
                        "rx": 1
                    })
                cur_x += stack_w + random.choice([3, 4, 6])
            else:
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

    tier1 = make_shelf_books(8, 108)
    tier2 = make_shelf_books(122, 108)
    all_books = tier1 + tier2

    dark_rects = []
    color_rects = []
    for b in all_books:
        dark_rects.append(f'<rect x="{b["x"]}" y="{b["y"]}" width="{b["w"]}" height="{b["h"]}" rx="{b["rx"]}" fill="{b["dark"]}" stroke="#040906" stroke-width="1"/>')
        color_rects.append(f'<rect x="{b["x"]}" y="{b["y"]}" width="{b["w"]}" height="{b["h"]}" rx="{b["rx"]}" fill="{b["color"]}" stroke="rgba(0,0,0,0.5)" stroke-width="1"/>')
        if b["w"] > 16 and b["h"] > 20:
            dark_rects.append(f'<line x1="{b["x"]+4}" y1="{b["y"]+6}" x2="{b["x"]+b["w"]-4}" y2="{b["y"]+6}" stroke="#14261a" stroke-width="1"/>')
            color_rects.append(f'<line x1="{b["x"]+4}" y1="{b["y"]+8}" x2="{b["x"]+b["w"]-4}" y2="{b["y"]+8}" stroke="rgba(255,255,255,0.6)" stroke-width="1.5"/>')
            color_rects.append(f'<line x1="{b["x"]+4}" y1="{b["y"]+13}" x2="{b["x"]+b["w"]-4}" y2="{b["y"]+13}" stroke="rgba(255,255,255,0.3)" stroke-width="1"/>')

    dark_books_svg = "\n    ".join(dark_rects)
    color_books_svg = "\n    ".join(color_rects)

    # Terminal text rows
    term_lines = [
        ("Engineer:", '"Mohammed Sahil (@Arnim-Zola)"'),
        ("Institution:", '"3rd Year B.E. Computer Science &amp; Engineering @ DSATM (Class of 2028)"'),
        ("Location:", '"Bengaluru, Karnataka, India"'),
        ("Target Roles:", '"Full-Stack AI Developer / GenAI Engineer • SDE"'),
        ("Core Pillars:", '"DSA • OS &amp; Systems • DBMS • Computer Networks • OOP"'),
        ("Daily Drivers:", '"FastAPI, pgvector, OpenCV, Whisper RAG, Next.js 15, Docker"'),
        ("Active Pursuits:", '"Competitive Hackathons, Research Papers, Problem Solving &amp; Full-Stack Projects"')
    ]

    text_start_y = 56
    text_line_h = 25
    text_svg_list = []
    
    for i, (k, v) in enumerate(term_lines):
        y = text_start_y + i * text_line_h
        text_svg_list.append(f"""    <text x="28" y="{y}" class="t-line">
      <tspan class="t-key">{k:<16}</tspan> <tspan class="t-val">{v}</tspan>
    </text>""")

    text_content = "\n".join(text_svg_list)

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vbox_w} {vbox_h}" width="100%" height="{vbox_h}" fill="none">
  <defs>
    <style>
      {font_face_css}

      .t-title {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 16px;
        font-weight: 700;
        letter-spacing: 0.5px;
        fill: #00ff66;
        filter: drop-shadow(0 2px 4px rgba(0,0,0,0.95));
      }}
      .t-line {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 14.5px;
        font-weight: 400;
        letter-spacing: 0.3px;
        filter: drop-shadow(0 2px 5px rgba(0,0,0,0.95)) drop-shadow(0 1px 2px rgba(0,0,0,1));
      }}
      .t-key {{
        fill: #00ff66;
        font-weight: 700;
      }}
      .t-val {{
        fill: #ffffff;
        font-weight: 400;
      }}

      @keyframes bg-flashlight {{
        0% {{ transform: translate(-100px, 30px); }}
        35% {{ transform: translate(520px, 40px); }}
        39% {{ transform: translate(560px, 120px); opacity: 1; }}
        40% {{ transform: translate(560px, 120px); opacity: 0.2; }}
        41% {{ transform: translate(560px, 120px); opacity: 1; }}
        42% {{ transform: translate(560px, 120px); opacity: 0.2; }}
        54% {{ transform: translate(560px, 120px); opacity: 0.2; }}
        55% {{ transform: translate(560px, 120px); opacity: 1; }}
        59% {{ transform: translate(560px, 120px); opacity: 1; }}
        64% {{ transform: translate(320px, 80px); }}
        68% {{ transform: translate(720px, 130px); }}
        72% {{ transform: translate(560px, 120px); }}
        75% {{ transform: translate(560px, 120px); }}
        100% {{ transform: translate(1050px, 60px); }}
      }}

      @keyframes bg-eyes {{
        0%, 38% {{ opacity: 0; transform: scaleY(0); }}
        39%, 40.5% {{ opacity: 1; transform: scaleY(1); fill: #ffffff; filter: drop-shadow(0 0 5px #ffffff); }}
        41% {{ opacity: 0; transform: scaleY(0); }}
        41.5%, 43% {{ opacity: 1; transform: scaleY(1); fill: #ff0033; filter: drop-shadow(0 0 8px #ff0033); }}
        43.5%, 100% {{ opacity: 0; transform: scaleY(0); }}
      }}

      .bg-torch-beam {{
        animation: bg-flashlight 20s ease-in-out infinite;
      }}

      .bg-spooky-eyes {{
        transform-origin: 569px 92px;
        animation: bg-eyes 20s infinite;
      }}
    </style>

    <!-- ClipPath for sharp cartoon flashlight cutout -->
    <clipPath id="shelf-torch-clip">
      <g class="bg-torch-beam">
        <circle cx="0" cy="0" r="130" fill="#ffffff" />
      </g>
    </clipPath>
  </defs>

  <!-- Container Box -->
  <rect x="0" y="0" width="{vbox_w}" height="{vbox_h}" rx="10" fill="#040906" stroke="rgba(0,255,102,0.4)" stroke-width="1.5" />

  <!-- Shelves Structure -->
  <rect x="6" y="115" width="{vbox_w - 12}" height="6" rx="1" fill="#0a140e" stroke="#14261a" stroke-width="1" />
  <rect x="6" y="230" width="{vbox_w - 12}" height="6" rx="1" fill="#0a140e" stroke="#14261a" stroke-width="1" />

  <!-- Layer 1: Flat Dark Silhouetted Bookshelf in Shadow -->
  <g>
    {dark_books_svg}
  </g>

  <!-- Layer 2: 100% Vivid Flat Cartoon Books Revealed by Torch -->
  <g clip-path="url(#shelf-torch-clip)">
    {color_books_svg}
  </g>

  <!-- Sharp Cartoon Flashlight Circular Rim Outline -->
  <g class="bg-torch-beam" pointer-events="none">
    <circle cx="0" cy="0" r="130" fill="none" stroke="#00ff66" stroke-width="1.5" opacity="0.6" />
  </g>

  <!-- Spooky Eyes Hidden between Books -->
  <g class="bg-spooky-eyes">
    <circle cx="564" cy="92" r="3.5" fill="#fff" />
    <circle cx="574" cy="92" r="3.5" fill="#fff" />
  </g>

  <!-- Header Title -->
  <text x="28" y="28" class="t-title">Terminal Profile:</text>

  <!-- Terminal Text Floating Directly Over the Bookshelf -->
  <g>
{text_content}
  </g>
</svg>
"""

    for fname in ["terminal-profile-bg-torch.svg", "terminal-profile-v3.svg", "terminal-profile-cartoon.svg"]:
        out_path = os.path.join(assets_dir, fname)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(svg_content)
        print(f"Generated: {out_path}")

if __name__ == "__main__":
    generate_terminal_bookshelf_bg_svg()
