# Arnim-Zola Profile Design System & Architecture

This repository houses the visual identity and dynamic HUD assets for Mohammed Sahil's GitHub profile.

## 1. Color Palette & Theming
- **Primary Cyber Accent**: `#00ff66` (Neon Emerald)
- **Secondary Accent**: `#7ee787` (Muted Terminal Mint)
- **Background Void**: `#040906` / `#07150c` (Cyberpunk Deep Forest Dark)
- **Border / Structure**: `#163d22` / `#164d27` (Subtle Laser Green)
- **Typography Base**: `#ffffff` (High-contrast Pure White)

## 2. Typography
- **Display Font**: `Caacupe One` (Cursive Geometric / Cybernetic Display)
- **Fallback**: `system-ui`, `-apple-system`, `sans-serif`
- **Embedding Format**: Embedded Base64 TTF inside SVG `<defs><style>` blocks for cross-platform consistency.

## 3. Motion & Animation Standards
- **Banner**: Standalone parallax starfield (4-layer CSS animation, 2000px cycle).
- **Subtitles**: Iris text reveal animation with continuous looping keyframes.
- **Social Buttons**: Morphing hover state with watermarked expanding icons and glow transitions.
