class Solution:
    def minimizeStringValue(self, s: str) -> str:

        # SHORTCUT: the order of the characters is irrelevant for
        #   the cost.  The first copy of each character is free,
        #   and the remainder follow the triangle relation N * (N+1) / 2.
        #   Therefore for a count of N, the total is actually (N-1) * N / 2.

        if '?' not in s:
            return s
        
        Alphabet = 'abcdefghijklmnopqrstuvwxyz'
        
        counts = Counter(s)
        # print(f'{counts=}')
        for L in Alphabet:
            counts.setdefault(L, 0)
        # print(f'{counts=}')
        queries = counts['?']
        del counts['?']
        print(f'{counts=}')
        additions = []
        for _ in range(queries):
            CMC = counts.most_common()
            CMC.sort(
                key=lambda x: (x[1], x[0])  # count ASC then letter ASC
            )
            letter, count = CMC[0]
            print(f'Replace {_+1}/{queries}: {letter},{count}')
            additions.append(letter)
            counts[letter] += 1         # change the count for this letter
        
        print(f'{additions=}')
        for C in sorted(additions):
            s = s.replace('?', C, 1)

        return s

# NOTE: Runtime 3544 ms Beats 5.29%
# NOTE: Memory 18.78 MB Beats 51.85%
