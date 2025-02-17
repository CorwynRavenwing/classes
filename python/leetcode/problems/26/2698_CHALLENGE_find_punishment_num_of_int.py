class Solution:
    def punishmentNumber(self, n: int) -> int:
        
        Square = lambda x: (x * x)

        # @cache    # no: caching makes it worse
        def can_be_partitioned(numStr: str, target: int) -> bool:
            # print(f'CBP({numStr},{target})')
            if int(numStr) == target:
                # print(f'  A: yes')
                return True
            for index in range(1, len(numStr)):
                left = numStr[:index]
                right = numStr[index:]
                # print(f'  B: split "{left}|{right}"')
                leftVal = int(left)
                if leftVal > target:
                    # print(f'    B: No')
                    continue
                if can_be_partitioned(right, target - leftVal):
                    # print(f'  C: split "{left}|{right}" YES')
                    return True
            # print(f'  D: all splits done: NO')
            return False
        
        # @cache    # no: caching makes it worse
        def is_punishing(i: int) -> bool:
            i2 = Square(i)
            return can_be_partitioned(str(i2), i)
        
        punishing = [
            Square(i)
            for i in range(1, n + 1)
            if is_punishing(i)
        ]
        print(f'{punishing=}')
        return sum(punishing)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 674 ms Beats 71.13%
# NOTE: Memory 17.78 MB Beats 68.75%
