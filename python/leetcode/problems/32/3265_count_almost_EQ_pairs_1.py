class Solution:

    # we borrow some code from #1790:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        if s1 == s2:
            # nothing to change: swap char 0 with itself
            return True
        
        pairs = tuple(zip(s1, s2))
        # print(f'{pairs}')
        differences = tuple(
            (A, B)
            for (A, B) in pairs
            if A != B
        )
        # print(f'{differences}')
        if len(differences) != 2:
            return False
        
        (D1, D2) = differences
        # (D1a, D1b) = D1
        # (D2a, D2b) = D2
        D2r = tuple(reversed(D2))
        # print(f"{D1a}/{D2b} {D1b}/{D2a}")
        return D1 == D2r

    def countPairs(self, nums: List[int]) -> int:

        answer = 0

        # (A) deal with all numbers that are *actually* equal:

        numCounts = Counter(nums)
        print(f'{numCounts=}')

        for N, count in numCounts.most_common():
            # sort by count descending
            if count == 1:
                # all other counts will also be 1
                break
            triangle = count * (count - 1) // 2     # == count choose 2
            print(f'A: {N} * {count}: {triangle}')
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
        print(f'{buckets=}')
        buckets = {
            Bucket: Numbers
            for Bucket, Numbers in buckets.items()
            if len(Numbers) > 1
        }
        print(f'{buckets=}')

        for Bucket, Numbers in buckets.items():
            Numbers = tuple(Numbers)    # need to keep their order during this work
            for i, NTi in enumerate(Numbers):
                (Ni, NSi) = NTi
                countI = numCounts[Ni]
                print(f'{i=} {countI=} {NTi=}')
                for j in range(i+1, len(Numbers)):
                    NTj = Numbers[j]
                    (Nj, NSj) = NTj
                    countJ = numCounts[Nj]
                    print(f'  {j=} {countJ=} {NTj=}')
                    if self.areAlmostEqual(NSi, NSj):
                        product = countI * countJ
                        print(f'    B: {countI} * {countJ} = {product}')
                        answer += product
                    else:
                        print(f'    b: no; same bucket but not Almost Equal')
        
        return answer

# NOTE: Accepted on first Submit
# NOTE: Runtime 114 ms Beats 94.97%
# NOTE: Memory 17.58 MB Beats 5.23%
