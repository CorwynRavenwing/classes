from collections import Counter

X = int(input())
shoes = tuple(map(int, input().split()))
shoe_counter = Counter(shoes)
N = int(input())
money = 0
for i in range(N):
    print(shoe_counter)
    (size,price) = tuple(map(int, input().split()))
    if shoe_counter[size]:
        print("buy a size {} for ${}".format(size,price))
        shoe_counter[size] -= 1
        money += price
    else:
        print("out of size {}".format(size))
print(shoe_counter)
print(money)

