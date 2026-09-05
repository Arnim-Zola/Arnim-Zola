import os

def generate_v6_svgs():
    assets_dir = r"c:\Holidays\Arnim-Zola\assets"
    os.makedirs(assets_dir, exist_ok=True)

    # LinkedIn SVG v6 - Symmetrically centered text + icon combo
    linkedin_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 165 42" width="165" height="42">
  <defs>
    <linearGradient id="bgGradIn6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#238636"/>
      <stop offset="100%" stop-color="#1a6328"/>
    </linearGradient>
    <clipPath id="btnClipIn6">
      <rect x="1" y="1" width="163" height="40" rx="20" ry="20"/>
    </clipPath>
  </defs>

  <style>
    .pill-bg {
      fill: url(#bgGradIn6);
      stroke: #39d353;
      stroke-width: 2;
      rx: 20;
      ry: 20;
      animation: pillGlow 6s cubic-bezier(0.4, 0, 0.2, 1) infinite;
    }
    .label {
      font-family: 'Space Grotesk', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 1.5px;
      fill: #ffffff;
      text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.8);
      dominant-baseline: central;
      text-anchor: middle;
    }

    .text-resting {
      animation: slideExitRight 6s cubic-bezier(0.2, 0.8, 0.25, 1) infinite;
    }
    .text-hovered {
      animation: slideEnterLeft 6s cubic-bezier(0.2, 0.8, 0.25, 1) infinite;
    }

    .icon-anim {
      animation: iconWatermarkIn 6s cubic-bezier(0.2, 0.8, 0.25, 1) infinite;
    }

    @keyframes slideExitRight {
      0%, 40% {
        opacity: 1;
        transform: translateX(0);
      }
      48%, 90% {
        opacity: 0;
        transform: translateX(50px);
      }
      96%, 100% {
        opacity: 1;
        transform: translateX(0);
      }
    }

    @keyframes slideEnterLeft {
      0%, 40% {
        opacity: 0;
        transform: translateX(-50px);
      }
      48%, 90% {
        opacity: 1;
        transform: translateX(0);
      }
      96%, 100% {
        opacity: 0;
        transform: translateX(50px);
      }
    }

    @keyframes iconWatermarkIn {
      0%, 40% {
        opacity: 1;
        transform: translate(122px, 21px) scale(1);
      }
      48%, 90% {
        opacity: 0.15;
        transform: translate(130px, 21px) scale(3.2);
      }
      96%, 100% {
        opacity: 1;
        transform: translate(122px, 21px) scale(1);
      }
    }

    @keyframes pillGlow {
      0%, 40% {
        stroke: #39d353;
        fill: #238636;
      }
      48%, 90% {
        stroke: #00ff66;
        fill: #2ea043;
      }
      96%, 100% {
        stroke: #39d353;
        fill: #238636;
      }
    }
  </style>

  <!-- Button Background -->
  <rect x="1" y="1" width="163" height="40" class="pill-bg"/>

  <!-- Clipped Interactive Content -->
  <g clip-path="url(#btnClipIn6)">
    <!-- Right-Side Icon centered at (122, 21) -->
    <g class="icon-anim" transform="translate(122, 21)">
      <svg x="-8" y="-8" width="16" height="16" viewBox="0 0 24 24" fill="#ffffff">
        <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
      </svg>
    </g>

    <!-- Resting State: LINKEDIN centered at x=70 (combo spans 36 to 130) -->
    <text x="70" y="21.5" class="label text-resting">LINKEDIN</text>

    <!-- Hovered State: CONNECT perfectly centered in the 165px pill -->
    <text x="82.5" y="21.5" class="label text-hovered">CONNECT</text>
  </g>
</svg>
"""

    # Email SVG v6 - Symmetrically centered text + icon combo
    email_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 165 42" width="165" height="42">
  <defs>
    <linearGradient id="bgGradMail6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#238636"/>
      <stop offset="100%" stop-color="#1a6328"/>
    </linearGradient>
    <clipPath id="btnClipMail6">
      <rect x="1" y="1" width="163" height="40" rx="20" ry="20"/>
    </clipPath>
  </defs>

  <style>
    .pill-bg {
      fill: url(#bgGradMail6);
      stroke: #39d353;
      stroke-width: 2;
      rx: 20;
      ry: 20;
      animation: pillGlow 6s cubic-bezier(0.4, 0, 0.2, 1) infinite;
    }
    .label {
      font-family: 'Space Grotesk', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 1.5px;
      fill: #ffffff;
      text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.8);
      dominant-baseline: central;
      text-anchor: middle;
    }

    .text-resting {
      animation: slideExitRight 6s cubic-bezier(0.2, 0.8, 0.25, 1) infinite;
    }
    .text-hovered {
      animation: slideEnterLeft 6s cubic-bezier(0.2, 0.8, 0.25, 1) infinite;
    }

    .icon-anim {
      animation: iconWatermarkMail 6s cubic-bezier(0.2, 0.8, 0.25, 1) infinite;
    }

    @keyframes slideExitRight {
      0%, 40% {
        opacity: 1;
        transform: translateX(0);
      }
      48%, 90% {
        opacity: 0;
        transform: translateX(50px);
      }
      96%, 100% {
        opacity: 1;
        transform: translateX(0);
      }
    }

    @keyframes slideEnterLeft {
      0%, 40% {
        opacity: 0;
        transform: translateX(-50px);
      }
      48%, 90% {
        opacity: 1;
        transform: translateX(0);
      }
      96%, 100% {
        opacity: 0;
        transform: translateX(50px);
      }
    }

    @keyframes iconWatermarkMail {
      0%, 40% {
        opacity: 1;
        transform: translate(110px, 21px) scale(1);
      }
      48%, 90% {
        opacity: 0.15;
        transform: translate(122px, 21px) scale(3.2);
      }
      96%, 100% {
        opacity: 1;
        transform: translate(110px, 21px) scale(1);
      }
    }

    @keyframes pillGlow {
      0%, 40% {
        stroke: #39d353;
        fill: #238636;
      }
      48%, 90% {
        stroke: #00ff66;
        fill: #2ea043;
      }
      96%, 100% {
        stroke: #39d353;
        fill: #238636;
      }
    }
  </style>

  <!-- Button Background -->
  <rect x="1" y="1" width="163" height="40" class="pill-bg"/>

  <!-- Clipped Interactive Content -->
  <g clip-path="url(#btnClipMail6)">
    <!-- Right-Side Icon centered at (110, 21) -->
    <g class="icon-anim" transform="translate(110, 21)">
      <svg x="-8" y="-8" width="16" height="16" viewBox="0 0 24 24" fill="#ffffff">
        <path d="M24 5.457v13.909c0 .904-.732 1.636-1.636 1.636h-3.819V11.73L12 16.64l-6.545-4.91v9.273H1.636A1.636 1.636 0 0 1 0 19.366V5.457c0-2.023 2.309-3.178 3.927-1.964L5.455 4.64 12 9.548l6.545-4.91 1.528-1.145C21.69 2.28 24 3.434 24 5.457z"/>
      </svg>
    </g>

    <!-- Resting State: EMAIL centered at x=70 (combo spans 48 to 118, center is 83) -->
    <text x="70" y="21.5" class="label text-resting">EMAIL</text>

    <!-- Hovered State: SEND MAIL perfectly centered in the 165px pill -->
    <text x="82.5" y="21.5" class="label text-hovered">SEND MAIL</text>
  </g>
</svg>
"""

    for fname, content in [("btn-linkedin.svg", linkedin_svg), 
                           ("btn-linkedin-v6.svg", linkedin_svg),
                           ("btn-email.svg", email_svg), 
                           ("btn-email-v6.svg", email_svg)]:
        with open(os.path.join(assets_dir, fname), "w", encoding="utf-8") as f:
            f.write(content)

    print("Created v6 SVGs with mathematically balanced centering for text and icons!")

if __name__ == "__main__":
    generate_v6_svgs()
