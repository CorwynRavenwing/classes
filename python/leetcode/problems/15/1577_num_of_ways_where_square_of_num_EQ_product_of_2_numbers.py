class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def squares(nums: List[int]) -> List[int]:
            return [
                N * N
                for N in nums
            ]

        def check_for_triplets(squares: List[int], factors: List[int]) -> int:
            # print(f'CFT({squares},{factors})')
            cSquares = Counter(squares)
            cFactors = Counter(factors)
            print(f'CFT({cSquares},{cFactors})')
            answer = 0
            for sq, sqNum in cSquares.items():
                print(f'  {sq}:{sqNum}')
                for F, fNum in cFactors.items():
                    print(f'    {F}:{fNum}')
                    if sq % F != 0:
                        print(f'      SKIP (not a factor)')
                        continue
                    Q = sq // F
                    if Q not in cFactors:
                        print(f'      skip (no {Q})')
                        continue
                    if Q < F:
                        print(f'      Skip (dup)')
                        continue
                    elif Q == F:
                        print(f'      (root)')
                        if fNum < 2:
                            print(f'        <2 copies')
                            pass
                        else:
                            qPairs = fNum * (fNum - 1) // 2     # === N choose 2
                            A = sqNum * qPairs
                            print(f'        +{A=}')
                            answer += A
                    else:
                        # Q > F, normal case
                        qNum = cFactors[Q]
                        print(f'      {Q}:{qNum}')
                        qPairs = fNum * qNum
                        A = sqNum * qPairs
                        print(f'        +{A=}')
                        answer += A
            return answer

        return sum([
            check_for_triplets(squares(nums1), nums2),
            check_for_triplets(squares(nums2), nums1),
        ])

