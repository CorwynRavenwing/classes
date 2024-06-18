class Solution:
    def minCut(self, s: str) -> int:

        # we repurpose the code from 131

        def is_palindrome_naive(P: str) -> bool:
            return list(P) == list(reversed(list(P)))

        def is_palindrome(P: str) -> bool:
            for i, ch in enumerate(P):
                j = len(P) - i - 1
                if ch != P[j]:
                    return False
                if i > j:
                    return True
            
            return True
        
        def test_it(P: str):
            old = is_palindrome_naive(P)
            new = is_palindrome(P)
            if old != new:
                print(f'ERROR: {P=} {old=} {new=}')
            # else:
            #     print(f'OK: {P=} {old=} {new=}')
            return
        
        # test_it('a')
        # test_it('ab')
        # test_it('aba')
        # test_it('abba')

        # data[N] contains "minimum cuts to partition
        #   string s[:N]"
        # Which means that data[0] is "minimum cuts for the
        #   substring ENDING at index 0, i.e. the empty string"
        # The answer will be in data[len(s)]
        # data = {
        #     0: 0
        # }
        data = [None] * (len(s) + 1)
        data[0] = 0

        if is_palindrome(s):
            # shortcut
            return 0
        
        for j in range(1,len(s)+1):
            partial = None
            # test case 0 first
            if is_palindrome(s[:j]):
                data[j] = 1
                continue
            best_prior = min(data[1:j])
            # test other strings smallest to largest:
            for i in reversed(range(1,j)):
                fragment = s[i:j]
                prior = data[i]
                is_pal = is_palindrome(fragment)
                # print(f'{i=} {j=} {fragment} {is_pal} {prior=}')
                if not is_pal:
                    continue
                new_value = prior + 1
                # print(f'  {new_value=}')
                if partial is None or partial > new_value:
                    partial = new_value
                if new_value == 1:
                    # shortcut
                    break
                if prior == best_prior:
                    # shortcut
                    break
            # print(f'{partial=}')
            data[j] = partial
        
        partitions = data[len(s)]
        # print(f'{partitions=}')
        # print(f'{data=}')
        return partitions - 1

