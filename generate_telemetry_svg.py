import os
import re
import xml.etree.ElementTree as ET

def generate_telemetry_svg():
    assets_dir = r"c:\Holidays\Arnim-Zola\assets"

    # Read base64 font from taglines.svg
    taglines_path = os.path.join(assets_dir, "taglines.svg")
    with open(taglines_path, "r", encoding="utf-8") as f:
        taglines_content = f.read()

    font_match = re.search(r"@font-face\s*\{[^}]*\}", taglines_content, re.DOTALL)
    font_face_css = font_match.group(0) if font_match else ""

    vbox_w = 920
    vbox_h = 550

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vbox_w} {vbox_h}" width="100%" height="{vbox_h}" fill="none">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700;800&amp;family=Space+Grotesk:wght@600;700;800&amp;family=Caacupe+One&amp;display=swap');
      {font_face_css}

      .card-title {{
        font-family: 'Space Grotesk', 'Caacupe One', -apple-system, sans-serif;
        font-size: 15px;
        font-weight: 700;
        letter-spacing: 0.5px;
        fill: #ffffff;
      }}
      .card-title-green {{
        font-family: 'Space Grotesk', 'Caacupe One', -apple-system, sans-serif;
        font-size: 15px;
        font-weight: 700;
        letter-spacing: 0.5px;
        fill: #7ee787;
      }}
      .telemetry-title {{
        font-family: 'Space Grotesk', -apple-system, sans-serif;
        font-size: 11.5px;
        font-weight: 700;
        letter-spacing: 1.5px;
        fill: #7ee787;
      }}
      .streak-val {{
        font-family: 'Space Grotesk', -apple-system, sans-serif;
        font-size: 28px;
        font-weight: 800;
        fill: #ffffff;
        text-anchor: middle;
      }}
      .streak-lbl {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 0.5px;
        fill: #8b949e;
        text-anchor: middle;
        text-transform: uppercase;
      }}
      .streak-sub {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 9px;
        fill: #6e7681;
        text-anchor: middle;
      }}
      .stat-lbl {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 12px;
        font-weight: 500;
        fill: #8b949e;
      }}
      .stat-num {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 12px;
        font-weight: 700;
        fill: #00ff66;
        text-anchor: end;
      }}
      .lang-name {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 12px;
        font-weight: 600;
        fill: #e6edf3;
      }}
      .lang-pct {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 12px;
        font-weight: 600;
        fill: #8b949e;
        text-anchor: end;
      }}
    </style>

    <!-- Celestial Nocturnal Emerald Sky Gradient -->
    <linearGradient id="skyMasterGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#020d06" />
      <stop offset="18%" stop-color="#041c0d" />
      <stop offset="38%" stop-color="#083218" />
      <stop offset="62%" stop-color="#0f4e26" />
      <stop offset="82%" stop-color="#186935" />
      <stop offset="100%" stop-color="#268d4a" />
    </linearGradient>

    <!-- Moon Atmospheric Radial Glow -->
    <radialGradient id="moonRadialHaze" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#a7f3d0" stop-opacity="0.36" />
      <stop offset="30%" stop-color="#34d399" stop-opacity="0.22" />
      <stop offset="65%" stop-color="#059669" stop-opacity="0.08" />
      <stop offset="100%" stop-color="#020d06" stop-opacity="0" />
    </radialGradient>

    <!-- Celestial Crescent Moon Gradient -->
    <linearGradient id="naturalMoonGrad" x1="100%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#f4fff7" />
      <stop offset="18%" stop-color="#dcfce7" />
      <stop offset="42%" stop-color="#86efac" />
      <stop offset="70%" stop-color="#22c55e" />
      <stop offset="88%" stop-color="#15803d" />
      <stop offset="100%" stop-color="#14532d" />
    </linearGradient>

    <!-- Painterly Volumetric Cloud Gradients -->
    <linearGradient id="cloudGradSoft1" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0e381f" stop-opacity="0.95" />
      <stop offset="52%" stop-color="#1a5631" stop-opacity="0.88" />
      <stop offset="100%" stop-color="#0a2916" stop-opacity="0.6" />
    </linearGradient>
    <linearGradient id="cloudGradSoft2" x1="1" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#124325" stop-opacity="0.95" />
      <stop offset="52%" stop-color="#1e6238" stop-opacity="0.88" />
      <stop offset="100%" stop-color="#0c2f1a" stop-opacity="0.6" />
    </linearGradient>
    <linearGradient id="cloudGradCenter" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#0a2e18" stop-opacity="0.4" />
      <stop offset="35%" stop-color="#226e3e" stop-opacity="0.88" />
      <stop offset="65%" stop-color="#226e3e" stop-opacity="0.88" />
      <stop offset="100%" stop-color="#0a2e18" stop-opacity="0.4" />
    </linearGradient>

    <!-- Cloud Rim Highlight -->
    <linearGradient id="cloudRimLight" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#a7f3d0" stop-opacity="0.85" />
      <stop offset="45%" stop-color="#4ade80" stop-opacity="0.6" />
      <stop offset="100%" stop-color="#10b981" stop-opacity="0.15" />
    </linearGradient>

    <!-- Mountain Ridge Gradients -->
    <linearGradient id="distantRidgeGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#154728" />
      <stop offset="100%" stop-color="#0d321c" />
    </linearGradient>
    <linearGradient id="midRidgeGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#092c17" />
      <stop offset="100%" stop-color="#051c0e" />
    </linearGradient>
    <linearGradient id="foreRidgeGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#03160a" />
      <stop offset="100%" stop-color="#010a04" />
    </linearGradient>

    <!-- Moon Halo Filter -->
    <filter id="moonAura" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="18" />
    </filter>
    <filter id="moonBloom" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="4" result="bloom" />
      <feMerge>
        <feMergeNode in="bloom" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
    <filter id="sparkleGlow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
    <filter id="cardShadow" x="-10%" y="-10%" width="120%" height="130%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#000000" flood-opacity="0.85" />
    </filter>

    <!-- Clip Path for Outer Chamber Rounded Rectangle -->
    <clipPath id="chamberClip">
      <rect x="0" y="0" width="{vbox_w}" height="{vbox_h}" rx="14" />
    </clipPath>
  </defs>

  <!-- ==================== OUTER CHAMBER CONTAINER ==================== -->
  <g clip-path="url(#chamberClip)">
    <!-- 1. Nocturnal Emerald Sky Canvas -->
    <rect width="{vbox_w}" height="{vbox_h}" fill="url(#skyMasterGrad)" />

    <!-- 2. Atmospheric Moonlight Glow (Centered on Moon at x:670, y:95) -->
    <ellipse cx="670" cy="95" rx="240" ry="160" fill="url(#moonRadialHaze)" />

    <!-- 3. Ambient Radiant Moon Bloom -->
    <path d="M 684,51 A 45 45 0 1 1 639,121 A 43 43 0 0 0 684,51 Z" fill="#34d399" opacity="0.48" filter="url(#moonAura)" />

    <!-- 4. Celestial Emerald Crescent Moon -->
    <path d="M 684,51 A 45 45 0 1 1 639,121 A 43 43 0 0 0 684,51 Z" fill="url(#naturalMoonGrad)" filter="url(#moonBloom)" stroke="rgba(244, 255, 247, 0.7)" stroke-width="0.8" />

    <!-- 5. Diamond Sparkle Stars -->
    <g>
      <!-- Sparkle 1 (Top Left) -->
      <path d="M 145,100 Q 145,115 150,115 Q 145,115 145,130 Q 145,115 140,115 Q 145,115 145,100 Z" fill="#d1fae5" filter="url(#sparkleGlow)" />
      <circle cx="145" cy="115" r="2.2" fill="#f0fff4" />
      
      <!-- Sparkle 2 (Mid Sky) -->
      <path d="M 400,120 Q 400,132 404,132 Q 400,132 400,144 Q 400,132 396,132 Q 400,132 400,120 Z" fill="#d1fae5" filter="url(#sparkleGlow)" />
      <circle cx="400" cy="132" r="1.8" fill="#f0fff4" />

      <!-- Sparkle 3 (Near Moon) -->
      <path d="M 550,95 Q 550,105 553,105 Q 550,105 550,115 Q 550,105 547,105 Q 550,105 550,95 Z" fill="#d1fae5" filter="url(#sparkleGlow)" />
      <circle cx="550" cy="105" r="1.8" fill="#f0fff4" />

      <!-- Sparkle 4 (Right) -->
      <path d="M 830,125 Q 830,135 833,135 Q 830,135 830,145 Q 830,135 827,135 Q 830,135 830,125 Z" fill="#a7f3d0" filter="url(#sparkleGlow)" />
      <circle cx="830" cy="135" r="1.8" fill="#f0fff4" />
    </g>

    <!-- 6. Stardust Ambient Dots -->
    <g opacity="0.8">
      <circle cx="210" cy="38" r="1.5" fill="#86efac" />
      <circle cx="310" cy="68" r="1.4" fill="#d1fae5" />
      <circle cx="390" cy="40" r="1.8" fill="#86efac" />
      <circle cx="510" cy="50" r="1.6" fill="#f0fff4" />
      <circle cx="750" cy="85" r="1.6" fill="#86efac" />
      <circle cx="810" cy="130" r="1.4" fill="#d1fae5" />
      <circle cx="680" cy="310" r="1.5" fill="#86efac" />
      <circle cx="440" cy="340" r="1.4" fill="#f0fff4" />
    </g>

    <!-- 7. Painterly Clouds -->
    <g>
      <!-- Cloud Left -->
      <path d="M -40,160 C -15,125 45,120 80,142 C 115,115 178,115 214,142 C 250,128 290,150 304,178 C 270,192 130,196 -40,188 Z" fill="url(#cloudGradSoft1)" opacity="0.85" />
      <path d="M -40,160 C -15,125 45,120 80,142 C 115,115 178,115 214,142 C 250,128 290,150 304,178" fill="none" stroke="url(#cloudRimLight)" stroke-width="2" opacity="0.8" />

      <!-- Cloud Right -->
      <path d="M 600,210 C 610,175 668,160 708,180 C 744,158 808,158 844,180 C 880,166 925,175 960,198 L 960,234 C 930,248 865,248 815,230 C 765,248 700,244 650,226 C 620,230 600,220 600,210 Z" fill="url(#cloudGradSoft2)" opacity="0.85" />
      <path d="M 600,210 C 610,175 668,160 708,180 C 744,158 808,158 844,180 C 880,166 925,175 960,198" fill="none" stroke="url(#cloudRimLight)" stroke-width="2" opacity="0.85" />

      <!-- Horizon Cloud Center -->
      <path d="M 150,440 C 190,405 250,400 290,422 C 335,390 410,385 455,418 C 500,390 575,390 620,418 C 660,400 715,410 750,436 C 778,458 745,480 688,488 C 570,502 270,502 150,440 Z" fill="url(#cloudGradCenter)" opacity="0.82" />
    </g>

    <!-- 8. Distant Misty Rolling Hills -->
    <path d="M -30,470 Q 200,405 480,465 T 950,440 L 950,560 L -30,560 Z" fill="url(#distantRidgeGrad)" />
    <path d="M -30,470 Q 200,405 480,465 T 950,440" fill="none" stroke="rgba(134, 239, 172, 0.22)" stroke-width="1.2" />

    <!-- 9. Mid Rolling Hills -->
    <path d="M -30,500 Q 250,455 500,510 Q 710,470 950,495 L 950,560 L -30,560 Z" fill="url(#midRidgeGrad)" />
    <path d="M -30,500 Q 250,455 500,510 Q 710,470 950,495" fill="none" stroke="rgba(110, 231, 183, 0.16)" stroke-width="1.4" />

    <!-- 10. Foreground Rolling Hills -->
    <path d="M -30,530 Q 300,495 600,545 Q 780,515 950,548 L 950,560 L -30,560 Z" fill="url(#foreRidgeGrad)" />

    <!-- 11. Silhouette Pine Trees (Left & Right) -->
    <!-- Left Tree -->
    <g transform="translate(45, 430) scale(0.6)">
      <rect x="180" y="140" width="12" height="50" fill="#010603" rx="2" />
      <polygon points="186,40 216,145 156,145" fill="#072011" />
      <polygon points="186,20 210,95 162,95" fill="#0b2c18" />
      <polygon points="186,0 204,55 168,55" fill="#0f3c21" />
    </g>
    <!-- Right Trees -->
    <g transform="translate(830, 435) scale(0.55)">
      <rect x="100" y="140" width="10" height="45" fill="#010603" rx="2" />
      <polygon points="105,45 130,140 80,140" fill="#061c0e" />
      <polygon points="105,25 125,95 85,95" fill="#092514" />
      <polygon points="105,10 120,55 90,55" fill="#0c321b" />
    </g>
  </g>

  <!-- Container Outline Border & Inner Glow -->
  <rect x="0" y="0" width="{vbox_w}" height="{vbox_h}" rx="14" fill="none" stroke="#164d27" stroke-width="1.5" />

  <!-- ==================== TOP TELEMETRY BAR ==================== -->
  <g transform="translate(24, 20)">
    <!-- Pulsing Beacon Dot -->
    <circle cx="4" cy="5" r="4" fill="#00ff66" filter="url(#sparkleGlow)" />
    <circle cx="4" cy="5" r="2" fill="#ffffff" />
    <text x="16" y="9" class="telemetry-title">CORE TELEMETRY &#8226; SYNCHRONIZED</text>
    <line x1="0" y1="20" x2="{vbox_w - 48}" y2="20" stroke="#164d27" stroke-width="1" stroke-opacity="0.6" />
  </g>

  <!-- ==================== ROW 1: CARDS (STREAK + OVERALL STATS) ==================== -->
  <!-- 1. STREAK STATS CARD -->
  <g transform="translate(24, 56)" filter="url(#cardShadow)">
    <rect width="422" height="195" rx="12" fill="#040906" stroke="#164d27" stroke-width="1.5" />
    
    <!-- Col 1: Total Contributions -->
    <g transform="translate(70, 48)">
      <text x="0" y="38" class="streak-val">174</text>
      <text x="0" y="68" class="streak-lbl">TOTAL</text>
      <text x="0" y="82" class="streak-lbl">CONTRIBUTIONS</text>
      <text x="0" y="104" class="streak-sub">Jul 7, 2025 &#8211; Present</text>
    </g>

    <!-- Vertical Divider 1 -->
    <line x1="140" y1="24" x2="140" y2="170" stroke="#163d22" stroke-width="1" />

    <!-- Col 2: Current Streak Ring -->
    <g transform="translate(211, 48)">
      <!-- SVG Ring -->
      <circle cx="0" cy="24" r="26" stroke="#163d22" stroke-width="3.5" fill="none" />
      <circle cx="0" cy="24" r="26" stroke="#00ff66" stroke-width="3.5" stroke-dasharray="163" stroke-dashoffset="163" stroke-linecap="round" fill="none" />
      <text x="0" y="32" class="streak-val">0</text>
      
      <text x="0" y="78" class="streak-lbl" fill="#00ff66" style="fill:#00ff66;">CURRENT STREAK</text>
      <text x="0" y="104" class="streak-sub">Sep 5</text>
    </g>

    <!-- Vertical Divider 2 -->
    <line x1="282" y1="24" x2="282" y2="170" stroke="#163d22" stroke-width="1" />

    <!-- Col 3: Longest Streak -->
    <g transform="translate(352, 48)">
      <text x="0" y="38" class="streak-val">3</text>
      <text x="0" y="78" class="streak-lbl">LONGEST STREAK</text>
      <text x="0" y="104" class="streak-sub">Jun 19 &#8211; Jun 21</text>
    </g>
  </g>

  <!-- 2. OVERALL STATS CARD -->
  <g transform="translate(474, 56)" filter="url(#cardShadow)">
    <rect width="422" height="195" rx="12" fill="#040906" stroke="#164d27" stroke-width="1.5" />
    
    <text x="24" y="32" class="card-title">Mohammed Sahil's GitHub Stats</text>

    <!-- Stats Items List -->
    <!-- Item 1: Total Stars -->
    <g transform="translate(24, 62)">
      <!-- Star Icon -->
      <path d="M7 0.5 L8.8 4.2 L13 4.8 L9.9 7.8 L10.6 12 L7 10 L3.4 12 L4.1 7.8 L1 4.8 L5.2 4.2 Z" fill="#00ff66" />
      <text x="24" y="10" class="stat-lbl">Total Stars Earned:</text>
      <text x="374" y="10" class="stat-num">0</text>
    </g>

    <!-- Item 2: Total Commits -->
    <g transform="translate(24, 88)">
      <!-- Clock/Commit Icon -->
      <circle cx="7" cy="7" r="6" stroke="#00ff66" stroke-width="1.5" fill="none" />
      <path d="M7 3.5 L7 7 L9.5 8.5" stroke="#00ff66" stroke-width="1.5" fill="none" stroke-linecap="round" />
      <text x="24" y="11" class="stat-lbl">Total Commits:</text>
      <text x="374" y="11" class="stat-num">114</text>
    </g>

    <!-- Item 3: Total PRs -->
    <g transform="translate(24, 114)">
      <!-- PR Icon -->
      <circle cx="4" cy="3" r="2" fill="#00ff66" />
      <circle cx="4" cy="11" r="2" fill="#00ff66" />
      <circle cx="10" cy="7" r="2" fill="#00ff66" />
      <path d="M4 3 L4 11 M10 7 L10 5 C10 3.5 8 3.5 4 3.5" stroke="#00ff66" stroke-width="1.2" fill="none" />
      <text x="24" y="11" class="stat-lbl">Total PRs:</text>
      <text x="374" y="11" class="stat-num">2</text>
    </g>

    <!-- Item 4: Total Issues -->
    <g transform="translate(24, 140)">
      <!-- Issue Icon -->
      <circle cx="7" cy="7" r="6" stroke="#00ff66" stroke-width="1.5" fill="none" />
      <circle cx="7" cy="7" r="1.5" fill="#00ff66" />
      <text x="24" y="11" class="stat-lbl">Total Issues:</text>
      <text x="374" y="11" class="stat-num">0</text>
    </g>

    <!-- Item 5: Contributed to -->
    <g transform="translate(24, 166)">
      <!-- Repo Icon -->
      <rect x="2" y="2" width="10" height="10" rx="1.5" stroke="#00ff66" stroke-width="1.3" fill="none" />
      <line x1="5" y1="2" x2="5" y2="12" stroke="#00ff66" stroke-width="1" />
      <text x="24" y="11" class="stat-lbl">Contributed to (Last year):</text>
      <text x="374" y="11" class="stat-num">0</text>
    </g>
  </g>

  <!-- ==================== ROW 2: MOST USED LANGUAGES CARD (CENTERED) ==================== -->
  <g transform="translate(195, 275)" filter="url(#cardShadow)">
    <rect width="530" height="245" rx="12" fill="#040906" stroke="#164d27" stroke-width="1.5" />
    
    <text x="26" y="36" class="card-title-green">Most Used Languages</text>

    <!-- Multi-Segment Progress Bar -->
    <g transform="translate(26, 56)">
      <!-- Track Background -->
      <rect width="478" height="10" rx="5" fill="#0e2617" />
      
      <!-- Colored Segments -->
      <!-- JavaScript: 80.33% = 384px -->
      <rect x="0" y="0" width="384" height="10" rx="5" fill="#f1e05a" />
      <!-- Python: 16.74% = 80px -->
      <rect x="385" y="0" width="80" height="10" fill="#3572A5" />
      <!-- CSS: 2.38% = 11.4px -->
      <rect x="466" y="0" width="11" height="10" fill="#663399" />
      <!-- HTML: 0.38% = 1.8px -->
      <rect x="474" y="0" width="2" height="10" fill="#e34c26" />
      <!-- Batchfile: 0.09% -->
      <rect x="476" y="0" width="1" height="10" fill="#C1F12E" />
      <!-- Shell: 0.08% -->
      <rect x="477" y="0" width="1" height="10" rx="5" fill="#89e051" />
    </g>

    <!-- Language Grid Breakdown (2 Columns x 3 Rows) -->
    <!-- Row 1 -->
    <!-- JavaScript -->
    <g transform="translate(26, 96)">
      <circle cx="5" cy="5" r="4.5" fill="#f1e05a" />
      <text x="18" y="9" class="lang-name">JavaScript</text>
      <text x="210" y="9" class="lang-pct">80.33%</text>
    </g>
    <!-- HTML -->
    <g transform="translate(280, 96)">
      <circle cx="5" cy="5" r="4.5" fill="#e34c26" />
      <text x="18" y="9" class="lang-name">HTML</text>
      <text x="210" y="9" class="lang-pct">0.38%</text>
    </g>

    <!-- Row 2 -->
    <!-- Python -->
    <g transform="translate(26, 140)">
      <circle cx="5" cy="5" r="4.5" fill="#3572A5" />
      <text x="18" y="9" class="lang-name">Python</text>
      <text x="210" y="9" class="lang-pct">16.74%</text>
    </g>
    <!-- Batchfile -->
    <g transform="translate(280, 140)">
      <circle cx="5" cy="5" r="4.5" fill="#C1F12E" />
      <text x="18" y="9" class="lang-name">Batchfile</text>
      <text x="210" y="9" class="lang-pct">0.09%</text>
    </g>

    <!-- Row 3 -->
    <!-- CSS -->
    <g transform="translate(26, 184)">
      <circle cx="5" cy="5" r="4.5" fill="#663399" />
      <text x="18" y="9" class="lang-name">CSS</text>
      <text x="210" y="9" class="lang-pct">2.38%</text>
    </g>
    <!-- Shell -->
    <g transform="translate(280, 184)">
      <circle cx="5" cy="5" r="4.5" fill="#89e051" />
      <text x="18" y="9" class="lang-name">Shell</text>
      <text x="210" y="9" class="lang-pct">0.08%</text>
    </g>
  </g>
</svg>"""

    for fname in ["telemetry-cosmos-card.svg", "telemetry-cosmos-card-v1.svg"]:
        out_path = os.path.join(assets_dir, fname)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(svg_content)
    ET.fromstring(svg_content)
    print("Generated & Validated: telemetry-cosmos-card.svg and v1")

if __name__ == "__main__":
    generate_telemetry_svg()
