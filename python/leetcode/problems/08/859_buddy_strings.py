from collections import Counter

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        
        if s == goal:
            sCount = Counter(s)
            for letter, count in sCount.items():
                if count >= 2:
                    print(f"Equal: '{letter}'={count}")
                    return True
            print("Equal: nope")
            return False
        else:
            sCount = Counter(s)
            gCount = Counter(goal)
            sSort = sorted(sCount.items())
            gSort = sorted(gCount.items())
            if sSort != gSort:
                print("Diff: counters are different")
                print(f"{sSort=}")
                print(f"{gSort=}")
                return False
            diff = 0
            for i, sVal in enumerate(s):
                gVal = goal[i]
                if sVal != gVal:
                    diff += 1
                    print(f"diff {diff} {i} '{sVal}'|'{gVal}'")
            if diff == 2:
                print(f"diff yes {diff}")
                return True
            else:
                print(f"diff no {diff}")
                return False

