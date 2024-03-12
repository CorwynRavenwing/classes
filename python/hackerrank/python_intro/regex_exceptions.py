import re

T = int(input())
for i in range(T):
    line = input()
    try:
        x = re.search(line, "TEST")
        # print("#X", x, bool(x))
        print(True)
    except re.error as e:
        # print("#E", e)
        print(False)

