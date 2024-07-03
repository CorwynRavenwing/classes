class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:

        if len(nums) == 2:
            # short-circuit answer for trivial case
            return 2
        
        bestSequencesAtIndex = [None] * len(nums)
        # will be an array of:
        # {
        #     diff: bestLength
        # }
        indexesOfOpenSequences = {
            # nextVal: [index, ...]
        }

        for i, N in enumerate(nums):
            print(f'{i=} {N=}')
            if i == 0:
                continue
            prior = set(nums[:i])
            print(f'  {prior=}')
            bestSequencesAtIndex[i] = {}
            nextValArray = []
            for Nprior in prior:
                diff = N - Nprior
                nextVal = N + diff
                nextValArray.append(nextVal)
                bestSequencesAtIndex[i].setdefault(diff, 2)

            if N not in indexesOfOpenSequences:
                # shortcut: skip next section if unnecessary
                continue
            
            for index in indexesOfOpenSequences[N]:
                N_index = nums[index]
                S_index = bestSequencesAtIndex[index]



            for nextVal in nextValArray:
                indexesOfOpenSequences.setdefault(nextVal, [])
                indexesOfOpenSequences.[nextVal].append(i)

        return -99999
        
        singletons = []
        sequences = []
        for N in nums:
            new_singletons = []
            new_sequences = []
            
            # 1. always allow a new singleton starting here
            # unless we already have this singleton available
            if N not in singletons:
                new_singletons.append(N)

            # 2. each former singleton -> create a new 2-item sequence
            for S in singletons:
                diff = N - S
                new_sequences.append(
                    (2, diff, N + diff)
                )

            # 3. try all former sequences for a match
            for S in sequences:
                (length, diff, nextVal) = S
                if nextVal == N:
                    # match: replace this sequence with the next-larger version
                    new_sequences.append(
                        (length + 1, diff, N + diff)
                    )
                else:
                    # not a match: keep this sequence for later
                    new_sequences.append(S)
            singletons.extend(new_singletons)   # ADD these
            sequences = new_sequences           # REPLACE these
        lengths = [
            length
            for (length, diff, nextVal) in sequences
        ]
        maxLen = max(lengths)
        return maxLen

