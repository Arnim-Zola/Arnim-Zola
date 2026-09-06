import os

def generate_divider_svg():
    assets_dir = r"c:\Holidays\Arnim-Zola\assets"
    
    # 1. Sleek Cyber Glow Green Divider
    svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 16" fill="none" width="100%" height="16">
  <defs>
    <linearGradient id="greenBeam" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00ff88" stop-opacity="0" />
      <stop offset="15%" stop-color="#00ff88" stop-opacity="0.2" />
      <stop offset="50%" stop-color="#00ff88" stop-opacity="1" />
      <stop offset="85%" stop-color="#00ff88" stop-opacity="0.2" />
      <stop offset="100%" stop-color="#00ff88" stop-opacity="0" />
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <!-- Ambient Glow Line -->
  <line x1="20" y1="8" x2="1180" y2="8" stroke="url(#greenBeam)" stroke-width="3" filter="url(#glow)" stroke-linecap="round" />
  
  <!-- Core Crisp Sharp Laser Line -->
  <line x1="40" y1="8" x2="1160" y2="8" stroke="url(#greenBeam)" stroke-width="1.2" stroke-linecap="round" />
  
  <!-- Center Cyber Tech Node -->
  <circle cx="600" cy="8" r="3" fill="#00ff88" filter="url(#glow)" />
  <circle cx="600" cy="8" r="1.5" fill="#ffffff" />
  <polygon points="575,8 580,5 585,8 580,11" fill="#00ff88" opacity="0.6" />
  <polygon points="625,8 620,5 615,8 620,11" fill="#00ff88" opacity="0.6" />
</svg>'''

    output_path = os.path.join(assets_dir, "green-divider.svg")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated {output_path}")

    # 2. Minimalist Clean Green Line (2px)
    minimal_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 4" fill="none" width="100%" height="4">
  <defs>
    <linearGradient id="minGreen" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#238636" stop-opacity="0" />
      <stop offset="20%" stop-color="#238636" stop-opacity="0.8" />
      <stop offset="50%" stop-color="#39d353" stop-opacity="1" />
      <stop offset="80%" stop-color="#238636" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#238636" stop-opacity="0" />
    </linearGradient>
  </defs>
  <line x1="0" y1="2" x2="1200" y2="2" stroke="url(#minGreen)" stroke-width="2" stroke-linecap="round" />
</svg>'''
    min_output_path = os.path.join(assets_dir, "green-divider-minimal.svg")
    with open(min_output_path, "w", encoding="utf-8") as f:
        f.write(minimal_svg)
    print(f"Generated {min_output_path}")

if __name__ == "__main__":
    generate_divider_svg()
