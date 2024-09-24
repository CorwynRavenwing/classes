class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:

        # SHORTCUT: instead of doing the O(N^2) work of comparing every
        # value of the two lists to each other, I'm going to precompute
        # all the prefixes of each number, in a set for easy comparison.

        def set_of_all_prefixes(arr: List[int]) -> Set[int]:
            answer = set(arr)
            print(f'answer={sorted(answer)[:10]}...')
            working = answer
            while working:
                working = {
                    N // 10
                    for N in working
                }
                working -= answer
                print(f'working={sorted(working)[:10]}...')
                answer |= working
            return answer
        
        set1 = set_of_all_prefixes(arr1)
        set2 = set_of_all_prefixes(arr2)
        print(f'set1={sorted(set1)[:10]}...')
        print(f'set2={sorted(set2)[:10]}...')
        intersect = set1 & set2
        print(f'intersect={sorted(intersect)[:10]}...')

        # SHORTCUT: number with greatest length, will be greatest number.

        M = max(intersect)
        print(f'{M=}')

        return len(str(M)) if M else 0

# NOTE: Runtime 751 ms Beats 85.80%
# NOTE: Memory 31.02 MB Beats 44.75%
