import os
import re
import json
import urllib.request
from datetime import datetime
import xml.etree.ElementTree as ET

def fetch_live_stats(username, token):
    """
    Fetches real-time GitHub stats via GitHub GraphQL API.
    Returns dictionary with parsed values or None on error.
    """
    if not token:
        return None

    query = """
    query($login: String!) {
      user(login: $login) {
        name
        contributionsCollection {
          totalCommitContributions
          totalPullRequestContributions
          totalIssueContributions
          restrictedContributionsCount
          contributionCalendar {
            totalContributions
            weeks {
              contributionDays {
                contributionCount
                date
                weekday
                color
              }
            }
          }
        }
        repositories(first: 100, ownerAffiliations: OWNER, isFork: false) {
          nodes {
            name
            stargazerCount
            languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
              edges {
                size
                node {
                  name
                  color
                }
              }
            }
          }
        }
      }
    }
    """
    req_body = json.dumps({"query": query, "variables": {"login": username}}).encode("utf-8")
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=req_body,
        headers={
          "Authorization": f"bearer {token}",
          "User-Agent": "Arnim-Zola-Telemetry-Bot",
          "Content-Type": "application/json"
        }
    )

    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            if "errors" in res_data:
                print("GraphQL Error:", res_data["errors"])
                return None
            user_data = res_data.get("data", {}).get("user")
            if not user_data:
                return None

            col = user_data.get("contributionsCollection", {})
            cal = col.get("contributionCalendar", {})
            repos = user_data.get("repositories", {}).get("nodes", [])

            # 1. Basic Stats
            total_contributions = cal.get("totalContributions", 174)
            total_commits = col.get("totalCommitContributions", 0) + col.get("restrictedContributionsCount", 0)
            total_prs = col.get("totalPullRequestContributions", 0)
            total_issues = col.get("totalIssueContributions", 0)
            total_stars = sum(r.get("stargazerCount", 0) for r in repos)

            # 2. Streaks calculation from calendar days
            all_days = []
            for w in cal.get("weeks", []):
                for d in w.get("contributionDays", []):
                    all_days.append(d)

            current_streak = 0
            curr_streak_date = "Today"
            longest_streak = 0
            longest_start = None
            longest_end = None

            temp_streak = 0
            temp_start = None

            for i, day in enumerate(all_days):
                cnt = day.get("contributionCount", 0)
                dt_str = day.get("date")
                if cnt > 0:
                    if temp_streak == 0:
                        temp_start = dt_str
                    temp_streak += 1
                    if temp_streak > longest_streak:
                        longest_streak = temp_streak
                        longest_start = temp_start
                        longest_end = dt_str
                else:
                    temp_streak = 0

            # Current streak ending at the end of calendar
            if all_days:
                today_day = all_days[-1]
                if today_day.get("contributionCount", 0) > 0:
                    current_streak = 1
                    for d in reversed(all_days[:-1]):
                        if d.get("contributionCount", 0) > 0:
                            current_streak += 1
                        else:
                            break
                    curr_streak_date = datetime.strptime(today_day.get("date"), "%Y-%m-%d").strftime("%b %d").lstrip("0")
                elif len(all_days) > 1 and all_days[-2].get("contributionCount", 0) > 0:
                    current_streak = 1
                    for d in reversed(all_days[:-2]):
                        if d.get("contributionCount", 0) > 0:
                            current_streak += 1
                        else:
                            break
                    curr_streak_date = datetime.strptime(all_days[-2].get("date"), "%Y-%m-%d").strftime("%b %d").lstrip("0")

            longest_range = "Active"
            if longest_start and longest_end:
                s_dt = datetime.strptime(longest_start, "%Y-%m-%d").strftime("%b %d").lstrip("0")
                e_dt = datetime.strptime(longest_end, "%Y-%m-%d").strftime("%b %d").lstrip("0")
                longest_range = f"{s_dt} &#8211; {e_dt}"

            # 3. Languages aggregation
            lang_sizes = {}
            lang_colors = {}
            color_fallbacks = {
                "JavaScript": "#f1e05a",
                "Python": "#3572A5",
                "CSS": "#663399",
                "HTML": "#e34c26",
                "Batchfile": "#C1F12E",
                "Shell": "#89e051",
                "TypeScript": "#3178c6",
                "C++": "#f34b7d",
                "ShaderLab": "#222c37",
                "GLSL": "#5686a5"
            }

            for r in repos:
                for edge in r.get("languages", {}).get("edges", []):
                    lname = edge.get("node", {}).get("name")
                    lcolor = edge.get("node", {}).get("color") or color_fallbacks.get(lname, "#00ff66")
                    lsize = edge.get("size", 0)
                    lang_sizes[lname] = lang_sizes.get(lname, 0) + lsize
                    lang_colors[lname] = lcolor

            sorted_langs = sorted(lang_sizes.items(), key=lambda x: x[1], reverse=True)
            total_code_size = sum(lang_sizes.values()) or 1

            langs_list = []
            for lname, lsize in sorted_langs[:6]:
                pct = round((lsize / total_code_size) * 100, 2)
                langs_list.append((lname, pct, lang_colors.get(lname, color_fallbacks.get(lname, "#00ff66"))))

            while len(langs_list) < 6:
                langs_list.append(("-", 0.0, "#1b4d2e"))

            return {
                "total_contributions": total_contributions,
                "total_commits": total_commits,
                "total_prs": total_prs,
                "total_issues": total_issues,
                "total_stars": total_stars,
                "current_streak": current_streak,
                "curr_streak_date": curr_streak_date,
                "longest_streak": longest_streak,
                "longest_range": longest_range,
                "languages": langs_list,
                "weeks": cal.get("weeks", [])
            }

    except Exception as e:
        print("Error fetching live GitHub stats:", e)
        return None

def fetch_public_contribution_calendar(username="Arnim-Zola"):
    import urllib.request
    import re
    from datetime import datetime

    url = f"https://github.com/users/{username}/contributions"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode("utf-8")

        matches = re.findall(r'data-date="([^"]+)"\s+id="([^"]+)"\s+data-level="([^"]+)"', html)
        tooltips = dict(re.findall(r'for="([^"]+)"[^>]*>([^<]+)</tool-tip>', html))

        day_map = {}
        for dt, cid, lvl in matches:
            tt = tooltips.get(cid, "")
            cnt_match = re.search(r'(\d+)\s+contribution', tt)
            cnt = int(cnt_match.group(1)) if cnt_match else 0
            day_map[dt] = {
                "date": dt,
                "contributionCount": cnt,
                "level": int(lvl),
                "tooltip": tt
            }

        if not day_map:
            return None, 0

        sorted_dates = sorted(day_map.keys())
        weeks = []
        cur_week = []
        for dt_str in sorted_dates:
            dt = datetime.strptime(dt_str, "%Y-%m-%d")
            weekday = (dt.weekday() + 1) % 7
            day_data = day_map[dt_str]
            day_data["weekday"] = weekday
            cur_week.append(day_data)
            if weekday == 6:
                weeks.append({"contributionDays": cur_week})
                cur_week = []
        if cur_week:
            weeks.append({"contributionDays": cur_week})

        total_contribs = sum(d["contributionCount"] for d in day_map.values())
        print(f"Successfully fetched real public GitHub contributions: {total_contribs} contributions across {len(weeks)} weeks")
        return weeks, total_contribs
    except Exception as e:
        print("Error fetching real public contribution calendar:", e)
        return None, 0

def build_heatmap_svg(weeks, total_contributions):
    month_svg_parts = []
    cells_svg_parts = []
    last_month_x = -100

    for w_idx, w in enumerate(weeks):
        col_x = round(64 + w_idx * 14.6, 1)
        days = w.get("contributionDays", [])
        if days:
            first_d = days[0]
            try:
                dt = datetime.strptime(first_d.get("date", ""), "%Y-%m-%d")
                if w_idx == 0 or (dt.day <= 7 and col_x - last_month_x >= 38):
                    m_name = dt.strftime("%b")
                    month_svg_parts.append(f'<text x="{col_x}" y="160" class="month-lbl">{m_name}</text>')
                    last_month_x = col_x
            except Exception:
                pass

            for day in days:
                weekday = day.get("weekday", 0)
                cnt = day.get("contributionCount", 0)
                lvl = day.get("level", 0)
                dt_str = day.get("date", "")
                tooltip_txt = day.get("tooltip") or f"{cnt} contributions on {dt_str}"
                cell_y = round(172 + weekday * 13.5, 1)

                if lvl == 0 and cnt == 0:
                    fill = "#0d2415"
                    stroke = ' stroke="#173f24" stroke-width="0.7"'
                elif lvl == 1 or cnt <= 5:
                    fill = "#005524"
                    stroke = ''
                elif lvl == 2 or cnt <= 15:
                    fill = "#009940"
                    stroke = ''
                elif lvl == 3 or cnt <= 25:
                    fill = "#00dd5b"
                    stroke = ''
                else:
                    fill = "#00ff66"
                    stroke = ''
                cells_svg_parts.append(f'<rect x="{col_x}" y="{cell_y}" width="11" height="11" rx="2.5" fill="{fill}"{stroke}><title>{tooltip_txt}</title></rect>')

    month_svg = "\n    ".join(month_svg_parts)
    cells_svg = "\n    ".join(cells_svg_parts)
    return month_svg, cells_svg

def generate_telemetry_svg():
    assets_dir = r"c:\Holidays\Arnim-Zola\assets"
    token = os.environ.get("GITHUB_TOKEN")
    username = os.environ.get("GITHUB_USERNAME", "Arnim-Zola")

    live_stats = fetch_live_stats(username, token)

    if live_stats:
        print("Using freshly fetched live GitHub telemetry stats!")
        total_contributions = live_stats["total_contributions"]
        total_commits = live_stats["total_commits"]
        total_prs = live_stats["total_prs"]
        total_issues = live_stats["total_issues"]
        total_stars = live_stats["total_stars"]
        current_streak = live_stats["current_streak"]
        curr_streak_date = live_stats["curr_streak_date"]
        longest_streak = live_stats["longest_streak"]
        longest_range = live_stats["longest_range"]
        public_weeks, real_total = fetch_public_contribution_calendar(username)
        weeks = live_stats.get("weeks") or public_weeks
        if real_total > 0:
            total_contributions = real_total
    else:
        print("Using local default/fallback telemetry values.")
        public_weeks, real_total = fetch_public_contribution_calendar(username)
        total_contributions = real_total if real_total > 0 else 177
        total_commits = 114
        total_prs = 2
        total_issues = 0
        total_stars = 0
        current_streak = 0
        curr_streak_date = "Sep 5"
        longest_streak = 3
        longest_range = "Jun 19 &#8211; Jun 21"
        languages = [
            ("JavaScript", 80.33, "#f1e05a"),
            ("Python", 16.74, "#3572A5"),
            ("CSS", 2.38, "#663399"),
            ("HTML", 0.38, "#e34c26"),
            ("Batchfile", 0.09, "#C1F12E"),
            ("Shell", 0.08, "#89e051")
        ]
        weeks = public_weeks

    # Read base64 font from taglines.svg for signature Caacupe One
    taglines_path = os.path.join(assets_dir, "taglines.svg")
    caacupe_font_css = ""
    if os.path.exists(taglines_path):
        with open(taglines_path, "r", encoding="utf-8") as f:
            taglines_content = f.read()
        font_match = re.search(r"@font-face\s*\{[^}]*\}", taglines_content, re.DOTALL)
        caacupe_font_css = font_match.group(0) if font_match else ""

    vbox_w = 920
    vbox_h = 740
    card_w = 872
    card_x = 24

    # Build progress bar segments for languages (Wide 816px bar across Card 3)
    bar_width_total = 816
    cur_x = 0
    bar_rects = []
    for idx, (lname, pct, col) in enumerate(languages):
        if pct <= 0:
            continue
        seg_w = max(1.5, round((pct / 100.0) * bar_width_total, 1))
        if cur_x + seg_w > bar_width_total:
            seg_w = bar_width_total - cur_x
        rx_attr = ' rx="5"' if (idx == 0 or idx == len(languages)-1) else ''
        bar_rects.append(f'<rect x="{cur_x}" y="0" width="{seg_w}" height="10"{rx_attr} fill="{col}" />')
        cur_x += seg_w
    bar_svg = "\n      ".join(bar_rects)

    # 3 Columns x 2 Rows for Languages Grid (Wide layout)
    col_x_offsets = [28, 316, 604]
    lang_grid_lines = []
    for idx, (lname, pct, col) in enumerate(languages):
        col_idx = idx % 3
        row_idx = idx // 3
        bx = col_x_offsets[col_idx]
        by = 82 + row_idx * 34
        pct_str = f"{pct:.2f}%" if pct > 0 else "0.0%"
        lang_grid_lines.append(f'''<g transform="translate({bx}, {by})">
      <circle cx="5" cy="5" r="4.5" fill="{col}" />
      <text x="18" y="9" class="lang-name">{lname}</text>
      <text x="240" y="9" class="lang-pct">{pct_str}</text>
    </g>''')

    lang_grid_svg = "\n    ".join(lang_grid_lines)
    month_svg, cells_svg = build_heatmap_svg(weeks, total_contributions)

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vbox_w} {vbox_h}" width="100%" height="{vbox_h}" fill="none">
  <defs>
    <style>
      <![CDATA[
      {caacupe_font_css}

      .card-title {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 16px;
        font-weight: 400;
        letter-spacing: 0.5px;
        fill: #ffffff;
      }}
      .card-title-green {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 16px;
        font-weight: 400;
        letter-spacing: 0.5px;
        fill: #7ee787;
      }}
      .telemetry-title {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 13px;
        font-weight: 400;
        letter-spacing: 1px;
        fill: #7ee787;
      }}
      .streak-val {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 38px;
        font-weight: 400;
        letter-spacing: 0.5px;
        fill: #ffffff;
        text-anchor: middle;
      }}
      .streak-curr-val {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 28px;
        font-weight: 400;
        fill: #ffffff;
        text-anchor: middle;
      }}
      .streak-lbl {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 12.5px;
        font-weight: 400;
        letter-spacing: 0.5px;
        fill: #7ee787;
        text-anchor: middle;
      }}
      .streak-curr-label {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 12.5px;
        font-weight: 400;
        letter-spacing: 0.5px;
        fill: #00ff66;
        text-anchor: middle;
      }}
      .streak-sub {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 11.5px;
        font-weight: 400;
        fill: #8b949e;
        text-anchor: middle;
      }}
      .heatmap-header {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 13.5px;
        font-weight: 400;
        letter-spacing: 0.8px;
        fill: #7ee787;
      }}
      .heatmap-total {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 12px;
        font-weight: 400;
        fill: #8b949e;
      }}
      .month-lbl {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 10.5px;
        font-weight: 400;
        fill: #7ee787;
      }}
      .day-lbl {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 10px;
        font-weight: 400;
        fill: #7ee787;
      }}
      .legend-lbl {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 11px;
        font-weight: 400;
        fill: #8b949e;
      }}
      .stat-lbl {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 13.5px;
        font-weight: 400;
        letter-spacing: 0.2px;
        fill: #ffffff;
      }}
      .stat-num {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 14px;
        font-weight: 400;
        fill: #00ff66;
        text-anchor: end;
      }}
      .lang-name {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 13.5px;
        font-weight: 400;
        letter-spacing: 0.2px;
        fill: #ffffff;
      }}
      .lang-pct {{
        font-family: 'Caacupe One', cursive, sans-serif;
        font-size: 13.5px;
        font-weight: 400;
        fill: #7ee787;
        text-anchor: end;
      }}
      ]]>
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

    <!-- 2. Atmospheric Moonlight Glow (Centered on Moon at x:740, y:72) -->
    <ellipse cx="740" cy="72" rx="260" ry="170" fill="url(#moonRadialHaze)" />

    <!-- 3. Ambient Radiant Moon Bloom -->
    <path d="M 754,28 A 45 45 0 1 1 709,98 A 43 43 0 0 0 754,28 Z" fill="#34d399" opacity="0.48" filter="url(#moonAura)" />

    <!-- 4. Celestial Emerald Crescent Moon -->
    <path d="M 754,28 A 45 45 0 1 1 709,98 A 43 43 0 0 0 754,28 Z" fill="url(#naturalMoonGrad)" filter="url(#moonBloom)" stroke="rgba(244, 255, 247, 0.7)" stroke-width="0.8" />

    <!-- 5. Diamond Sparkle Stars in Headroom -->
    <g>
      <!-- Sparkle 1 (Top Left) -->
      <path d="M 145,70 Q 145,85 150,85 Q 145,85 145,100 Q 145,85 140,85 Q 145,85 145,70 Z" fill="#d1fae5" filter="url(#sparkleGlow)" />
      <circle cx="145" cy="85" r="2.2" fill="#f0fff4" />
      
      <!-- Sparkle 2 (Mid Sky) -->
      <path d="M 420,80 Q 420,92 424,92 Q 420,92 420,104 Q 420,92 416,92 Q 420,92 420,80 Z" fill="#d1fae5" filter="url(#sparkleGlow)" />
      <circle cx="420" cy="92" r="1.8" fill="#f0fff4" />

      <!-- Sparkle 3 (Near Moon) -->
      <path d="M 610,55 Q 610,65 613,65 Q 610,65 610,75 Q 610,65 607,65 Q 610,65 610,55 Z" fill="#d1fae5" filter="url(#sparkleGlow)" />
      <circle cx="610" cy="65" r="1.8" fill="#f0fff4" />

      <!-- Sparkle 4 (Right) -->
      <path d="M 870,75 Q 870,85 873,85 Q 870,85 870,95 Q 870,85 867,85 Q 870,85 870,75 Z" fill="#a7f3d0" filter="url(#sparkleGlow)" />
      <circle cx="870" cy="85" r="1.8" fill="#f0fff4" />
    </g>

    <!-- 6. Stardust Ambient Dots in Headroom -->
    <g opacity="0.8">
      <circle cx="210" cy="38" r="1.5" fill="#86efac" />
      <circle cx="280" cy="68" r="1.4" fill="#d1fae5" />
      <circle cx="360" cy="40" r="1.8" fill="#86efac" />
      <circle cx="510" cy="50" r="1.6" fill="#f0fff4" />
      <circle cx="750" cy="65" r="1.6" fill="#86efac" />
      <circle cx="810" cy="95" r="1.4" fill="#d1fae5" />
      <circle cx="680" cy="85" r="1.5" fill="#86efac" />
      <circle cx="490" cy="88" r="1.4" fill="#f0fff4" />
    </g>

    <!-- 7. Upper Drifting Clouds in Headroom -->
    <g>
      <!-- Cloud Left -->
      <path d="M -40,110 C -15,75 45,70 80,92 C 115,65 178,65 214,92 C 250,78 290,100 304,128 C 270,142 130,146 -40,138 Z" fill="url(#cloudGradSoft1)" opacity="0.85" />
      <path d="M -40,110 C -15,75 45,70 80,92 C 115,65 178,65 214,92 C 250,78 290,100 304,128" fill="none" stroke="url(#cloudRimLight)" stroke-width="2" opacity="0.8" />

      <!-- Cloud Right -->
      <path d="M 640,110 C 650,75 708,60 748,80 C 784,58 848,58 884,80 C 920,66 965,75 1000,98 L 1000,134 C 970,148 905,148 855,130 C 805,148 740,144 690,126 C 660,130 640,120 640,110 Z" fill="url(#cloudGradSoft2)" opacity="0.85" />
      <path d="M 640,110 C 650,75 708,60 748,80 C 784,58 848,58 884,80 C 920,66 965,75 1000,98" fill="none" stroke="url(#cloudRimLight)" stroke-width="2" opacity="0.85" />
    </g>

    <!-- ==================== BOTTOM LANDSCAPE (Generous Scenery below Card 3) ==================== -->
    <!-- Horizon Soft Cloud Center -->
    <path d="M 150,615 C 190,580 250,575 290,597 C 335,565 410,560 455,593 C 500,565 575,565 620,593 C 660,575 715,585 750,611 C 778,633 745,655 688,663 C 570,677 270,677 150,615 Z" fill="url(#cloudGradCenter)" opacity="0.82" />

    <!-- Distant Misty Rolling Hills -->
    <path d="M -30,645 Q 200,585 480,645 T 950,620 L 950,750 L -30,750 Z" fill="url(#distantRidgeGrad)" />
    <path d="M -30,645 Q 200,585 480,645 T 950,620" fill="none" stroke="rgba(134, 239, 172, 0.22)" stroke-width="1.2" />

    <!-- Mid Rolling Hills -->
    <path d="M -30,670 Q 250,625 500,680 Q 710,640 950,665 L 950,750 L -30,750 Z" fill="url(#midRidgeGrad)" />
    <path d="M -30,670 Q 250,625 500,680 Q 710,640 950,665" fill="none" stroke="rgba(110, 231, 183, 0.16)" stroke-width="1.4" />

    <!-- Foreground Rolling Hills -->
    <path d="M -30,695 Q 300,660 600,705 Q 780,675 950,708 L 950,750 L -30,750 Z" fill="url(#foreRidgeGrad)" />

    <!-- Silhouette Pine Trees (Rising in Foreground) -->
    <!-- Left Tree -->
    <g transform="translate(45, 595) scale(0.68)">
      <rect x="180" y="140" width="12" height="50" fill="#010603" rx="2" />
      <polygon points="186,40 216,145 156,145" fill="#072011" />
      <polygon points="186,20 210,95 162,95" fill="#0b2c18" />
      <polygon points="186,0 204,55 168,55" fill="#0f3c21" />
    </g>
    <!-- Right Trees -->
    <g transform="translate(825, 600) scale(0.62)">
      <rect x="100" y="140" width="10" height="45" fill="#010603" rx="2" />
      <polygon points="105,45 130,140 80,140" fill="#061c0e" />
      <polygon points="105,25 125,95 85,95" fill="#092514" />
      <polygon points="105,10 120,55 90,55" fill="#0c321b" />
    </g>
  </g>

  <!-- Container Outline Border & Inner Glow -->
  <rect x="0" y="0" width="{vbox_w}" height="{vbox_h}" rx="14" fill="none" stroke="#164d27" stroke-width="1.5" />

  <!-- ==================== TOP TELEMETRY BAR ==================== -->
  <g transform="translate(24, 22)">
    <!-- Pulsing Beacon Dot -->
    <circle cx="4" cy="5" r="4" fill="#00ff66" filter="url(#sparkleGlow)" />
    <circle cx="4" cy="5" r="2" fill="#ffffff" />
    <text x="16" y="9" class="telemetry-title">CORE TELEMETRY &#8226; SYNCHRONIZED</text>
    <line x1="0" y1="20" x2="{vbox_w - 48}" y2="20" stroke="#164d27" stroke-width="1" stroke-opacity="0.6" />
  </g>

  <!-- ==================== UNIFIED CARD 1: CONTRIBUTIONS & STREAKS (Pushed Down to y=135) ==================== -->
  <g transform="translate({card_x}, 135)" filter="url(#cardShadow)">
    <rect width="{card_w}" height="130" rx="12" fill="#040906" stroke="#164d27" stroke-width="1.5" />
    
    <!-- Top Row Metric Col 1: Total Contributions (Center x=145) -->
    <g transform="translate(145, 12)">
      <text x="0" y="44" class="streak-val">{total_contributions}</text>
      <text x="0" y="76" class="streak-lbl">TOTAL CONTRIBUTIONS</text>
      <text x="0" y="102" class="streak-sub">Jul 7, 2025 &#8211; Present</text>
    </g>

    <!-- Vertical Divider 1 -->
    <line x1="290" y1="18" x2="290" y2="112" stroke="#163d22" stroke-width="1" />

    <!-- Top Row Metric Col 2: Current Streak Ring (Center x=436) -->
    <g transform="translate(436, 12)">
      <!-- SVG Ring -->
      <circle cx="0" cy="30" r="28" stroke="#163d22" stroke-width="3.5" fill="none" />
      <circle cx="0" cy="30" r="28" stroke="#00ff66" stroke-width="3.5" stroke-dasharray="176" stroke-dashoffset="176" stroke-linecap="round" fill="none" />
      <text x="0" y="39" class="streak-curr-val">{current_streak}</text>
      
      <text x="0" y="76" class="streak-curr-label">CURRENT STREAK</text>
      <text x="0" y="102" class="streak-sub">{curr_streak_date}</text>
    </g>

    <!-- Vertical Divider 2 -->
    <line x1="582" y1="18" x2="582" y2="112" stroke="#163d22" stroke-width="1" />

    <!-- Top Row Metric Col 3: Longest Streak (Center x=727) -->
    <g transform="translate(727, 12)">
      <text x="0" y="44" class="streak-val">{longest_streak}</text>
      <text x="0" y="76" class="streak-lbl">LONGEST STREAK</text>
      <text x="0" y="102" class="streak-sub">{longest_range}</text>
    </g>
  </g>

  <!-- ==================== STACKED CARD 2: GITHUB OVERALL STATS (Pushed Down to y=285) ==================== -->
  <g transform="translate({card_x}, 285)" filter="url(#cardShadow)">
    <rect width="{card_w}" height="145" rx="12" fill="#040906" stroke="#164d27" stroke-width="1.5" />
    
    <text x="28" y="28" class="card-title">Mohammed Sahil's GitHub Stats</text>

    <!-- Left Column (3 items) -->
    <!-- Item 1: Total Stars -->
    <g transform="translate(36, 44)">
      <path d="M7 0.5 L8.8 4.2 L13 4.8 L9.9 7.8 L10.6 12 L7 10 L3.4 12 L4.1 7.8 L1 4.8 L5.2 4.2 Z" fill="#00ff66" />
      <text x="24" y="10" class="stat-lbl">Total Stars Earned:</text>
      <text x="360" y="10" class="stat-num">{total_stars}</text>
    </g>

    <!-- Item 2: Total Commits -->
    <g transform="translate(36, 74)">
      <circle cx="7" cy="7" r="6" stroke="#00ff66" stroke-width="1.5" fill="none" />
      <path d="M7 3.5 L7 7 L9.5 8.5" stroke="#00ff66" stroke-width="1.5" fill="none" stroke-linecap="round" />
      <text x="24" y="11" class="stat-lbl">Total Commits:</text>
      <text x="360" y="11" class="stat-num">{total_commits}</text>
    </g>

    <!-- Item 3: Total PRs -->
    <g transform="translate(36, 104)">
      <circle cx="4" cy="3" r="2" fill="#00ff66" />
      <circle cx="4" cy="11" r="2" fill="#00ff66" />
      <circle cx="10" cy="7" r="2" fill="#00ff66" />
      <path d="M4 3 L4 11 M10 7 L10 5 C10 3.5 8 3.5 4 3.5" stroke="#00ff66" stroke-width="1.2" fill="none" />
      <text x="24" y="11" class="stat-lbl">Total PRs:</text>
      <text x="360" y="11" class="stat-num">{total_prs}</text>
    </g>

    <!-- Center Subtle Divider -->
    <line x1="436" y1="36" x2="436" y2="128" stroke="#163d22" stroke-width="1" />

    <!-- Right Column (2 items) -->
    <!-- Item 4: Total Issues -->
    <g transform="translate(476, 44)">
      <circle cx="7" cy="7" r="6" stroke="#00ff66" stroke-width="1.5" fill="none" />
      <circle cx="7" cy="7" r="1.5" fill="#00ff66" />
      <text x="24" y="11" class="stat-lbl">Total Issues:</text>
      <text x="360" y="11" class="stat-num">{total_issues}</text>
    </g>

    <!-- Item 5: Contributed to -->
    <g transform="translate(476, 74)">
      <rect x="2" y="2" width="10" height="10" rx="1.5" stroke="#00ff66" stroke-width="1.3" fill="none" />
      <line x1="5" y1="2" x2="5" y2="12" stroke="#00ff66" stroke-width="1" />
      <text x="24" y="11" class="stat-lbl">Contributed to (Last year):</text>
      <text x="360" y="11" class="stat-num">0</text>
    </g>
  </g>

  <!-- ==================== STACKED CARD 3: MOST USED LANGUAGES (Pushed Down to y=450) ==================== -->
  <g transform="translate({card_x}, 450)" filter="url(#cardShadow)">
    <rect width="{card_w}" height="150" rx="12" fill="#040906" stroke="#164d27" stroke-width="1.5" />
    
    <text x="28" y="28" class="card-title-green">Most Used Languages</text>

    <!-- Wide Multi-Segment Progress Bar -->
    <g transform="translate(28, 44)">
      <!-- Track Background -->
      <rect width="{bar_width_total}" height="10" rx="5" fill="#0e2617" />
      {bar_svg}
    </g>

    <!-- Language Grid Breakdown (3 Columns x 2 Rows) -->
    {lang_grid_svg}
  </g>
</svg>"""

    for fname in ["telemetry-cosmos-card.svg", "telemetry-cosmos-card-v1.svg", "telemetry-cosmos-card-v2.svg", "telemetry-cosmos-card-v3.svg", "telemetry-cosmos-card-v4.svg", "telemetry-cosmos-card-v5.svg", "telemetry-cosmos-card-v6.svg", "telemetry-cosmos-card-v7.svg", "telemetry-cosmos-card-v8.svg", "telemetry-cosmos-card-v9.svg"]:
        out_path = os.path.join(assets_dir, fname)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(svg_content)
    ET.fromstring(svg_content)
    print("Generated & Validated: telemetry-cosmos-card.svg, v1..v9")

if __name__ == "__main__":
    generate_telemetry_svg()
