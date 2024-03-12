from collections import OrderedDict

od = OrderedDict()

N = int(input())
for i in range(N):
    L = input().split()
    item_price = int(L.pop())
    item_name = " ".join(L)
    if item_name in od:
        item_price += od[item_name]
    od[item_name] = item_price

for item_name, item_price in od.items():
    print(item_name, item_price)

