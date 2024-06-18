class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        def my_square_root(x: int) -> int:
            if not x:
                return 0

            # print(f"#{x=}")
            digits = tuple(str(x))
            # print(f"#{digits=}")
            l_digits = len(digits)
            # print(f"#{l_digits=}")
            e_digits = (l_digits + 1) // 2
            # print(f"#{e_digits=}")
            LB = 10 ** (e_digits - 1)
            UB = (10 ** e_digits)
            # print(f"#{LB=} {UB=}")
            # print(f"#{LB*LB=} <= {x=} <= {UB*UB=}")
            assert LB*LB <= x <= UB*UB
            while LB + 1 < UB:
                MID = (LB + UB) // 2
                # print(f"#  {LB=} {MID=} {UB=}")
                test = MID*MID
                if test > x:
                    UB = MID
                elif test < x:
                    LB = MID
                elif test == x:
                    # print(f"found!  {MID=}")
                    return MID
                else:
                    assert Exception("(test <=> x) is false")
            # print(f"#{LB*LB=} <= {x=} <= {UB*UB=}")
            assert LB*LB <= x <= UB*UB
            # print(f"#{LB=} {UB=}")
            assert LB + 1 == UB
            return LB
            
        root = my_square_root(num)
        check = root * root
        # print(f"{root=} {num=} {check=}")
        return (num == check)

