import re

phone_test = re.compile(r"^[789]\d{9}$")

N = int(input())
for i in range(N):
    line = input()
    if (re.match(phone_test, line)):
        print("YES")
    else:
        print("NO")

