def wrapper(func):
    def remove_lead_0_91(item):
        # print("#R", item)
        if item[0] == "+":
            item = item[1:]
            # print("#+", item)
        if item[0] == "0" and len(item) == 10+1:
            item = item[1:]
            # print("#0", item)
        elif item[0] == "9" and item[1] == "1" and len(item) == 10+2:
            item = item[2:]
            # print("#91", item)
        return item
    
    def format_for_print(item):
        # print("#F0", item)
        item = "+91" + " " + item[0:5] + " " + item[5:]
        # print("#F1", item)
        return item
    
    def fun(L):
        # print("#L", L)
        for i, item in enumerate(L):
            # print("#I0", i, item)
            item = remove_lead_0_91(item)
            # print("#I1", i, item)
            item = format_for_print(item)
            # print("#I2", i, item)
            L[i] = item
        return func(L)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 

