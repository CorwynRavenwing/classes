import re

fp_test = re.compile(r"^[-+]?[0-9]*[.][0-9]+$")

T = int(input())
for i in range(T):
    line = input()
    # print("# L", line)
    ans = re.match(fp_test, line)
    # print("# A", ans)
    print(bool(ans))

