import re

def func(match):
    m = match.group(0)
    # print("func: <{}>".format(m))
    if m == "&&":
        return "and"
    elif m == "||":
        return "or"
    #else:
    return "<?"+m+"?>"

N = int(input())
bSP = r"(?<= )"
eSP = r"(?= )"
AND = re.escape("&&")
OR  = re.escape("||")
ANDorOR = r"(" + AND + r"|" + OR + ")"

for i in range(N):
    line = input()
    # print("L1", line)
    line = re.sub(
        bSP + ANDorOR + eSP,
        func,
        line
    )
    # print("L2", line)
    print(line)

