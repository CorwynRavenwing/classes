class Solution:

    def Add(self, A: int, B: int) -> int:
        print(f'Add({A},{B})')
        # if not A: return B
        # if not B: return A
        #  001010101 A (85)
        # +000010010 B (18)
        # ==========
        #  001000111 A ^ B          Xor gives "sum without carry"
        XOR = A ^ B
        #  000010000 A & B          And gives "carry of this column"
        #  000100000 (A & B) << 1   And+shift gives "carry in proper column"
        CARRY = (A & B) << 1
        # you now need to add (sum without carry) to (carry)
        # continue until carry === 0
        #  001000111 (sum without)
        #  000100000 (carry)
        #  001100111 ANSWER (103)
        if not CARRY: return XOR
        return self.Add(XOR, CARRY)

    def Sub(self, A: int, B: int) -> int:
        print(f'Sub({A},{B})')
        #  001100111 A
        # -000010010 B
        # ==========
        #  001110101 A ^ B          Xor gives "diff without borrow"
        XOR = A ^ B
        #  000010000 ~A & B         (Not A) And (B) gives "borrow of this column"
        #  000100000 (~A & B) << 1  ((Not A) And (B))+shift gives "borrow in proper column"
        BORROW = (~A & B) << 1
        # you now need to subtract (borrow) from (diff without borrow)
        # continue until borrow === 0
        #  001110101 (diff without)
        #  000100000 (borrow)
        #  001010101 ANSWER
        if not BORROW: return XOR
        return self.Sub(XOR, BORROW)

    def getSum(self, a: int, b: int) -> int:
        print(f'getSum({a},{b})')

        # case 0: either is zero
        if not a: return b
        if not b: return a

        A_is_negative = (a < 0)     # these exclude the middle "== 0"
        B_is_negative = (b < 0)     # b/c that's impossible, since
        A_is_positive = (a > 0)     # if either were zero, we would 
        B_is_positive = (b > 0)     # have returned a or b above ^^^

        abs_A = abs(a)
        abs_B = abs(b)

        A_is_bigger = abs_A >= abs_B
        B_is_bigger = abs_A <= abs_B
        
        negOne = (
            a // abs_A if A_is_negative
            else
            b // abs_B if B_is_negative
            else
            None    # it's irrelevant b/c we won't need it
        )

        # case 1: both positive
        if (A_is_positive) and (B_is_positive):
            return self.Add(abs_A, abs_B)

        # case 2: both negative
        # take abs() of both sides
        # add using case 1
        if (A_is_negative) and (B_is_negative):
            total = self.Add(abs_A, abs_B)
            # make result negative
            return negOne * total

        # case 3: one negative, one positive, larger one is positive
        # get abs() of negative one
        # perform subtraction of large - small
        if (B_is_negative and A_is_bigger):
            total = self.Sub(abs_A, abs_B)
            return total
        if (A_is_negative and B_is_bigger):
            total = self.Sub(abs_B, abs_A)
            return total

        # case 4: one negative, one positive, larger one is negative
        # get abs() of negative one
        # subtract using case 3
        if (A_is_negative and A_is_bigger):
            total = self.Sub(abs_A, abs_B)
        if (B_is_negative and B_is_bigger):
            total = self.Sub(abs_B, abs_A)
        # make result negative
        return negOne * total

# NOTE: Accepted on first Submit
# NOTE: Runtime 36 ms Beats 44.83%
# NOTE: Memory 16.60 MB Beats 18.74%
