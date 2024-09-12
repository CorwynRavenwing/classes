class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        
        # we borrow some code from #3201:

        mods = [N % k for N in nums]
        print(f'{mods[:10]=}')

        counts = Counter(mods)
        print(f'counts{tuple(counts.items())[:10]}')

        cases = []

        # case group 1: all the same
        for mod, count in counts.items():
            cases.append(count)
            # print(f'case group 1: all {mod} = {count}')
        
        best_case_1 = max(cases, default=0)
        print(f'{best_case_1=}')
        cases = []

        # case group 2: any pair, alternating
        for first, firstCount in counts.items():
            for second, secondCount in counts.items():
                # print(f'Try {first}, {second}:')
                if first == second:
                    # print(f'  No: same')
                    continue
                if min(firstCount, secondCount) * 2 + 1 <= best_case_1:
                    # series will be alternating, e.g. [1 2 1 2 1]
                    # our limiting reagent is the 2's (minimum count):
                    # any extra 1's will be unused
                    # print(f'  No: {firstCount},{secondCount} cant beat best case 1')
                    continue

                prior = first
                index = mods.index(prior)
                this_case = 1
                # print(f'{this_case=} [{index}]{prior}')
                while True:
                    next = second if (prior == first) else first    # 1st->2nd, 2nd->1st
                    try:
                        index = mods.index(next, index + 1)
                    except ValueError:
                        break
                    prior = mods[index]
                    this_case += 1
                    # print(f'{this_case=} [{index}]{prior}')
                cases.append(this_case)
                # print(f'case group 2: {first},{second} = {this_case}')
        best_case_2 = max(cases, default=0)
        print(f'{best_case_2=}')

        return max(best_case_1, best_case_2)

# NOTE: Runtime 1433 ms Beats 75.40%
# NOTE: Memory 17.00 MB Beats 80.99%
