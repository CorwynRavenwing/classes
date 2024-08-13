class Solution:
    def maxStrength(self, nums: List[int]) -> int:

        # I don't know why the comments are full of people
        # doing "pick / don't pick" logic, but the list we need
        # to pick is exactly this:

        # 1. all positive numbers, as well as:
        # 2. all *pairs* of negative numbers, starting at the largest magnitude
        # 3. max(nums) if the preceeding two groups are empty
        
        # batched() comes standard in python 3.12
        # unfortunately, leetcode uses python 3.11.9 as of right now
        # using a recipe from the itertools module, found at:
        # https://docs.python.org/3/library/itertools.html#itertools-recipes
        def batched(iterable, n):
            "Batch data into lists of length n. The last batch may be shorter."
            # batched('ABCDEFG', 3) --> ABC DEF G
            it = iter(iterable)
            while True:
                batch = list(islice(it, n))
                if not batch:
                    return
                yield batch


        positives = [N for N in nums if N > 0]
        negatives = [N for N in nums if N < 0]
        negatives.sort()
        negative_pairs = [P for P in batched(negatives, 2) if len(P) == 2]
        negative_choose = [Num for Pair in negative_pairs for Num in Pair]
        print(f'{positives=}')
        print(f'{negatives=}')
        print(f'{negative_pairs=}')
        print(f'{negative_choose=}')
        choose = positives + negative_choose
        if not choose:
            print(f'Nothing chosen: returning max')
            return max(nums)
        
        return math.prod(choose)
# NOTE: Runtime 60 ms Beats 33.99%
# NOTE: Memory 16.56 MB Beats 63.37%
