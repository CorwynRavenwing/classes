class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        
        mod = 10 ** 9 + 7

        print(f'{len(nums)=}')
        freq = Counter(nums)
        # print(f'{freq=}')
        has_freq_GE_2 = {
            N
            for N, count in freq.items()
            if count >= 2
        }
        # print(f'{has_freq_GE_2=}')
        
        middles = {
            N
            for N in freq.keys()
            if (2 * N) in has_freq_GE_2
        }
        # print(f'{middles=}')
        endpoints = {
            2 * N
            for N in middles
        }
        # print(f'{endpoints=}')
        keep = middles | endpoints
        # print(f'{keep=}')

        # delete all nums that are irrelevant:
        nums = [
            N
            for N in nums
            if N in keep
        ]

        # print(f'{nums=}')
        print(f'{len(nums)=}')

        indexesByValue = {}
        for index, value in enumerate(nums):
            indexesByValue.setdefault(value, [])
            indexesByValue[value].append(index)
        # print(f'{indexesByValue=}')

        answer = 0
        for B in middles:
            B2 = B * 2
            B_indexes = indexesByValue[B]
            B2_indexes = indexesByValue[B2]
            print(f'{B =} {B_indexes =}')
            print(f'{B2=} {B2_indexes=}')
            LEN = len(B2_indexes)
            for B_idx in B_indexes:
                A = bisect_left(B2_indexes, B_idx)
                C_pos = A
                try:
                    if B2_indexes[C_pos] == B_idx:
                        C_pos += 1
                except IndexError:
                    # too high: just don't increment it
                    break
                C = LEN - C_pos
                prod = A * C
                # print(f'{B=} {B2=} {A=} {C=} {prod=}')
                answer += prod
                answer %= mod
                print(f'  {B_idx} {A=} {C=} {prod=}')

        return answer % mod

# NOTE: Acceptance Rate 37.9% (medium)

# NOTE: Accepted on third Run (typos)
# NOTE: Accepted on first Submit of third version (Output Exceeded; Time/Memory Exceeded)
# NOTE: Runtime 559 ms Beats 80.09%
# NOTE: Memory 37.64 MB Beats 94.69%

# NOTE: re-ran for challenge:
# NOTE: Runtime 571 ms Beats 69.65%
# NOTE: Memory 35.67 MB Beats 94.35%
