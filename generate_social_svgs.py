import os

def create_social_svgs():
    assets_dir = r"c:\Holidays\Arnim-Zola\assets"
    os.makedirs(assets_dir, exist_ok=True)

    # LinkedIn SVG Button with Automatic Dynamic Looping Hover Animation
    linkedin_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 170 42" width="170" height="42">
  <defs>
    <linearGradient id="bgGradIn" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#238636"/>
      <stop offset="100%" stop-color="#144d20"/>
    </linearGradient>
    <clipPath id="pillClipIn">
      <rect x="2" y="2" width="166" height="38" rx="19" ry="19"/>
    </clipPath>
  </defs>

  <style>
    .btn-pill {
      fill: url(#bgGradIn);
      stroke: #39d353;
      stroke-width: 1.75;
      rx: 19;
      ry: 19;
      animation: borderPulseIn 6s ease-in-out infinite;
    }
    .btn-text {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Space Grotesk", Roboto, sans-serif;
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 1.5px;
      fill: #ffffff;
      text-shadow: 1px 1px 2px rgba(0,0,0,0.8);
      text-anchor: middle;
      dominant-baseline: central;
    }
    .text-play {
      animation: textSlide1 6s cubic-bezier(0.2, 0.8, 0.25, 1) infinite;
    }
    .text-now {
      animation: textSlide2 6s cubic-bezier(0.2, 0.8, 0.25, 1) infinite;
    }
    .icon-wrap {
      transform-origin: 26px 21px;
      animation: iconMorphIn 6s cubic-bezier(0.2, 0.8, 0.25, 1) infinite;
    }
    .shimmer {
      opacity: 0.15;
      animation: sweepIn 6s ease-in-out infinite;
    }

    @keyframes textSlide1 {
      0%, 42% { opacity: 1; transform: translateX(0); }
      48%, 92% { opacity: 0; transform: translateX(50px); }
      98%, 100% { opacity: 1; transform: translateX(0); }
    }
    @keyframes textSlide2 {
      0%, 42% { opacity: 0; transform: translateX(-50px); }
      48%, 92% { opacity: 1; transform: translateX(0); }
      98%, 100% { opacity: 0; transform: translateX(50px); }
    }
    @keyframes iconMorphIn {
      0%, 42% { transform: scale(1); opacity: 1; }
      48%, 92% { transform: scale(2.6) translate(18px, 0); opacity: 0.18; }
      98%, 100% { transform: scale(1); opacity: 1; }
    }
    @keyframes borderPulseIn {
      0%, 42% { stroke: #39d353; }
      48%, 92% { stroke: #00ff66; }
      98%, 100% { stroke: #39d353; }
    }
    @keyframes sweepIn {
      0%, 42% { opacity: 0.1; transform: translateX(-30px); }
      48%, 92% { opacity: 0.35; transform: translateX(30px); }
      98%, 100% { opacity: 0.1; transform: translateX(-30px); }
    }
  </style>

  <!-- Button Background -->
  <rect x="2" y="2" width="166" height="38" class="btn-pill"/>

  <!-- Clipped Area for Dynamic Content -->
  <g clip-path="url(#pillClipIn)">
    <!-- Light Shimmer Sweep -->
    <ellipse cx="85" cy="21" rx="60" ry="14" fill="#00ff66" class="shimmer"/>

    <!-- Morphing LinkedIn Icon -->
    <g class="icon-wrap" transform="translate(18, 12.5)">
      <path fill="#ffffff" d="M14.25 0H1.75C0.78 0 0 0.78 0 1.75V14.25C0 15.22 0.78 16 1.75 16H14.25C15.22 16 16 15.22 16 14.25V1.75C16 0.78 15.22 0 14.25 0ZM4.75 13.5H2.375V5.875H4.75V13.5ZM3.56 4.83C2.8 4.83 2.18 4.21 2.18 3.44C2.18 2.68 2.8 2.06 3.56 2.06C4.33 2.06 4.95 2.68 4.95 3.44C4.95 4.21 4.33 4.83 3.56 4.83ZM13.625 13.5H11.25V9.75C11.25 8.85 10.45 8.1 9.55 8.1C8.65 8.1 7.875 8.85 7.875 9.75V13.5H5.5V5.875H7.875V6.85C8.38 6.05 9.4 5.65 10.35 5.65C12.15 5.65 13.625 7.12 13.625 8.92V13.5Z"/>
    </g>

    <!-- Alternating Text Layers -->
    <text x="98" y="21.5" class="btn-text text-play">LINKEDIN</text>
    <text x="85" y="21.5" class="btn-text text-now">CONNECT</text>
  </g>
</svg>
"""

    # Email SVG Button with Automatic Dynamic Looping Hover Animation
    email_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 170 42" width="170" height="42">
  <defs>
    <linearGradient id="bgGradMail" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#238636"/>
      <stop offset="100%" stop-color="#144d20"/>
    </linearGradient>
    <clipPath id="pillClipMail">
      <rect x="2" y="2" width="166" height="38" rx="19" ry="19"/>
    </clipPath>
  </defs>

  <style>
    .btn-pill {
      fill: url(#bgGradMail);
      stroke: #39d353;
      stroke-width: 1.75;
      rx: 19;
      ry: 19;
      animation: borderPulseMail 6s ease-in-out infinite;
    }
    .btn-text {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Space Grotesk", Roboto, sans-serif;
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 1.5px;
      fill: #ffffff;
      text-shadow: 1px 1px 2px rgba(0,0,0,0.8);
      text-anchor: middle;
      dominant-baseline: central;
    }
    .text-play {
      animation: textSlide1 6s cubic-bezier(0.2, 0.8, 0.25, 1) infinite;
    }
    .text-now {
      animation: textSlide2 6s cubic-bezier(0.2, 0.8, 0.25, 1) infinite;
    }
    .icon-wrap {
      transform-origin: 26px 21px;
      animation: iconMorphMail 6s cubic-bezier(0.2, 0.8, 0.25, 1) infinite;
    }
    .shimmer {
      opacity: 0.15;
      animation: sweepMail 6s ease-in-out infinite;
    }

    @keyframes textSlide1 {
      0%, 42% { opacity: 1; transform: translateX(0); }
      48%, 92% { opacity: 0; transform: translateX(50px); }
      98%, 100% { opacity: 1; transform: translateX(0); }
    }
    @keyframes textSlide2 {
      0%, 42% { opacity: 0; transform: translateX(-50px); }
      48%, 92% { opacity: 1; transform: translateX(0); }
      98%, 100% { opacity: 0; transform: translateX(50px); }
    }
    @keyframes iconMorphMail {
      0%, 42% { transform: scale(1); opacity: 1; }
      48%, 92% { transform: scale(2.6) translate(18px, 0); opacity: 0.18; }
      98%, 100% { transform: scale(1); opacity: 1; }
    }
    @keyframes borderPulseMail {
      0%, 42% { stroke: #39d353; }
      48%, 92% { stroke: #00ff66; }
      98%, 100% { stroke: #39d353; }
    }
    @keyframes sweepMail {
      0%, 42% { opacity: 0.1; transform: translateX(-30px); }
      48%, 92% { opacity: 0.35; transform: translateX(30px); }
      98%, 100% { opacity: 0.1; transform: translateX(-30px); }
    }
  </style>

  <!-- Button Background -->
  <rect x="2" y="2" width="166" height="38" class="btn-pill"/>

  <!-- Clipped Area for Dynamic Content -->
  <g clip-path="url(#pillClipMail)">
    <!-- Light Shimmer Sweep -->
    <ellipse cx="85" cy="21" rx="60" ry="14" fill="#00ff66" class="shimmer"/>

    <!-- Morphing Mail Icon -->
    <g class="icon-wrap" transform="translate(20, 13)">
      <path fill="#ffffff" d="M16 3.638V12.91C16 13.513 15.513 14 14.91 14H12.363V7.82L8 11.093L3.636 7.82V14H1.09C0.487 14 0 13.513 0 12.91V3.638C0 2.29 1.54 1.52 2.618 2.329L3.636 3.093L8 6.365L12.364 3.093L13.382 2.33C14.46 1.52 16 2.29 16 3.638Z"/>
    </g>

    <!-- Alternating Text Layers -->
    <text x="96" y="21.5" class="btn-text text-play">EMAIL</text>
    <text x="85" y="21.5" class="btn-text text-now">SEND MAIL</text>
  </g>
</svg>
"""

    with open(os.path.join(assets_dir, "btn-linkedin.svg"), "w", encoding="utf-8") as f:
        f.write(linkedin_svg)

    with open(os.path.join(assets_dir, "btn-email.svg"), "w", encoding="utf-8") as f:
        f.write(email_svg)

    print("Created animated btn-linkedin.svg and btn-email.svg successfully!")

if __name__ == "__main__":
    create_social_svgs()
