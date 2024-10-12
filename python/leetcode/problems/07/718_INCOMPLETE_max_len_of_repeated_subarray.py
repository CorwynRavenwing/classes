class Solution:

    def findLength(self, nums1: List[int], nums2: List[int]) -> int:

        IndexesByValue = {}
        for N in set(nums1):
            IndexesByValue.setdefault(N, [])
            index = -1
            while True:
                try:
                    index = nums2.index(N, index + 1)
                except ValueError:
                    print(f'  no more matches')
                    break
                assert N == nums2[index]
                IndexesByValue[N].append(index)

        answer = 0
        for I, A in enumerate(nums1):
            print(f'[{I}] {A}:')
            if len(nums1) - I < answer:
                print(f'  Nums1: not enough room to matter ({len(nums1)} - {I} < {answer})')
                break
            # if A not in nums2:
            #     print(f'  (nope)')
            #     continue
            for K in IndexesByValue[A]:
                C = nums2[K]
                # print(f'  [{K=}] {C}')
                if len(nums2) - K < answer:
                    # print(f'  Nums2: not enough room to matter ({len(nums2)} - {K} < {answer})')
                    break
                length = 1
                # print(f'  {length=}')
                while True:
                    answer = max(answer, length)
                    length += 1
                    J = I + length - 1
                    L = K + length - 1
                    try:
                        B = nums1[J]
                        D = nums2[L]
                    except IndexError:
                        print(f'  (out of range)')
                        break
                    if B != D:
                        # print(f'  {length=} {B}/{D} (NO)')
                        break
                    # else:
                    #     # print(f'  {length=} {B}/{D} (yes)')

        return answer

# NOTE: Time Limit Exceeded for large inputs
