class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        assert divisor != 0

        is_neg = False
        if dividend < 0:
            dividend = -dividend
            is_neg = not is_neg
        if divisor < 0:
            divisor = -divisor
            is_neg = not is_neg

        if divisor == 1:
            answer = dividend
            print(f'{dividend} / {divisor}: {answer}')
        else:
            answer = 0
            print(f'{dividend} / {divisor}: {answer}')

            power = [(1, divisor)]
            print(f'{power[0]=}')
            max_div = divisor
            while dividend >= max_div:
                P = power[-1]
                (N, D) = P
                (N1, D1) = (0, 0)
                for _ in range(10):
                    N1 += N
                    D1 += D
                max_div = D1
                P1 = (N1, D1)
                power.append(P1)
                print(f'power[{len(power)-1}]={P1}')

            while dividend >= divisor:
                print(f'{dividend} / {divisor}: {answer}')
                (N, D) = power.pop()
                print(f'POW:({N},{D})')
                while dividend >= D:
                    answer += N
                    dividend -= D
                    print(f'{dividend} / {divisor}: {answer}')
                # answer += 1
                # dividend -= divisor
                # print(f'{dividend} / {divisor}: {answer}')
            print(f'{dividend} / {divisor}: {answer}')
        
        if is_neg:
            answer = -answer
        
        MAX = 2 ** 31
        if answer > MAX - 1:
            print('positive truncate')
            return MAX - 1
        if answer < -MAX:
            print('negative truncate')
            return -MAX
        return answer

