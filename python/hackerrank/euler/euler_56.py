
def euler_56(N):
    answer = 0
    for A in range(N):
        for B in range(N):
            power = A ** B
            digits = list(str(power))
            digit_sum = sum(map(int, digits))
            # print(f"#{A=} {B=} {power=} {digit_sum}")
            answer = max(answer, digit_sum)
    return answer


N = int(input().strip())
print(euler_56(N))

