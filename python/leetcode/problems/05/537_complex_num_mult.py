class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:

        def strToComplex(num: str) -> Tuple[int,int]:
            assert num[-1] == 'i'
            num = num[:-1]  # throw away the "i"
            (A,B) = num.split('+')
            return tuple(map(int,(A,B)))
        
        C1 = strToComplex(num1)
        C2 = strToComplex(num2)
        (r1, i1) = C1
        (r2, i2) = C2
        r3 = (r1 * r2) - (i1 * i2)
        i3 = (r1 * i2) + (r2 * i1)
        C3 = f'{r3}+{i3}i'
        return C3

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 28 ms Beats 92.74%
# NOTE: Memory 16.71 MB Beats 6.58%
