"""Generate profile.svg: ASCII portrait on the left + colored neofetch info on the right.

Run when static content changes. today.py updates dynamic stat values in-place.
"""

ASCII_FILE = 'ascii_dark.txt'
OUTPUT = 'profile.svg'

# Left column (ASCII)
ASCII_X = 50
ASCII_Y = 80
ASCII_LINE_H = 22
ASCII_FONT_SIZE = 17
ASCII_COLOR = '#c9d1d9'

# Right column (info)
INFO_X = 660
INFO_Y = 30
INFO_LINE_H = 22
INFO_FONT_SIZE = 17

KEY = '#ffa657'
VALUE = '#a5d6ff'
CC = '#616e7f'
FG = '#c9d1d9'
BG = '#161b22'

WIDTH = 1260


def k(text): return (text, KEY)
def v(text, _id=None): return (text, VALUE, _id) if _id else (text, VALUE)
def s(text): return (text, CC)


rows = [
    [v('rohit'), s(' ----------------------------------------')],
    [s('. '), k('OS'), s(':'), v('        Windows 11')],
    [s('. '), k('Uptime'), s(':    '), ('pending', VALUE, 'UPTIME')],
    [s('. '), k('Role'), s(':'), v('      AI/ML Engineer')],
    [s('. '), k('Host'), s(':'), v('      Open Source Contributor')],
    [s('. '), k('IDE'), s(':'), v('       VSCode 1.96.0')],
    [],
    [s('. '), k('Languages'), s('.'), k('Programming'), s(':')],
    [s('    '), v('Python, JavaScript, TypeScript, C++')],
    [s('. '), k('Languages'), s('.'), k('Computer'), s(':')],
    [s('    '), v('HTML, CSS, JSON, YAML, SQL')],
    [s('. '), k('Languages'), s('.'), k('Real'), s(':')],
    [s('    '), v('English, Hindi, Telugu')],
    [],
    [s('. '), k('Hobbies'), s('.'), k('Software'), s(':')],
    [s('    '), v('OSS Contributing, AI Experiments')],
    [],
    [s('- Contact ------------------------------------')],
    [s('. '), k('Email'), s(':     '), v('rohitmudili5@gmail.com')],
    [s('. '), k('LinkedIn'), s(':  '), v('linkedin.com/in/rohit-mudili')],
    [s('. '), k('GitHub'), s(':    '), v('github.com/RohitMudili')],
    [],
    [s('- GitHub Stats -------------------------------')],
    [
        s('. '), k('Repos'), s(':     '), ('0', VALUE, 'REPOS'),
        s(' {'), k('Contributed'), s(': '), ('0', VALUE, 'CONTRIB'), s('}'),
    ],
    [s('. '), k('Stars'), s(':     '), ('0', VALUE, 'STARS')],
    [s('. '), k('Commits'), s(':   '), ('0', VALUE, 'COMMITS')],
    [s('. '), k('Followers'), s(': '), ('0', VALUE, 'FOLLOWERS')],
    [s('. '), k('Lines of Code on GitHub'), s(':')],
    [s('    '), ('pending', VALUE, 'LOC')],
]


def main():
    ascii_lines = open(ASCII_FILE, encoding='utf-8').read().splitlines()
    ascii_height = ASCII_Y + ASCII_LINE_H * len(ascii_lines)
    info_height = INFO_Y + INFO_LINE_H * len(rows)
    height = max(ascii_height, info_height) + 16

    svg = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{height}" '
        f'font-family="Consolas, ui-monospace, monospace">',
        f'<rect width="{WIDTH}" height="{height}" fill="{BG}" rx="10"/>',
    ]

    # ASCII portrait (left)
    svg.append(f'<g font-size="{ASCII_FONT_SIZE}px" fill="{ASCII_COLOR}">')
    for i, line in enumerate(ascii_lines):
        # XML-escape the line (only & < > matter, none in our ramp)
        escaped = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        y = ASCII_Y + i * ASCII_LINE_H
        svg.append(f'<text x="{ASCII_X}" y="{y}" xml:space="preserve">{escaped}</text>')
    svg.append('</g>')

    # Info card (right)
    svg.append(f'<g font-size="{INFO_FONT_SIZE}px" fill="{FG}">')
    y = INFO_Y
    for row in rows:
        if not row:
            y += INFO_LINE_H
            continue
        parts = [f'<text x="{INFO_X}" y="{y}" xml:space="preserve">']
        for span in row:
            if len(span) == 3:
                text, color, _id = span
                parts.append(f'<tspan fill="{color}" id="{_id}">{text}</tspan>')
            else:
                text, color = span
                parts.append(f'<tspan fill="{color}">{text}</tspan>')
        parts.append('</text>')
        svg.append(''.join(parts))
        y += INFO_LINE_H
    svg.append('</g>')

    svg.append('</svg>')
    with open(OUTPUT, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg))
    print(f'{OUTPUT} written: {WIDTH}x{height}')


if __name__ == '__main__':
    main()
