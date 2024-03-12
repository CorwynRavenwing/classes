if __name__ == '__main__':
    N = int(input())
    L = []
    # print("L", L)
    for i in range(N):
        line = input().split()
        # print("LINE:", line)
        cmd = line[0]
        # print("CMD:", cmd)
        if cmd == "insert":
            i = int(line[1])
            e = int(line[2])
            L.insert(i, e)
        elif cmd == "print":
            print(L)
        elif cmd == "remove":
            e = int(line[1])
            L.remove(e)
        elif cmd == "append":
            e = int(line[1])
            L.append(e)
        elif cmd == "sort":
            L.sort()
        elif cmd == "pop":
            L.pop()
        elif cmd == "reverse":
            L.reverse()
        else:
            print("ERROR: invalid cmd", cmd)
        # print("L", L)

