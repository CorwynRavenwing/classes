class Solution:
    def lastNonEmptyString(self, s: str) -> str:

        # brute-force method:

        Alphabet = 'abcdefghijklmnopqrstuvwxyz'
        # print(f'{s=}')
        print(f'{len(s)=}')
        while s:
            prev = s
            deleted = ''
            for C in Alphabet:
                if C in s:
                    s = s.replace(C, '', 1)
                    deleted += C
            if deleted == Alphabet:
                print(f'-*')
            else:
                print(f'-{deleted}')
            # print(f'{s=}')
        
        return prev
# NOTE: times out on large (400K) inputs, works on smaller (200K) ones
