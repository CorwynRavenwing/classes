class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        print(f"{arr=}")
        S = sum(arr)
        print(f"sum={S}")
        if S % 3 != 0:
            print("  NO, not divisible by 3")
            return False
        Goal = S // 3
        print(f"{Goal=}")
        group = 1
        total = 0
        count = 0
        print(f"BEGIN GROUP {group}")
        for N in arr:
            total += N
            count += 1
            print(f"  {group} {N} {total}")
            if total == Goal:
                if group < 3:
                    group += 1
                    total = 0
                    count = 0
                    print(f"BEGIN GROUP {group}")
                else:
                    print("END GROUP?")
        print(f"END {group} {N} {total}")

        if total != Goal:
            print(f"FAIL, {total=} {Goal=}")
            return False

        if group != 3:
            print(f"FAIL, {group=}")
            return False

        if count == 0:
            print(f"NOTHING IN GROUP {group}")
            return False

        print("SUCCESS")
        return True

