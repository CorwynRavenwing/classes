from collections import namedtuple

N = int(input())
headers = input()
# print("headers", headers)
Student = namedtuple('Student',headers)
marks = []
for i in range(N):
    Ii = tuple(input().split())
    # print("Ii", Ii)
    Si = Student(*Ii)
    # print("Si", Si)
    marks.append(int(Si.MARKS))
print(sum(marks)/N)

