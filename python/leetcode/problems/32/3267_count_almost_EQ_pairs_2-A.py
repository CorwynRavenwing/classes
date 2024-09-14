class Solution:
        # we borrow some code from #3265:

    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # print(f'AAE({s1},{s2}):')

        if s1 == s2:
            # nothing to change
            return True
        
        pairs = tuple(map(sorted, zip(s1, s2)))
        # print(f'{pairs}')
        differences = tuple(
            (A, B)
            for (A, B) in pairs
            if A != B
        )
        if len(differences) > 4:
            return False
        
        # print(f'  {differences=}')
        L = len(differences)
        if L == 2:
            (D1, D2) = differences
            return D1 == D2
        elif L == 3:
            # three swaps must be correct
            return True
        elif L == 4:
            (D1, D2, D3, D4) = sorted(differences)
            # two swaps, not a scramble of four letters
            return (D1 == D2) and (D3 == D4)

    def countPairs(self, nums: List[int]) -> int:

        answer = 0

        # (A) deal with all numbers that are *actually* equal:

        numCounts = Counter(nums)
        # print(f'{numCounts=}')

        for N, count in numCounts.most_common():
            # sort by count descending
            if count == 1:
                # all other counts will also be 1
                break
            triangle = count * (count - 1) // 2     # == count choose 2
            # print(f'A: {N} * {count}: {triangle}')
            answer += triangle
        
        # (B) bucket up groups of numbers that share digits:

        buckets = {}
        maxNum = max(numCounts.keys())
        width = len(str(maxNum))
        for N in numCounts.keys():
            nStr = f'{N:0{width}}'
            # print(f'{nStr=}')
            Bucket = ''.join(sorted(nStr))
            # print(f'{Bucket=}')
            buckets.setdefault(Bucket, set())
            buckets[Bucket].add((N, nStr))
        # print(f'{buckets=}')
        buckets = {
            Bucket: Numbers
            for Bucket, Numbers in buckets.items()
            if len(Numbers) > 1
        }
        # print(f'{buckets=}')

        for Bucket, Numbers in buckets.items():
            Numbers = tuple(Numbers)    # need to keep their order during this work
            for i, NTi in enumerate(Numbers):
                (Ni, NSi) = NTi
                countI = numCounts[Ni]
                # print(f'{i=} {countI=} {Ni=}')
                for j in range(i+1, len(Numbers)):
                    NTj = Numbers[j]
                    (Nj, NSj) = NTj
                    countJ = numCounts[Nj]
                    # print(f'  {j=} {countJ=} {Nj=}')
                    if self.areAlmostEqual(NSi, NSj):
                        product = countI * countJ
                        # print(f'    B: {countI} * {countJ} = {product}')
                        answer += product
                    # else:
                    #     # print(f'    b: no; same bucket but not Almost Equal')
        
        return answer

# NOTE: works for reasonable-sized inputs, timeout for huge inputs
