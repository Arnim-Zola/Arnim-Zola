import os

def create_social_svgs():
    assets_dir = r"c:\Holidays\Arnim-Zola\assets"
    os.makedirs(assets_dir, exist_ok=True)

    # LinkedIn SVG Button
    linkedin_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 170 42" width="170" height="42">
  <defs>
    <linearGradient id="bgGradIn" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#238636"/>
      <stop offset="100%" stop-color="#1a6328"/>
    </linearGradient>
    <linearGradient id="borderGradIn" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#39d353">
        <animate attributeName="stop-color" values="#39d353;#00ff66;#39d353" dur="3s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="#00ff66">
        <animate attributeName="stop-color" values="#00ff66;#39d353;#00ff66" dur="3s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>
    <filter id="btnGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <style>
    .btn-pill {
      fill: url(#bgGradIn);
      stroke: url(#borderGradIn);
      stroke-width: 1.5;
      rx: 21;
      ry: 21;
    }
    .btn-text {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Space Grotesk", Roboto, sans-serif;
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 1.5px;
      fill: #ffffff;
      text-anchor: middle;
      dominant-baseline: central;
    }
    .btn-icon {
      fill: #ffffff;
    }
    .shimmer {
      opacity: 0.12;
      animation: sweep 4s ease-in-out infinite;
    }
    @keyframes sweep {
      0%, 100% { opacity: 0.08; transform: translateX(-50px); }
      50% { opacity: 0.25; transform: translateX(50px); }
    }
  </style>

  <!-- Button Pill Background -->
  <rect x="2" y="2" width="166" height="38" class="btn-pill"/>
  
  <!-- Subtle Internal Glow Shimmer -->
  <ellipse cx="85" cy="21" rx="60" ry="14" fill="#39d353" class="shimmer"/>

  <!-- Content Group: Icon + Text -->
  <g transform="translate(18, 12)">
    <!-- LinkedIn Icon (18x18) -->
    <path class="btn-icon" d="M14.25 0H1.75C0.78 0 0 0.78 0 1.75V14.25C0 15.22 0.78 16 1.75 16H14.25C15.22 16 16 15.22 16 14.25V1.75C16 0.78 15.22 0 14.25 0ZM4.75 13.5H2.375V5.875H4.75V13.5ZM3.56 4.83C2.8 4.83 2.18 4.21 2.18 3.44C2.18 2.68 2.8 2.06 3.56 2.06C4.33 2.06 4.95 2.68 4.95 3.44C4.95 4.21 4.33 4.83 3.56 4.83ZM13.625 13.5H11.25V9.75C11.25 8.85 10.45 8.1 9.55 8.1C8.65 8.1 7.875 8.85 7.875 9.75V13.5H5.5V5.875H7.875V6.85C8.38 6.05 9.4 5.65 10.35 5.65C12.15 5.65 13.625 7.12 13.625 8.92V13.5Z"/>
  </g>

  <!-- Text -->
  <text x="96" y="22" class="btn-text">LINKEDIN</text>
</svg>
"""

    # Email SVG Button
    email_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 170 42" width="170" height="42">
  <defs>
    <linearGradient id="bgGradMail" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#238636"/>
      <stop offset="100%" stop-color="#1a6328"/>
    </linearGradient>
    <linearGradient id="borderGradMail" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#39d353">
        <animate attributeName="stop-color" values="#39d353;#00ff66;#39d353" dur="3s repeatCount="indefinite""/>
      </stop>
      <stop offset="100%" stop-color="#00ff66">
        <animate attributeName="stop-color" values="#00ff66;#39d353;#00ff66" dur="3s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>
  </defs>

  <style>
    .btn-pill {
      fill: url(#bgGradMail);
      stroke: url(#borderGradMail);
      stroke-width: 1.5;
      rx: 21;
      ry: 21;
    }
    .btn-text {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Space Grotesk", Roboto, sans-serif;
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 1.5px;
      fill: #ffffff;
      text-anchor: middle;
      dominant-baseline: central;
    }
    .btn-icon {
      fill: #ffffff;
    }
    .shimmer {
      opacity: 0.12;
      animation: sweep 4s ease-in-out infinite;
    }
    @keyframes sweep {
      0%, 100% { opacity: 0.08; transform: translateX(-50px); }
      50% { opacity: 0.25; transform: translateX(50px); }
    }
  </style>

  <!-- Button Pill Background -->
  <rect x="2" y="2" width="166" height="38" class="btn-pill"/>

  <!-- Subtle Internal Glow Shimmer -->
  <ellipse cx="85" cy="21" rx="60" ry="14" fill="#39d353" class="shimmer"/>

  <!-- Content Group: Icon + Text -->
  <g transform="translate(24, 13)">
    <!-- Email Envelope Icon (16x16) -->
    <path class="btn-icon" d="M16 3.638V12.91C16 13.513 15.513 14 14.91 14H12.363V7.82L8 11.093L3.636 7.82V14H1.09C0.487 14 0 13.513 0 12.91V3.638C0 2.29 1.54 1.52 2.618 2.329L3.636 3.093L8 6.365L12.364 3.093L13.382 2.33C14.46 1.52 16 2.29 16 3.638Z"/>
  </g>

  <!-- Text -->
  <text x="96" y="22" class="btn-text">EMAIL</text>
</svg>
"""

    with open(os.path.join(assets_dir, "btn-linkedin.svg"), "w", encoding="utf-8") as f:
        f.write(linkedin_svg)

    with open(os.path.join(assets_dir, "btn-email.svg"), "w", encoding="utf-8") as f:
        f.write(email_svg)

    print("Created btn-linkedin.svg and btn-email.svg successfully!")

if __name__ == "__main__":
    create_social_svgs()
