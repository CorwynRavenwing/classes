class Solution:
    def distMoney(self, money: int, children: int) -> int:

        print(f"{money=} {children=}")
        distrib = [1] * children
        moneyLeft = money - sum(distrib)
        print(f"{moneyLeft} {distrib}")
        if moneyLeft < 0:
            print("more children than money")
            return -1
        for index, dMoney in enumerate(distrib):
            # assert dMoney == 1
            desired = (8 - dMoney)
            if moneyLeft >= desired:
                moneyLeft -= desired
                distrib[index] += desired
                print(f"{moneyLeft} {distrib}")
        if moneyLeft:
            distrib[-1] += moneyLeft
            moneyLeft -= moneyLeft
            print(f"{moneyLeft} {distrib}")
        if distrib[-1] == 4:
            if distrib[-2] == 8:
                distrib[-1] -= 1
                distrib[0] += 1
            else:
                distrib[-1] -= 1
                distrib[-2] += 1
            print(f"{moneyLeft} {distrib}")
        assert sum(distrib) == money
        if 4 in distrib:
            print("cannot not give 4 dollars")
            print("  do we have $4 and 1 child?")
            return -1
        eights = [
            D
            for D in distrib
            if D == 8
        ]
        return len(eights)

