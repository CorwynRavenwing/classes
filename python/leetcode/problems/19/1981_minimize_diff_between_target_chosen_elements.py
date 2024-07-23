class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:

        Sums = set()
        i = 0
        for row in mat:
            if Sums == set():
                Sums = set([0])
            nextSums = set()
            for PR in Sums:
                for TR in set(row):
                    nextSums.add(PR + TR)
            Sums = nextSums
            print(f'{i}: {Sums}')
            i += 1
        diffs = [
            abs(S - target)
            for S in Sums
        ]
        print(f'{diffs=}')
        return min(diffs)

