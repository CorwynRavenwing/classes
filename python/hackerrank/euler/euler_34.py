
def factorial(N): 
    retval = N
    for i in range(1, N):
        retval *= i
        # print("#I", i, retval)
    return retval

def euler_34(N):
    retval = []
    # minimum 10 is because we must have >1 digit
    for C in range(10, N):
        digits = map(int, list(str(C)))
        factorial_sum = sum([
            factorial(d)
            for d in digits
        ])
        if factorial_sum % C == 0:
            print(f"#FOUND! {C} divides {factorial_sum}")
            retval.append(C)
    print(f"#{retval=}")
    return sum(retval) if len(retval) else 0

N = int(input().strip())
print(euler_34(N))

