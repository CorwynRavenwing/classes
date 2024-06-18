from collections import Counter

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        print(f"{deck=}")
        cards = Counter(deck)
        print(f"{cards=}")
        if len(cards) == 1:
            print(f"all cards are the same")
            if len(deck) > 1:
                print("  1 group")
                return True
            else:
                print("  only 1 card")
                return False
        groups = cards.values()
        print(f"{groups=}")
        if 1 in groups:
            print(f"a card with 1 copy: impossible")
            return False
        minSize = 2            # can't have groups of size 1
        maxSize = min(groups)  # only have so many of this card
        print(f"  {maxSize}")
        for size in range(2, maxSize + 1):
            print(f"    {size}?")
            divides = [
                x % size == 0
                for x in groups
            ]
            print(f"      {divides}")
            if False not in divides:
                print("      WORKS!")
                return True

        return False

