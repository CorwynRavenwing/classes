class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        max_value = int(sqrt(c))
        relevant_squares = [
            a * a
            for a in range(max_value + 1)
        ]
        halfway = c // 2
        index_a = bisect.bisect_right(relevant_squares, halfway)
        index_b = bisect.bisect_left(relevant_squares, halfway)
        relevant_A = relevant_squares[:index_a]
        relevant_B = relevant_squares[index_b:]
        # print(f'{relevant_A=}')
        # print(f'{relevant_B=}')
        for a in relevant_A:
            b = c - a
            # version with "IN": 2524 ms
            # version with "bisect": 55 ms
            # 46 times faster !!!
            index_b = bisect.bisect_left(relevant_B, b)
            if index_b < len(relevant_B) and relevant_B[index_b] == b:
            # if b in relevant_B:
                print(f'{a} + {b} = {c}!')
                return True
            # if a > b:
            #     print(f'{a} > {b}')
            #     break
        return False

