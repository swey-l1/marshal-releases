#!/usr/bin/env python3
"""Render download-stats.csv into download-chart.svg (Marshal-themed line chart)."""
import csv, math, os

rows = []
if os.path.exists("download-stats.csv"):
    with open("download-stats.csv") as f:
        for r in csv.DictReader(f):
            try:
                rows.append((r["date"], int(r["total_downloads"])))
            except (KeyError, ValueError):
                pass

W, H = 760, 260
PL, PR, PT, PB = 52, 22, 44, 42
iw, ih = W - PL - PR, H - PT - PB
n = len(rows)
maxv = max((v for _, v in rows), default=1) or 1
axis_max = max(1, int(math.ceil(maxv / 5.0) * 5))
accent = "#7c6cf6"

def X(i):
    return PL + (iw * i / (n - 1) if n > 1 else iw / 2)
def Y(v):
    return PT + ih * (1 - v / axis_max)

p = []
p.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
         f'font-family="ui-sans-serif,system-ui,Segoe UI,sans-serif">')
p.append(f'<rect width="{W}" height="{H}" rx="14" fill="#0c0d12"/>')
p.append(f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="13.5" fill="none" stroke="#272c3a"/>')
p.append('<defs><linearGradient id="g" x1="0" x2="0" y1="0" y2="1">'
         f'<stop offset="0" stop-color="{accent}" stop-opacity="0.32"/>'
         f'<stop offset="1" stop-color="{accent}" stop-opacity="0"/></linearGradient></defs>')
for k in range(5):
    gy = PT + ih * k / 4
    val = axis_max * (1 - k / 4)
    p.append(f'<line x1="{PL}" y1="{gy:.1f}" x2="{W-PR}" y2="{gy:.1f}" stroke="#1b1f2a"/>')
    p.append(f'<text x="{PL-8}" y="{gy+4:.1f}" fill="#6b7186" font-size="11" text-anchor="end">{int(round(val))}</text>')
cur = rows[-1][1] if rows else 0
p.append(f'<text x="{PL}" y="24" fill="#e9ebf2" font-size="14" font-weight="700">Marshal — total downloads</text>')
p.append(f'<text x="{W-PR}" y="24" fill="{accent}" font-size="14" font-weight="700" text-anchor="end">{cur}</text>')
if n >= 2:
    line = " ".join(f"{X(i):.1f},{Y(v):.1f}" for i, (_, v) in enumerate(rows))
    p.append(f'<polygon points="{PL},{PT+ih:.1f} {line} {X(n-1):.1f},{PT+ih:.1f}" fill="url(#g)"/>')
    p.append(f'<polyline points="{line}" fill="none" stroke="{accent}" stroke-width="2.5" '
             f'stroke-linejoin="round" stroke-linecap="round"/>')
    p.append(f'<circle cx="{X(n-1):.1f}" cy="{Y(rows[-1][1]):.1f}" r="3.5" fill="{accent}"/>')
elif n == 1:
    p.append(f'<circle cx="{X(0):.1f}" cy="{Y(rows[0][1]):.1f}" r="4" fill="{accent}"/>')
if rows:
    p.append(f'<text x="{PL}" y="{H-14}" fill="#6b7186" font-size="11">{rows[0][0]}</text>')
    p.append(f'<text x="{W-PR}" y="{H-14}" fill="#6b7186" font-size="11" text-anchor="end">{rows[-1][0]}</text>')
p.append("</svg>")
with open("download-chart.svg", "w") as f:
    f.write("\n".join(p))
print("wrote download-chart.svg (", n, "points, current", cur, ")")
