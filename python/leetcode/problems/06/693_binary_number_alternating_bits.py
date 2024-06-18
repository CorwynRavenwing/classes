class Solution:
    def hasAlternatingBits(self, n: int) -> bool:

        # 3x+1 method (26 ms)

        # divide by 2, if even
        if n % 2 == 0:
            n //= 2
        
        # fail, if still even
        if n % 2 == 0:
            return False
        
        # perform 3x+1
        n = (3 * n) + 1
        # note:
        #   10101  # 1x: if bits match this pattern
        # +101010  # 2x
        #  ------
        #  111111  # 3x
        # 1000000  # 3x+1: then 3x+1 is a power of 2

        # repeat division by 2 until not even
        while n % 2 == 0:
            n //= 2
        
        # "was a power of 2" === "is now 1"
        return (n == 1)

        # original method (34 ms)
        bit = None
        prior_bit = None
        print(f"{n=}")
        while n:
            bit = n % 2
            n = n // 2
            print(f"  {bit=} {prior_bit} {n=}")
            if prior_bit is not None:
                if prior_bit == bit:
                    print(f"    FAIL")
                    return False
            prior_bit = bit
        return True

