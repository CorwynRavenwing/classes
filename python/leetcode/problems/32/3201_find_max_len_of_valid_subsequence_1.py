class Solution:
    def maximumLength(self, nums: List[int]) -> int:

        mods = [N % 2 for N in nums]
        print(f'{mods=}')

        counts = Counter(mods)
        print(f'{counts=}')

        # case 1: all zeros
        case_1 = counts[0]
        print(f'{case_1=}')

        # case 2: all ones
        case_2 = counts[1]
        print(f'{case_2=}')

        # case 3: alternating 0 and 1
        # note; can start with either one
        index = 0
        prior = mods[index]
        case_3 = 1
        # print(f'{case_3=} [{index}]{prior}')
        while True:
            next = (prior + 1) % 2  # 0->1 and 1->0
            try:
                index = mods.index(next, index + 1)
            except ValueError:
                break
            prior = mods[index]
            case_3 += 1
            # print(f'{case_3=} [{index}]{prior}')
        print(f'{case_3=}')

        return max(case_1, case_2, case_3)

# NOTE: Accepted on first Submit
# NOTE: Runtime 643 ms Beats 36.60%
# NOTE: Memory 39.86 MB Beats 14.77%
