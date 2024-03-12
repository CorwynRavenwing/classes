# import re

# Say you have a problem.
# You think "I'll use regular expressions!"
# Now you have two problems.

string = input()
# m = re.match(r'(\d)\1', string)
# print("G", m.group(1))
L = list(string)
prev = None
done = False
for c in L:
    if not c.isalnum():
        continue
    elif prev == c:
        print(c)
        done = True
        break
    else:
        prev = c
if not done:
    print(-1)

