class Solution:
    def isPossible(self, nums: List[int]) -> bool:

        # We can't just greedily grab every matching sequence,
        # as Example 1 [1,2,3,3,4,5] demonstrates.
        # Correct answer needs [1,2,3],[3,4,5]: Success,
        # whereas Greedy chooses [1,2,3,4,5],[3]: Fail.

        # Instead, we need to keep track of all the sequences
        # currently in play, and possibly add more values to them
        # as we process each number.

        new_sequences = []
        old_sequences = []
        for N in nums:
            found = False
            if not found:
                for S in new_sequences:
                    lastNum = S[-1]
                    if lastNum + 1 == N:
                        # elipsis = ("..." if (len(S) > 5) else "")
                        # print(f'Append {N} to new sequence {S[:5]}{elipsis}')
                        S.append(N)
                        found = True
                        break
            if not found:
                for S in old_sequences:
                    lastNum = S[-1]
                    if lastNum + 1 == N:
                        # elipsis = ("..." if (len(S) > 5) else "")
                        # print(f'Append {N} to old sequence {S[:5]}{elipsis}')
                        S.append(N)
                        found = True
                        break
            if not found:
                # print(f'Create new sequence [{N}]')
                new_sequences.append([N])
            new_sequences.sort(
                key=len
            )
            while new_sequences and len(new_sequences[-1]) >= 3:
                S = new_sequences.pop(-1)
                elipsis = ("..." if (len(S) > 5) else "")
                # print(f'Move sequence {S[:5]}{elipsis} to "old" list')
                old_sequences.append(S)
        print(f'{old_sequences=}')
        print(f'{new_sequences=}')
        
        return (not new_sequences)

# NOTE: Approved on second Submit (first was Output Exceeded)
# NOTE: Runtime 8017 ms Beats 5.05%
# NOTE: Memory 18.28 MB Beats 18.32%
