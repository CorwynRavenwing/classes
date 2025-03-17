class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        
        # we borrow some code from #3355:
 
        first = nums[0]
        last = nums[-1]
        original_diffs = [first] + [
            B - A
            for (A, B) in pairwise(nums)
        ] + [-last]
        # print(f'[start] {original_diffs=}')

        def apply_query_K(diffs_before: List[int], k: int) -> List[int]:
            diffs_after = list(diffs_before)

            (Li, Ri, Vali) = queries[k - 1]
            # print(f'  DaKQ({k}) Q[{k-1}]: {queries[k - 1]}')
            diffs_after[Li] -= Vali
            diffs_after[Ri + 1] += Vali

            # print(f'  DaKQ({k}) => {diffs_after}')
            return tuple(diffs_after)

        # @cache    # nope: rolling our own due to memory limit
        diffs_cache = [None] * (len(queries) + 1)
        def diffs_after_K_queries(k: int) -> List[int]:
            if diffs_cache[k] is not None:
                return diffs_cache[k]
            # print(f'DaKQ({k})')
            nonlocal original_diffs

            if k == 0:
                answer = tuple(original_diffs)
                diffs_cache[k] = answer
                return answer
            
            local_diffs = diffs_after_K_queries(k - 1)
            local_diffs = apply_query_K(local_diffs, k)
            diffs_cache[k] = local_diffs
            return local_diffs
        
        def is_zero_array(diff_array: List[int]) -> bool:
            partialSum = tuple(accumulate(diff_array))
            # print(f'    {partialSum=}')
            return (max(partialSum) <= 0)

        def zero_array_after_Target_queries(target: int) -> bool:
            # print(f'zAaTq({target}):')
            # if target == 0:
            #     print(f'zAaTq({target}): (0: false)')
            #     return False
            diff_array = diffs_after_K_queries(target)
            # print(f'zAaTq({target}): {diff_array=}')
            answer = is_zero_array(diff_array)
            # print(f'zAaTq({target}): -> {answer}')
            return answer

        L = 0
        left = zero_array_after_Target_queries(L)
        if left:
            print(f'Strange, {L=} is true')
            return L
        R = len(queries)
        right = zero_array_after_Target_queries(R)
        if not right:
            print(f'Strange, {R=} is false')
            return -1
        print(f'[{L},{R}] ({left},{right})')
        while L + 1 < R:
            M = (L + R) // 2
            mid = zero_array_after_Target_queries(M)
            print(f'[{L},{M},{R}] ({left},{mid},{right})')
            if mid:
                print(f'  True: replace Right')
                (R, right) = (M, mid)
            else:
                print(f'  False: replace Left')
                (L, left) = (M, mid)

        print(f'[{L},{R}] ({left},{right})')
        # R is now the lowest possible True value
        return R

# NOTE: Acceptance Rate 38.0% (medium)

# NOTE: without cache: Time Exceeded
# NOTE: with cache: Memory Exceeded
# NOTE: trying a different method
