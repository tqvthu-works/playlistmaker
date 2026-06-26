#!/usr/bin/env python3
"""
Tạo file tracklist .ass từ danh sách bài hát với duration hardcode,
tự highlight đúng bài đang phát.

Cách dùng:
  1. Sửa phần CONFIG bên dưới: tên bài, sub-title, duration (HH:MM:SS).
  2. Chạy:  python3 generate_playlist_ass.py
  3. Mở file .ass bằng Aegisub để chỉnh toạ độ / font / size nếu cần.
"""

from pathlib import Path

# ====================== CONFIG - chỉnh ở đây ======================

ASS_FILE = "tracklist.ass"

RES_X, RES_Y = 1920, 1080

TRACKS = [
    {"title": "Tình Yêu Anh Dành Hết Cho Em", "sub": "(Bóng Dáng Thiên Thần)", "duration": "00:01:00"},
    {"title": "Chỉ Vì Em Đau Lòng",            "sub": "(Tình Đơn Phương 2)",   "duration": "00:01:30"},
    {"title": "Truy Mộng Nhân",                "sub": None,                    "duration": "00:02:00"},
    {"title": "Nụ Hồng Mong Manh",             "sub": None,                    "duration": "00:02:30"},
    {"title": "Sao Quá Mềm Lòng",              "sub": "(Con Tim Cổ Quên Em)", "duration": "00:03:00"},
]

LIST_X = 145
LIST_Y_START = 410
LINE_HEIGHT = 100
LINE_HEIGHT_NO_SUB = 64
SUB_Y_OFFSET = 44

FONT_TITLE = "Playfair Display"
FONT_SUB = "Cormorant Garamond"

COLOR_BASE = "D2BEDC"
COLOR_HILIGHT = "FFE6F7"
COLOR_SUB_BASE = "D2BEDC"
COLOR_SUB_HILIGHT = "FFD1EF"

# ====================================================================


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


def build_ass(tracks_with_time, total_duration) -> str:
    base_c = hex_to_ass_color(COLOR_BASE)
    hi_c = hex_to_ass_color(COLOR_HILIGHT)
    sub_base_c = hex_to_ass_color(COLOR_SUB_BASE)
    sub_hi_c = hex_to_ass_color(COLOR_SUB_HILIGHT)

    TAIL_BASE = "100,100,0,0,1,0,0,7,0,0,0,1"
    TAIL_HI = "100,100,0,0,1,0,0,7,0,0,0,1"
    TAIL_SUB_BASE = "100,100,0,0,1,0,0,7,0,0,0,1"

    header = f"""[Script Info]
Title: Tracklist
ScriptType: v4.00+
PlayResX: {RES_X}
PlayResY: {RES_Y}
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: TrackBase,{FONT_TITLE},38,{base_c},{base_c},&H00000000&,&H00000000&,0,0,0,0,{TAIL_BASE}
Style: TrackHi,{FONT_TITLE},38,{hi_c},{hi_c},&H00000000&,&H00000000&,-1,0,0,0,{TAIL_HI}
Style: SubBase,{FONT_SUB},30,{sub_base_c},{sub_base_c},&H00000000&,&H00000000&,0,1,0,0,{TAIL_SUB_BASE}
Style: SubHi,{FONT_SUB},30,{sub_hi_c},{sub_hi_c},&H00000000&,&H00000000&,-1,1,0,0,{TAIL_HI}

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

    t0 = sec_to_ass_time(0)
    tend = sec_to_ass_time(total_duration)
    events = []

    y = LIST_Y_START
    for i, tr in enumerate(tracks_with_time, start=1):
        title_line = f"{i}. {tr['title']}"
        start_t = sec_to_ass_time(tr["start"])
        end_t = sec_to_ass_time(tr["end"])

        events.append(f"Dialogue: 0,{t0},{start_t},TrackBase,,0,0,0,,{{\\pos({LIST_X},{y})}}{title_line}")
        events.append(f"Dialogue: 0,{start_t},{end_t},TrackHi,,0,0,0,,{{\\pos({LIST_X},{y})}}{title_line}")
        events.append(f"Dialogue: 0,{end_t},{tend},TrackBase,,0,0,0,,{{\\pos({LIST_X},{y})}}{title_line}")

        if tr["sub"]:
            y_sub = y + SUB_Y_OFFSET
            events.append(f"Dialogue: 0,{t0},{start_t},SubBase,,0,0,0,,{{\\pos({LIST_X + 28},{y_sub})}}{tr['sub']}")
            events.append(f"Dialogue: 0,{start_t},{end_t},SubHi,,0,0,0,,{{\\pos({LIST_X + 28},{y_sub})}}{tr['sub']}")
            events.append(f"Dialogue: 0,{end_t},{tend},SubBase,,0,0,0,,{{\\pos({LIST_X + 28},{y_sub})}}{tr['sub']}")
            y += LINE_HEIGHT
        else:
            y += LINE_HEIGHT_NO_SUB

    return header + "\n".join(events) + "\n"


def main():
    cursor = 0.0
    tracks_with_time = []
    for tr in TRACKS:
        dur = hms_to_sec(tr["duration"])
        tracks_with_time.append({**tr, "start": cursor, "end": cursor + dur, "duration": dur})
        print(f"  {tr['title']}: {tr['duration']}  ({sec_to_ass_time(cursor)} -> {sec_to_ass_time(cursor + dur)})")
        cursor += dur
    total_duration = cursor

    ass_content = build_ass(tracks_with_time, total_duration)
    Path(ASS_FILE).write_text(ass_content, encoding="utf-8")
    print(f"\nĐã tạo {ASS_FILE} | Tổng thời lượng: {total_duration:.1f}s")


if __name__ == "__main__":
    main()