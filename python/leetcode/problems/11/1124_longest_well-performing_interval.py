class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        
        # SHORTCUT 1 from hint: use 1,-1
        # for Tiring/nonTiring
        Tiring = tuple([
            (1 if work > 8 else -1)
            for work in hours
        ])
        # print(f'{Tiring=}')

        ACC = lambda x: (0,) + tuple(accumulate(x))

        # SHORTCUT 2: "range with T > N"
        # === "range with sum > 0"
        sumT = ACC(Tiring)
        # print(f'{sumT=}')

        # SHORTCUT 3: "sumT[j] - sumT[i]"
        # === "sum of range [i:j]"

        # SHORTCUT 4: we seek the largest span
        # where i < j and sumT[i] < sumT[j]

        # SHORTCUT 5: for each sumT value,
        # new_i = minimum index for that value,
        # i = min(all new_i values)
        # j = maximum index for value + 1,
        # length = j - i

        IndexesByValue = {}
        for index, value in enumerate(sumT):
            IndexesByValue.setdefault(value, [])
            IndexesByValue[value].append(index)
            # these indexes will be auto-sorted
        print(f'{IndexesByValue=}')

        longest = 0
        min_i_so_far = float('+inf')
        for value, indexList in sorted(IndexesByValue.items()):
            new_i = indexList[0]   # the lowest
            new_j = indexList[-1]  # the highest
            i = min_i_so_far
            j = new_j
            print(f'{value=} {i=} {j=}')
            if i > j:
                print(f'  -> Negative length')
            else:
                L = j - i
                print(f'  -> {L=}')
                longest = max(longest, L)
            min_i_so_far = min(min_i_so_far, new_i)

        return longest

# NOTE: Works after using one hint and ignoring a second one
# NOTE: Runtime 55 ms Beats 5.75%
# NOTE: Memory 18.86 MB Beats 5.88%
