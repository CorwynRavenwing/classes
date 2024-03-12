n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    print("#S", s)
    cmds = input().split()
    print("#C", cmds)
    cmd = cmds[0]
    if cmd == "pop":
        s.pop()
        continue
    item = int(cmds[1])
    if cmd == "remove":
        s.remove(item)
    elif cmd == "discard":
        s.discard(item)
    else:
        print("ERROR: invalid command '{}({})'".format(cmd, item))
print("#S", s)
print(sum(s))

