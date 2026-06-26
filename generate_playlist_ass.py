#!/usr/bin/env python3
"""
Tạo file tracklist .ass từ file config.json.

Cách dùng:
  1. Sửa file config.json: tracks, duration, layout, fonts, colors.
  2. Chạy:  python3 generate_playlist_ass.py
  3. Mở file .ass bằng Aegisub để chỉnh toạ độ / font / size nếu cần.
"""

import json
from pathlib import Path


def hms_to_sec(hms: str) -> float:
    parts = list(map(float, hms.split(":")))
    return parts[0] * 3600 + parts[1] * 60 + parts[2]


def sec_to_ass_time(t: float) -> str:
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def hex_to_ass_color(hex_rgb: str, alpha: str = "00") -> str:
    """ASS dùng định dạng &HAABBGGRR& (đảo thứ tự so với RRGGBB).
    Chú ý: alpha trong ASS là NGƯỢC - 00 = đục hoàn toàn, FF = trong suốt hoàn toàn."""
    r, g, b = hex_rgb[0:2], hex_rgb[2:4], hex_rgb[4:6]
    return f"&H{alpha}{b}{g}{r}&"


def build_ass(cfg, tracks_with_time, total_duration) -> str:
    colors = cfg["colors"]
    fonts = cfg["fonts"]
    layout = cfg["layout"]

    base_c = hex_to_ass_color(colors["base"])
    hi_c = hex_to_ass_color(colors["hilight"])
    sub_base_c = hex_to_ass_color(colors["sub_base"])
    sub_hi_c = hex_to_ass_color(colors["sub_hilight"])

    TAIL = "100,100,0,0,1,0,0,7,0,0,0,1"

    header = f"""[Script Info]
Title: Tracklist
ScriptType: v4.00+
PlayResX: {cfg['resolution'][0]}
PlayResY: {cfg['resolution'][1]}
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: TrackBase,{fonts['title']},38,{base_c},{base_c},&H00000000&,&H00000000&,0,0,0,0,{TAIL}
Style: TrackHi,{fonts['title']},38,{hi_c},{hi_c},&H00000000&,&H00000000&,-1,0,0,0,{TAIL}
Style: SubBase,{fonts['sub']},30,{sub_base_c},{sub_base_c},&H00000000&,&H00000000&,0,1,0,0,{TAIL}
Style: SubHi,{fonts['sub']},30,{sub_hi_c},{sub_hi_c},&H00000000&,&H00000000&,-1,1,0,0,{TAIL}

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

    t0 = sec_to_ass_time(0)
    tend = sec_to_ass_time(total_duration)
    events = []

    y = layout["y_start"]
    for i, tr in enumerate(tracks_with_time, start=1):
        title_line = f"{i}. {tr['title']}"
        start_t = sec_to_ass_time(tr["start"])
        end_t = sec_to_ass_time(tr["end"])

        events.append(f"Dialogue: 0,{t0},{start_t},TrackBase,,0,0,0,,{{\\pos({layout['x']},{y})}}{title_line}")
        events.append(f"Dialogue: 0,{start_t},{end_t},TrackHi,,0,0,0,,{{\\pos({layout['x']},{y})}}{title_line}")
        events.append(f"Dialogue: 0,{end_t},{tend},TrackBase,,0,0,0,,{{\\pos({layout['x']},{y})}}{title_line}")

        if tr["sub"]:
            y_sub = y + layout["sub_y_offset"]
            events.append(f"Dialogue: 0,{t0},{start_t},SubBase,,0,0,0,,{{\\pos({layout['x'] + 28},{y_sub})}}{tr['sub']}")
            events.append(f"Dialogue: 0,{start_t},{end_t},SubHi,,0,0,0,,{{\\pos({layout['x'] + 28},{y_sub})}}{tr['sub']}")
            events.append(f"Dialogue: 0,{end_t},{tend},SubBase,,0,0,0,,{{\\pos({layout['x'] + 28},{y_sub})}}{tr['sub']}")
            y += layout["line_height"]
        else:
            y += layout["line_height_no_sub"]

    return header + "\n".join(events) + "\n"


def main():
    cfg_path = Path(__file__).parent / "config.json"
    cfg = json.loads(cfg_path.read_text(encoding="utf-8"))

    cursor = 0.0
    tracks_with_time = []
    for tr in cfg["tracks"]:
        dur = hms_to_sec(tr["duration"])
        tracks_with_time.append({**tr, "start": cursor, "end": cursor + dur, "duration": dur})
        print(f"  {tr['title']}: {tr['duration']}  ({sec_to_ass_time(cursor)} -> {sec_to_ass_time(cursor + dur)})")
        cursor += dur
    total_duration = cursor

    ass_content = build_ass(cfg, tracks_with_time, total_duration)
    Path(cfg["output"]).write_text(ass_content, encoding="utf-8")
    print(f"\nĐã tạo {cfg['output']} | Tổng thời lượng: {total_duration:.1f}s")


if __name__ == "__main__":
    main()
