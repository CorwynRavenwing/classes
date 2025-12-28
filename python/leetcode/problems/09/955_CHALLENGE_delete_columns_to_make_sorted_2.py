class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        print(f'MDS({strs})')

        def is_sorted(arr: List[str]) -> bool:
            return arr == sorted(arr)
        
        def delete_column(strs: List[str], i: int) -> List[str]:
            print(f'dc({strs},{i}):')
            retval = [
                S[:i] + S[i + 1:]   # ... skipping S[i]
                for S in strs
            ]
            print(f'  -> {retval}')
            return retval
        
        deletes = 0
        i = 0
        while i < len(strs[0]):
            print(f'  loop({i=},{strs})')

            if is_sorted(strs):
                print(f'  already sorted')
                return deletes
        
            leftHalf = [
                S[:i + 1]
                for S in strs
            ]
            # rightHalf = [
            #     S[i + 1:]
            #     for S in strs
            # ]

            if is_sorted(leftHalf):
                print(f'  leftHalf sorted: keep; next i')
                i += 1
                continue
            else:
                print(f'  leftHalf not sorted: delete {i}')
                # delete this column
                deletes += 1
                strs = delete_column(strs, i)
                continue
        return deletes

# NOTE: Acceptance Rate 36.4% (medium)

# NOTE: re-ran for challenge
# NOTE: Runtime 63 ms Beats 5.13%
# NOTE: Memory 17.74 MB Beats 84.62%
