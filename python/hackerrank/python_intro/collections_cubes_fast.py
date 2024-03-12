def can_stack(B):
    for i in range(1, len(B)-1):
        left = B[i-1]
        center = B[i]
        right = B[i+1]
        # print("#I", i, ":", left, center, right)
        if left < center and center > right:
            # print("#I", i, ":", left, center, right)
            # print("FAIL: {} is highest".format(center))
            return False
    return True

T = int(input())
for t in range(T):
    N = int(input())
    B = list(map(int, input().split()))
    print("Yes" if can_stack(B) else "No")

