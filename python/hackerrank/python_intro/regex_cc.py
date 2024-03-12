import re

def delete(match):
    return ""

def check_cc(cc):
    # print("# cc", cc)
    if not re.match(r"[456]", cc):
        print("# not 456", cc[0])
        return False

    okay = False
    if re.match(r"^[0-9]{16}$", cc):
        okay = True
    elif re.match(r"^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}$", cc):
        okay = True
        cc = re.sub(r"[-]", delete, cc)
        # print("# cc", cc)
    else:
        okay = False
    if not okay:
        # print("# not okay")
        return False
    for d in range(10):
        # digit 0 .. 9
        d4 = str(d) * 4
        # print("# d4", d4)
        if re.search(d4, cc):
            # print("# MATCH d4", d4)
            return False
    return True

N = int(input())
for i in range(N):
    line = input()
    if check_cc(line):
        print("Valid")
    else:
        print("Invalid")

