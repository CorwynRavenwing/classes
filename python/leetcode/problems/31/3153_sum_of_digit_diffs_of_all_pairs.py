class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:

        # SHORTCUT: "sum of count of digits in same place that are different,
        # across all pairs (of same-sized numbers)"
        # === "some_function_of(count_of_different_numbers_per_digit)", summed by digit

        # DECR = lambda x: x - 1

        # def Triangle(X: int) -> int:
        #     return (X) * (X + 1) // 2

        def sum_of_products(counts: List[int]) -> int:
            total = sum(counts)
            products = [
                C * (total - C)
                for C in counts
            ]
            print(f'sum_of_products({counts})')
            print(f'  {total=}')
            print(f'  {products=}')
            answer = sum(products) // 2     # b/c each pair was counted twice
            print(f'  {answer=}')
            return answer

        def sum_of_counter(counter: Counter) -> int:
            return sum_of_products(counter.values())

        numStrs = tuple(map(str, nums))
        # print(f'{numStrs=}')
        digits = tuple(zip(*numStrs))
        # print(f'{digits=}')
        counts = tuple(map(Counter, digits))
        print(f'{counts=}')
        counter_sums = tuple(map(sum_of_counter, counts))
        print(f'{counter_sums=}')
        
        return sum(counter_sums)

# NOTE: Accepted on second Submit (first was an Output Exceeded)
# NOTE: Runtime 969 ms Beats 87.90%
# NOTE: Memory 43.36 MB Beats 5.34%
