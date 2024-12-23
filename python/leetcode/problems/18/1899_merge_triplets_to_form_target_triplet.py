class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        (tX, tY, tZ) = target

        # filter out all triplets with any too-large values
        triplets = [
            (X, Y, Z)
            for (X, Y, Z) in triplets
            if (X <= tX) and (Y <= tY) and (Z <= tZ)
        ]
        print(f'without-too-high {triplets=}')

        # of these, look for triplets with exact match for any value
        triplets = [
            (X, Y, Z)
            for (X, Y, Z) in triplets
            if (X == tX) or (Y == tY) or (Z == tZ)
        ]
        print(f'with-exact-match {triplets=}')

        merged = list(
            map(
                max,
                zip(*triplets)
            )
        )
        print(f'{merged=}')
        print(f'{target=}')

        return (merged == target)

# NOTE: Accepted on second Run (output type mismatch)
# NOTE: Accepted on first Submit
# NOTE: Runtime 55 ms Beats 16.60%
# NOTE: Memory 55.13 MB Beats 5.65%
