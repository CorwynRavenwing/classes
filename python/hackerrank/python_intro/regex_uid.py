from collections import Counter

def check_uid(uid):
    # print("# UID", uid)
    if len(uid) != 10:
        # print("# nope, len", len(uid))
        return False
    char_usage = Counter()
    classes    = Counter()
    chars = list(uid)
    for c in chars:
        char_usage[c] += 1
        if c.isupper():
            classes["upper"] += 1
        elif c.islower():
            classes["lower"] += 1
        elif c.isdigit():
            classes["digit"] += 1
        else:
            classes["other"] += 1
    # print("# chars", char_usage)
    # print("# class", classes)
    if classes["upper"] < 2:
        # print("# upper<2", classes["upper"])
        return False
    if classes["digit"] < 3:
        # print("# digit<3", classes["digit"])
        return False
    if classes["other"] > 0:
        # print("# other>0", classes["other"])
        return False
    char_items = tuple(char_usage.items())
    # print("### items", char_items)
    for T in char_items:
        # print("# T", T)
        if T[1] > 1:
            # print("# ", T[0], "chars>1", T[1])
            return False
    return True

T = int(input())
for i in range(T):
    line = input()
    if check_uid(line):
        print("Valid")
    else:
        print("Invalid")

