import math

count = 0

def is_smart_number(num):
    global count
    count += 1
    print("#" ,"=" * 20, count, "=" * 20)
    val = int(math.sqrt(num))
    print("#N", num, val, num / val, num // val, num % val)
    if num == val * val:
        return True
    return False

for _ in range(int(input())):
    num = int(input())
    ans = is_smart_number(num)
    if ans:
        print("YES")
    else:
        print("NO")

