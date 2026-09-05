import html
import os
import xml.etree.ElementTree as ET
import urllib.request
import base64
from PIL import ImageFont, ImageDraw, Image

# Download TTF for exact metrics
ttf_url = 'https://github.com/google/fonts/raw/main/ofl/caacupeone/CaacupeOne-Regular.ttf'
ttf_data = urllib.request.urlopen(ttf_url).read()
with open('CaacupeOne-Regular.ttf', 'wb') as f:
    f.write(ttf_data)

# Fetch latin woff2 for embedding
latin_url = 'https://fonts.gstatic.com/s/caacupeone/v2/PlI5Fl60NbF_eNjJe2jslWxDvcE.woff2'
font_data = urllib.request.urlopen(latin_url).read()
b64_latin = base64.b64encode(font_data).decode('utf-8')

taglines = [
    "Architecting Autonomous Multimodal AI Systems",
    "Building Sub-Second Agentic RAG Pipelines",
    "High-Throughput Celery & Redis AI Microservices",
    "Engineering 60FPS 3D WebGL Experiences",
    "Crafting Custom GLSL GPU Shaders",
    "Building Fluid 3D Web Interfaces",
    "Creating Interactive Three.js Shader Experiences"
]

view_width = 900
view_height = 76
font_size = 36.0
y_pos = 50
total_dur = 28.0  # 4.0s per tagline
n = len(taglines)
slot_dur = total_dur / n  # 4.0s

font = ImageFont.truetype('CaacupeOne-Regular.ttf', int(font_size))
dummy_img = Image.new('RGB', (1, 1))
draw = ImageDraw.Draw(dummy_img)

svg_clips = []
svg_groups = []

for i, text in enumerate(taglines):
    slot_start = i * slot_dur
    slot_end = (i + 1) * slot_dur
    
    # Measure cumulative character positions
    full_bbox = draw.textbbox((0, 0), text, font=font)
    text_w = full_bbox[2] - full_bbox[0]
    start_x = (view_width - text_w) / 2
    
    # Calculate each character's exact X coordinate and width
    char_positions = []
    curr_prefix = ""
    for char in text:
        w_before = draw.textbbox((0, 0), curr_prefix, font=font)[2] if curr_prefix else 0
        curr_prefix += char
        w_after = draw.textbbox((0, 0), curr_prefix, font=font)[2]
        char_w = w_after - w_before
        char_x = start_x + w_before
        char_positions.append((char, char_x, char_w))
    
    group_chars = []
    
    for j, (char, char_x, char_w) in enumerate(char_positions):
        if char == ' ':
            continue
        cx = char_x + char_w / 2
        cy = y_pos - 11
        clip_id = f"iris-{i}-{j}"
        
        # Stagger reveal: each char expands from r=0 to r=54px over 0.24s, staggered by 0.016s per char
        reveal_start = slot_start + 0.12 + j * 0.016
        reveal_end = reveal_start + 0.24
        
        # Stagger hide: each char contracts back from r=54px to r=0px near the end of the slot
        hide_start = slot_end - 0.38 + j * 0.008
        hide_end = hide_start + 0.22
        
        # Normalize to 0..1 keyTimes
        k1 = max(0.0001, min(0.9996, reveal_start / total_dur))
        k2 = max(k1 + 0.0001, min(0.9997, reveal_end / total_dur))
        k3 = max(k2 + 0.0001, min(0.9998, hide_start / total_dur))
        k4 = max(k3 + 0.0001, min(0.9999, hide_end / total_dur))
        
        times = [0.0, k1, k2, k3, k4, 1.0]
        vals = [0, 0, 54, 54, 0, 0]
        
        if k1 <= 0.0002:
            times = [0.0, k2, k3, k4, 1.0]
            vals = [0, 54, 54, 0, 0]
            
        times_str = ";".join(f"{t:.5f}" for t in times)
        vals_str = ";".join(str(v) for v in vals)
        
        clip_def = f'''    <clipPath id="{clip_id}">
      <circle cx="{cx:.1f}" cy="{cy:.1f}" r="0">
        <animate attributeName="r" values="{vals_str}" keyTimes="{times_str}" dur="{total_dur}s" repeatCount="indefinite" />
      </circle>
    </clipPath>'''
        svg_clips.append(clip_def)
        
        char_esc = html.escape(char)
        group_chars.append(f'<text x="{char_x:.1f}" y="{y_pos}" clip-path="url(#{clip_id})">{char_esc}</text>')
        
    chars_joined = "\n    ".join(group_chars)
    svg_groups.append(f'  <!-- Tagline {i+1}: {text} -->\n  <g class="tagline tagline-{i}">\n    {chars_joined}\n  </g>')

clips_content = "\n".join(svg_clips)
groups_content = "\n".join(svg_groups)

svg_output = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {view_width} {view_height}" width="100%" height="{view_height}" fill="none">
  <defs>
    <style>
      <![CDATA[
      @font-face {{
        font-family: 'Caacupe One';
        font-style: normal;
        font-weight: 400;
        src: url(data:font/woff2;charset=utf-8;base64,{b64_latin}) format('woff2');
      }}

      .tagline text {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: {font_size}px;
        font-weight: 400;
        fill: #FFFFFF;
        letter-spacing: 1.8px;
      }}
      ]]>
    </style>
{clips_content}
  </defs>

{groups_content}
</svg>
'''

output_path = "assets/taglines.svg"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(svg_output)

# Clean TTF
if os.path.exists('CaacupeOne-Regular.ttf'):
    os.remove('CaacupeOne-Regular.ttf')

# Validate XML
ET.fromstring(svg_output)
print(f"Extra large Taglines SVG generated successfully at {font_size}px with {len(svg_clips)} clips!")
