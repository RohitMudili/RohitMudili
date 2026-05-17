"""Convert a portrait photo into ASCII art sized for the profile SVG.

Outputs two text files: ascii_dark.txt (chars dense on light pixels, for dark bg)
and ascii_light.txt (chars dense on dark pixels, for light bg).
Both are 44 cols x 25 rows to fit the left column of dark_mode.svg / light_mode.svg.
"""
from PIL import Image, ImageOps

SRC = '9bde6f21-fa60-4d29-ad4a-400c05f0be75.jpg'
COLS = 44
ROWS = 25
CHAR_ASPECT = 2.0  # consolas chars are ~2x taller than wide

# Ramp from darkest visual weight to lightest (10 levels).
# Index 0 = most ink, index -1 = blank.
RAMP = '@%#*+=-:. '


def to_ascii(invert: bool) -> str:
    img = Image.open(SRC).convert('L')
    img = ImageOps.autocontrast(img, cutoff=2)
    w, h = img.size
    # We want COLS columns and ROWS rows after correcting for char aspect.
    # Sample a region matching target aspect ratio, centered on face.
    target_ratio = (COLS) / (ROWS * CHAR_ASPECT)
    src_ratio = w / h
    if src_ratio > target_ratio:
        new_w = int(h * target_ratio)
        left = (w - new_w) // 2
        img = img.crop((left, 0, left + new_w, h))
    else:
        new_h = int(w / target_ratio)
        top = (h - new_h) // 2
        img = img.crop((0, top, w, top + new_h))
    img = img.resize((COLS, ROWS), Image.LANCZOS)

    lines = []
    for y in range(ROWS):
        row = []
        for x in range(COLS):
            v = img.getpixel((x, y))  # 0=black, 255=white
            if invert:
                # light background: dark pixels (low v) should be dense chars
                idx = int((v / 255) * (len(RAMP) - 1))
            else:
                # dark background: light pixels (high v) should be dense chars
                idx = int(((255 - v) / 255) * (len(RAMP) - 1))
            row.append(RAMP[idx])
        lines.append(''.join(row))
    return '\n'.join(lines)


if __name__ == '__main__':
    dark = to_ascii(invert=False)
    light = to_ascii(invert=True)
    with open('ascii_dark.txt', 'w', encoding='utf-8') as f:
        f.write(dark)
    with open('ascii_light.txt', 'w', encoding='utf-8') as f:
        f.write(light)
    print('=== DARK MODE (chars are highlights on dark bg) ===')
    print(dark)
    print()
    print('=== LIGHT MODE (chars are shadows on light bg) ===')
    print(light)
