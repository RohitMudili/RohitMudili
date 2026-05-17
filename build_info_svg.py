"""Generate info.svg with the colored neofetch-style info card.

Run this whenever the static info content (labels, hobbies, etc.) changes.
today.py updates the dynamic stat values inside this SVG at workflow time.
"""

WIDTH = 660
LINE_H = 22
START_Y = 26
LEFT_PAD = 18
FONT_SIZE = 17

KEY = '#ffa657'
VALUE = '#a5d6ff'
CC = '#616e7f'
FG = '#c9d1d9'
BG = '#161b22'


def k(text): return (text, KEY)
def v(text, _id=None): return (text, VALUE, _id) if _id else (text, VALUE)
def s(text): return (text, CC)


rows = [
    [v('rohit'), s(' ----------------------------------------')],
    [s('. '), k('OS'), s(':'), v('        Windows 11')],
    [s('. '), k('Uptime'), s(':    '), ('pending', VALUE, 'UPTIME')],
    [s('. '), k('Role'), s(':'), v('      AI/ML Engineer')],
    [s('. '), k('Host'), s(':'), v('      Open Source Contributor')],
    [s('. '), k('IDE'), s(':'), v('       VSCode, Claude Code')],
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
    height = START_Y + LINE_H * len(rows) + 10
    svg = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{height}" '
        f'font-family="Consolas, ui-monospace, monospace" font-size="{FONT_SIZE}px">',
        f'<rect width="{WIDTH}" height="{height}" fill="{BG}" rx="10"/>',
    ]
    y = START_Y
    for row in rows:
        if not row:
            y += LINE_H
            continue
        parts = [f'<text x="{LEFT_PAD}" y="{y}" fill="{FG}">']
        for span in row:
            if len(span) == 3:
                text, color, _id = span
                parts.append(f'<tspan fill="{color}" id="{_id}">{text}</tspan>')
            else:
                text, color = span
                parts.append(f'<tspan fill="{color}">{text}</tspan>')
        parts.append('</text>')
        svg.append(''.join(parts))
        y += LINE_H
    svg.append('</svg>')
    with open('info.svg', 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg))
    print(f'info.svg written: {WIDTH}x{height}, {FONT_SIZE}px')


if __name__ == '__main__':
    main()
