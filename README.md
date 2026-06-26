# Playlister - Generate ASS Tracklist

Tự động tạo file phụ đề `.ass` hiển thị danh sách bài hát, tự highlight bài đang phát theo thời gian.

## Cách dùng

### 1. Sửa file `config.json`

Cấu hình danh sách bài hát, vị trí, font, màu sắc — tất cả trong 1 file.

```json
{
  "output": "tracklist.ass",
  "resolution": [1920, 1080],
  "tracks": [
    {"title": "Tên bài hát", "sub": "(Sub-title)", "duration": "00:03:30"},
    {"title": "Bài không có sub", "sub": null, "duration": "00:04:15"}
  ],
  "layout": {
    "x": 145,
    "y_start": 410,
    "line_height": 100,
    "line_height_no_sub": 64,
    "sub_y_offset": 44
  },
  "fonts": {
    "title": "Playfair Display",
    "sub": "Cormorant Garamond"
  },
  "colors": {
    "base": "D2BEDC",
    "hilight": "FFE6F7",
    "sub_base": "D2BEDC",
    "sub_hilight": "FFD1EF"
  }
}
```

### 2. Chạy script

```bash
python3 generate_playlist_ass.py
```

Kết quả: tạo file `.ass` theo đường dẫn trong `output`.

### 3. Sử dụng file .ass

- Nạp vào video editor (OBS, Premiere, VLC...) như một phụ đề bình thường.
- Mở bằng [Aegisub](https://aegisub.org/) để tinh chỉnh toạ độ, font, size.

## Cấu trúc config.json

### `tracks` — danh sách bài hát

| Field | Type | Mô tả |
|---|---|---|
| `title` | string | Tên bài hát, hiển thị làm dòng chính |
| `sub` | string \| null | Sub-title hiển thị bên dưới, đặt `null` nếu không có |
| `duration` | string | Thời lượng bài theo format `HH:MM:SS`, dùng để tính khoảng highlight |

### `layout` — vị trí hiển thị

| Field | Default | Mô tả |
|---|---|---|
| `x` | 145 | Toạ độ X của danh sách |
| `y_start` | 410 | Toạ độ Y bắt đầu |
| `line_height` | 100 | Chiều cao mỗi dòng (khi có sub-title) |
| `line_height_no_sub` | 64 | Chiều cao mỗi dòng (khi không có sub) |
| `sub_y_offset` | 44 | Khoảng cách từ title xuống sub-title |

### `fonts` — font chữ

| Field | Default | Mô tả |
|---|---|---|
| `title` | Playfair Display | Font cho tên bài |
| `sub` | Cormorant Garamond | Font cho sub-title |

### `colors` — màu sắc (hex RRGGBB)

| Field | Default | Mô tả |
|---|---|---|
| `base` | D2BEDC | Màu text bình thường |
| `hilight` | FFE6F7 | Màu text khi highlight (đang phát) |
| `sub_base` | D2BEDC | Màu sub-title bình thường |
| `sub_hilight` | FFD1EF | Màu sub-title khi highlight |

## Hiệu ứng highlight

Khi bài đang phát:
- **Bold** đậm lên
- **Sáng hơn** (màu highlight)

Bài chưa phát / đã phát: text bình thường, màu base nhạt hơn.

## Yêu cầu

- Python 3.6+ (không cần thư viện thêm)
