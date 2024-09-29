class Solution:
    def integerBreak(self, n: int) -> int:
        print(f'integerBreak({n}):')
        original_n = n

        # SHORTCUT: of a set of numbers whose sum and count are known,
        # the product is maximized when the numbers are closest together.
        # e.g. for count=3 and sum=6, 2x2x2 = 8 while 1x1x4 = 4.
        # HOWEVER: for this project, the count is variable, so long as
        # you have at least 2 pieces.  for sum=6 and count=variable,
        # 2x2x2 = 8 as above but 3x3=9.  Therefore we should split into
        # as many 3's as possible, leaving no more than two 2's, and only
        # use 1's if necessary because of the "split into 2 pieces" rule
        # (e.g. 2 -> 1x1, 3 -> 2x1)
        
        if n == 2:
            print(f'  1x1')
            return 1
        if n == 3:
            print(f'  2x1')
            return 2
        
        (threes, twos) = (0, 0)
        print(f'  {n=} {threes=} {twos=}')
        nines = n // 9
        if nines:
            threes = nines * 3
            n = n % 9
        del nines
        
        while n:
            print(f'  {n=} {threes=} {twos=}')
            # this loop will be quick, because we're only counting to 9
            if n == 1:
                if threes >= 1:
                    threes -= 1
                    n += 3
                    continue
                raise Exception(f'A: Somehow we got {n=} {threes=} {twos=}')
            if n == 2:
                twos += 1
                n -= 2
                continue
            if n == 4:
                twos += 2
                n -= 4
                continue
            if n >= 3:
                threes += 1
                n -= 3
            else:
                raise Exception(f'B: Somehow we got {n=} {threes=} {twos=}')
            
        print(f'  {n=} {threes=} {twos=}')
        checksum = 3 * threes + 2 * twos
        product = 3 ** threes * 2 ** twos
        print(f'{checksum=} {product=}')
        assert original_n == checksum
        return product

# NOTE: Accepted on first Submit
# NOTE: Runtime 42 ms Beats 23.19%
# NOTE: Memory 16.76 MB Beats 10.33%
