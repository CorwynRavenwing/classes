N = int(input())
for i in range(N):
    (a, b) = tuple(input().split())
    # print("#A", a)
    # print("#B", b)
    try:
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)

