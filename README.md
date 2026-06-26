# Playlister - Generate ASS Tracklist

Tự động tạo file phụ đề `.ass` hiển thị danh sách bài hát, tự highlight bài đang phát theo thời gian.

## Cách dùng

### 1. Cấu hình danh sách bài hát

Mở `generate_playlist_ass.py`, sửa phần `CONFIG` ở đầu file:

```python
TRACKS = [
    {"title": "Tên bài hát", "sub": "(Sub-title)", "duration": "00:03:30"},
    {"title": "Bài không có sub", "sub": None, "duration": "00:04:15"},
]
```

| Trường | Mô tả |
|---|---|
| `title` | Tên bài hát (hiển thị chính) |
| `sub` | Sub-title, đặt `None` nếu không có |
| `duration` | Thời lượng bài theo format `HH:MM:SS` |

### 2. Chạy script

```bash
python3 generate_playlist_ass.py
```

Kết quả: tạo file `tracklist.ass` cùng thư mục.

### 3. Sử dụng file .ass

- Nạp vào video editor (OBS, Premiere, VLC...) như một phụ đề bình thường.
- Mở bằng [Aegisub](https://aegisub.org/) để tinh chỉnh toạ độ, font, size.

## Hiệu ứng highlight

Khi bài đang phát, text sẽ:
- **Bold** đậm lên
- **Sáng hơn** (đổi sang màu highlight)

Bài chưa phát / đã phát: text bình thường, màu base nhạt hơn.

## Tuỳ chỉnh

Các tham số trong phần `CONFIG`:

| Tham số | Mặc định | Mô tả |
|---|---|---|
| `ASS_FILE` | `tracklist.ass` | Tên file output |
| `RES_X, RES_Y` | 1920x1080 | Độ phân giải video |
| `LIST_X` | 145 | Vị trí X của danh sách |
| `LIST_Y_START` | 410 | Vị trí Y bắt đầu |
| `LINE_HEIGHT` | 100 | Chiều cao dòng (có sub) |
| `LINE_HEIGHT_NO_SUB` | 64 | Chiều cao dòng (không sub) |
| `FONT_TITLE` | Playfair Display | Font tên bài |
| `FONT_SUB` | Cormorant Garamond | Font sub-title |
| `COLOR_BASE` | `D2BEDC` | Màu text bình thường |
| `COLOR_HILIGHT` | `FFE6F7` | Màu text highlight |
| `COLOR_SUB_BASE` | `D2BEDC` | Màu sub bình thường |
| `COLOR_SUB_HILIGHT` | `FFD1EF` | Màu sub highlight |

Màu sắc dùng format hex `RRGGBB` (viết thường hay hoa đều được).

## Yêu cầu

- Python 3.6+ (không cần thư viện thêm)
