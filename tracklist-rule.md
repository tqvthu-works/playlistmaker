# Mandopop Neon Playlist Style Guide

## Overview

Phong cách thị giác lấy cảm hứng từ:

* 90s–2000s Mandopop Romance
* Night City Lights
* Neon Glow Typography
* Glassmorphism UI
* Nostalgic Love Story
* Dreamy Urban Loneliness

Mục tiêu cảm xúc:

* Lãng mạn
* Hoài niệm
* Dịu dàng
* Buồn nhẹ
* Thành phố về đêm
* Ký ức tình yêu

---

# Color Palette

## Background Colors

```css
--bg-deep-navy: #080C22;
--bg-midnight-blue: #0A102E;
--bg-dark-purple: #140D2B;
--bg-indigo: #1A1238;
```

Sử dụng cho:

* Nền chính
* Overlay tối
* Thành phố đêm
* Vùng shadow

---

## Accent Colors

```css
--accent-pink: #FF3E92;
--accent-pink-soft: #FF4D9A;
--accent-neon: #FF61C8;
--accent-glow: #FF7FD4;
```

Sử dụng cho:

* Border
* Highlight title
* Glow effect
* Focus state

---

## Typography Colors

```css
--text-primary: #FFE6F7;
--text-secondary: #D8CBE4;
--text-muted: #B9A9C6;
--text-dim: rgba(210,190,220,0.75);
```

---

# Playlist Container

## Visual Style

Glassmorphism + Neon Border

```css
.playlist-box {
    background: rgba(12,8,35,0.28);

    backdrop-filter: blur(12px);

    border: 2px solid #FF3E92;

    box-shadow:
        0 0 10px rgba(255,70,160,.6),
        0 0 25px rgba(255,70,160,.35),
        inset 0 0 10px rgba(255,70,160,.15);
}
```

---

# Typography Rules

## Playlist Title

Ví dụ:

```text
BynG
Mandopop Playlist
```

### Main Title

```css
font-family: "Playfair Display", serif;
font-weight: 400;
letter-spacing: -1px;
color: #D8B8E6;
```

### Subtitle

```css
font-family: "Cormorant Garamond", serif;
font-style: italic;
font-weight: 300;
color: #E0C6EA;
```

---

# Song List

## Inactive Song

```css
font-family: "Playfair Display", serif;

color: rgba(210,190,220,.75);

text-shadow: none;
```

Visual characteristics:

* Mờ hơn
* Độ tương phản thấp
* Không có glow

---

## Active Song

Ví dụ:

```text
2. Chỉ Vì Em Đau Lòng
(Tình Đơn Phương 2)
```

### Text Color

```css
color: #FFE6F7;
```

### Glow Effect

```css
text-shadow:
    0 0 8px rgba(255,110,210,.8),
    0 0 18px rgba(255,80,190,.7),
    0 0 35px rgba(255,50,170,.6);
```

### Optional Premium Glow

```css
text-shadow:
    0 0 6px rgba(255,255,255,.9),
    0 0 12px rgba(255,140,220,.9),
    0 0 24px rgba(255,90,190,.8),
    0 0 48px rgba(255,40,170,.6);
```

---

# Subtitle Under Song

Ví dụ:

```text
(Tình Đơn Phương 2)
```

```css
font-family: "Cormorant Garamond", serif;
font-style: italic;
font-weight: 500;

color: #FFD1EF;
```

---

# Divider Lines

```css
.song-divider {
    border-bottom:
        1px solid rgba(255,255,255,.08);
}
```

Hoặc:

```css
.song-divider {
    background:
        linear-gradient(
            90deg,
            transparent,
            rgba(255,255,255,.15),
            transparent
        );
}
```

---

# Highlight Rules

Chỉ nên highlight:

* 1 bài hát duy nhất
* Bài hát đang quảng bá
* Bài hát mới phát hành
* Bài hát trọng tâm playlist

Các bài còn lại:

* Giảm sáng 30–50%
* Không glow
* Giữ cùng typography

---

# Visual Mood Rules

## Lighting

Ưu tiên:

* Neon reflection
* Soft bloom
* Wet surface reflection
* Purple-blue night lighting

Tránh:

* Ánh sáng ban ngày
* Màu vàng gắt
* Contrast quá mạnh

---

# Subject Rules

## Character

* Một người duy nhất
* Nữ trẻ châu Á
* Biểu cảm nhẹ nhàng
* Ánh mắt có chiều sâu
* Không cười quá tươi

## Emotion

Ưu tiên:

* Longing
* Nostalgia
* Melancholy
* Tenderness
* Bittersweet romance

---

# Recommended Font Pairings

## Option A (Original Style)

```text
Playfair Display
Cormorant Garamond
```

## Option B

```text
Bodoni Moda
Cormorant Garamond
```

## Option C

```text
DM Serif Display
Cormorant Garamond
```

---

# Style Keywords

mandopop,
90s mandopop,
city lights,
night romance,
neon glow,
pink neon,
glassmorphism,
nostalgic love,
dreamy city,
urban loneliness,
cinematic playlist cover,
romantic melancholy,
night river reflections,
soft bloom lighting

```
```
