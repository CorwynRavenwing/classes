class Solution:

    # SHORTCUT: instead of taking each value, performing every possible
    #   character swap on it, and then doing that *again*, and comparing
    #   all those values against the other values:
    # we instead perform every possible swap on each value *once*,
    #   store them as a set, and check the intersection of each pair of sets.

    # we borrow some code from #3265:

    def join(self, L: List[str]) -> str:
        # print(f'join({L})')
        return ''.join(L)

    def swapped(self, L: List[str], i: int, j: int) -> List[str]:
        assert i < j
        preI = L[:i]        # everything before index i
        I = tuple(L[i])     # item at index i
        ItoJ = L[i+1:j]     # everything after index i and before index j
        J = tuple(L[j])     # item at index j
        postJ = L[j+1:]     # everything after index j

        S = (preI + J + ItoJ + I + postJ)
        
        return tuple(S)

    def almostEqualSet(self, s: str) -> Set[str]:
        print(f'AES({s})')
        L = tuple(s)

        answer = {s}        # start with s itself

        for i, A in enumerate(L):
            # print(f'    {i=} {A=}')
            for j in range(i + 1, len(L)):
                B = L[j]
                # print(f'      {j=} {B=}')
                if A == B:
                    continue
                S = self.swapped(L, i, j)
                # print(f'        {S=}')
                answer.add(
                    self.join(S)
                )

        print(f'{answer=}')
        return answer

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
            EqualitySet = [
                self.almostEqualSet(NSi)
                for (Ni, NSi) in Numbers
            ]
            for i, NTi in enumerate(Numbers):
                (Ni, NSi) = NTi
                countI = numCounts[Ni]
                esI = EqualitySet[i]
                # print(f'{i=} {countI=} {Ni=}')
                for j in range(i+1, len(Numbers)):
                    NTj = Numbers[j]
                    (Nj, NSj) = NTj
                    countJ = numCounts[Nj]
                    esJ = EqualitySet[j]
                    # print(f'  {j=} {countJ=} {Nj=}')
                    if esI & esJ:
                        # set intersection exists: they are "almost equal"
                        product = countI * countJ
                        # print(f'    B: {countI} * {countJ} = {product}')
                        answer += product
                    # else:
                    #     # print(f'    b: no; same bucket but not Almost Equal')
        
        return answer

# NOTE: we reused some of the code from Version 1, but the
#       requirements were different enough that a lot had to change.
# NOTE: Runtime 6650 ms Beats 31.74%
# NOTE: Memory 28.68 MB Beats 28.18%
