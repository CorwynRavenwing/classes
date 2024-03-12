def reverse(L):
    LL = list(L)    # copy, so as not to erase the original
    # print("RL", LL)
    R = []
    for i in range(len(LL)):
        c = LL.pop()
        # print("RC", c)
        R.append(c)
    # print("RR", R)
    return R
    
def reflect_list(L):
    # print("L", L)
    R = reverse(L)
    f = R.pop()
    # print("R", R)
    # print("f", f)
    # print("L", L)
    B = R + L
    # print("B", B)
    return B

def rangoli_line(ABA):
    A_B_A = "-".join(ABA)
    return A_B_A

def print_rangoli(size):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letters = list(alphabet)
    lines = []
    for begin in range(0,size):
        used = letters[begin:size]
        ABA = reflect_list(used)
        A_B_A = rangoli_line(ABA)
        lines.append(A_B_A)
        # print(A_B_A)
    
    A_B_A = reflect_list(lines)
    # print(A_B_A)
    width = max(list(map(len, A_B_A)))
    # print(width)
    for l in A_B_A:
        print(l.center(width, '-'))
    
    return

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

