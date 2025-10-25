class Solution:
    def totalMoney(self, n: int) -> int:
        
        def bank_amounts_gen(n: int) -> List[int]:
            day = 0
            monday_value = 0
            value = 0
            for d in range(n):
                if day == 0:
                    value = monday_value + 1
                    monday_value = value
                else:
                    value += 1
                day += 1
                day %= 7
                print(f'{d}: {day} {value} {monday_value}')
                yield value
        
        return sum(bank_amounts_gen(n))

# NOTE: Acceptance Rate 79.2% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 24 ms Beats 6.56%
# NOTE: Memory 17.82 MB Beats 37.64%
