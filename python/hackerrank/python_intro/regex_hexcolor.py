import re

css_re = r"(#[0-9A-Fa-f]{3}([0-9A-Fa-f]{3})?)"
css_test = re.compile(css_re)
open_test = re.compile(r"^[-.,#: A-Za-z0-9]*{\s*$")
close_test = re.compile(r"^\s*}\s*$")
in_css = False
N = int(input())
for i in range(N):
    line = input()
    # print("# L", line)
    if not in_css and re.match(open_test, line):
        in_css = True
        # print("# >>> enter mode CSS")
        continue
    elif in_css and re.match(close_test, line):
        in_css = False
        # print("# <<< exit mode CSS")
        continue
    elif not in_css:
        # print("# -- SELECTOR")
        continue
    m = re.findall(css_test, line)
    if len(m):
        for T in m:
            print(T[0])
    # else:
        # print("# -- m", m)

