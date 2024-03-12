def special_sort(e):
    group = "X"
    if e.islower():
        group = "A"
    elif e.isupper():
        group = "B"
    elif e.isdigit():
        if int(e) % 2:
            group = "C"
        else:
            group = "D"
    else:
        group = "E"
    # print(group + e)
    return group + e

line = input()
# print(line)
arr = list(line)
# print(arr)
arr.sort(key=special_sort)
# print(arr)
line = ''.join(arr)
print(line)

