from collections import defaultdict

dd = defaultdict(list)

(N, M) = tuple(map(int, input().split()))
# import group A size N
for i in range(1,N+1):  # 1-indexed
    word = input()
    print("A:", word)
    dd[word].append(str(i))
print(dd)
# import group B size M
for j in range(1, M+1):  # 1-indexed
    word = input()
    print("B:", word)
    ans = dd[word]
    if len(ans):
        print(' '.join(ans))
    else:
        print(-1)
# print("C:", 'c')
# ans = dd['c']
# if len(ans):
#     print(' '.join(ans))
# else:
#     print(-1)

