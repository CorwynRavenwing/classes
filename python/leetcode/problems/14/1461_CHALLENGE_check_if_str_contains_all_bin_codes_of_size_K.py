class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        # NOTE: original version, producing all numbers and looking in the string for them:
        # NOTE: Time Limit Exceeded for large inputs.

        # end = (1 << k)
        # for N in range(end):
        #     binary = f'{N:0{k}b}'
        #     # print(f'{N=} {binary}')
        #     assert len(binary) == k
        #     if binary not in s:
        #         # print(f'  NO')
        #         return False
        # return True

        # NOTE: new version, checking all substrings and comparing them to the list of numbers:

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
        
        uniqueSubstrings = set()
        for startnum in range(k):
            for substring_list in batched(s[startnum:], k):
                if len(substring_list) < k:
                    continue
                substring = ''.join(substring_list)
                # print(f'{startnum}: {substring}')
                uniqueSubstrings.add(substring)
        
        print(f'{len(uniqueSubstrings)=} 2^k={(2 ** k)}')

        return len(uniqueSubstrings) == (2 ** k)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (was Output Exceeded)
# NOTE: Runtime 826 ms Beats 5.85%
# NOTE: Memory 53.24 MB Beats 51.41%
