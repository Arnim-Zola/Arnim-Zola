import os

def generate_exact_localhost_svgs():
    assets_dir = r"c:\Holidays\Arnim-Zola\assets"
    os.makedirs(assets_dir, exist_ok=True)

    # LinkedIn SVG matching localhost pixel-for-pixel:
    # Text on the LEFT, Icon on the RIGHT
    linkedin_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 165 42" width="165" height="42">
  <defs>
    <linearGradient id="bgIn" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#238636"/>
      <stop offset="100%" stop-color="#1a6328"/>
    </linearGradient>
  </defs>

  <style>
    .pill {
      fill: url(#bgIn);
      stroke: #39d353;
      stroke-width: 2;
      rx: 21;
      ry: 21;
      filter: drop-shadow(0 4px 10px rgba(35, 134, 54, 0.35));
    }
    .label {
      font-family: 'Space Grotesk', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 1.5px;
      fill: #ffffff;
      text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.8);
      dominant-baseline: central;
    }
  </style>

  <!-- Background Capsule -->
  <rect x="1" y="1" width="163" height="40" class="pill"/>

  <!-- Text on Left -->
  <text x="32" y="21.5" class="label">LINKEDIN</text>

  <!-- Icon on Right (16x16 viewBox 0 0 24 24) -->
  <g transform="translate(118, 13)">
    <svg width="16" height="16" viewBox="0 0 24 24" fill="#ffffff">
      <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
    </svg>
  </g>
</svg>
"""

    # Email SVG matching localhost pixel-for-pixel:
    # Text on the LEFT, Icon on the RIGHT
    email_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 165 42" width="165" height="42">
  <defs>
    <linearGradient id="bgMail" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#238636"/>
      <stop offset="100%" stop-color="#1a6328"/>
    </linearGradient>
  </defs>

  <style>
    .pill {
      fill: url(#bgMail);
      stroke: #39d353;
      stroke-width: 2;
      rx: 21;
      ry: 21;
      filter: drop-shadow(0 4px 10px rgba(35, 134, 54, 0.35));
    }
    .label {
      font-family: 'Space Grotesk', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 1.5px;
      fill: #ffffff;
      text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.8);
      dominant-baseline: central;
    }
  </style>

  <!-- Background Capsule -->
  <rect x="1" y="1" width="163" height="40" class="pill"/>

  <!-- Text on Left -->
  <text x="44" y="21.5" class="label">EMAIL</text>

  <!-- Icon on Right (16x16 viewBox 0 0 24 24) -->
  <g transform="translate(108, 13)">
    <svg width="16" height="16" viewBox="0 0 24 24" fill="#ffffff">
      <path d="M24 5.457v13.909c0 .904-.732 1.636-1.636 1.636h-3.819V11.73L12 16.64l-6.545-4.91v9.273H1.636A1.636 1.636 0 0 1 0 19.366V5.457c0-2.023 2.309-3.178 3.927-1.964L5.455 4.64 12 9.548l6.545-4.91 1.528-1.145C21.69 2.28 24 3.434 24 5.457z"/>
    </svg>
  </g>
</svg>
"""

    for fname, content in [("btn-linkedin.svg", linkedin_svg), 
                           ("btn-linkedin-v2.svg", linkedin_svg),
                           ("btn-linkedin-v3.svg", linkedin_svg),
                           ("btn-email.svg", email_svg), 
                           ("btn-email-v2.svg", email_svg),
                           ("btn-email-v3.svg", email_svg)]:
        with open(os.path.join(assets_dir, fname), "w", encoding="utf-8") as f:
            f.write(content)

    print("All SVGs updated with exact localhost layout!")

if __name__ == "__main__":
    generate_exact_localhost_svgs()
