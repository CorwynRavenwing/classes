class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        w1 = s1.split(' ')
        w2 = s2.split(' ')
        print(f'{w1=}')
        print(f'{w2=}')
        c1 = Counter(w1)
        c2 = Counter(w2)
        print(f'{c1=}')
        print(f'{c2=}')
        answer = [
            W
            for W, count in c1.items()
            if (count == 1) # only found once in this sentence
            if c2[W] == 0   # never found in other sentence
        ] + [
            W
            for W, count in c2.items()
            if (count == 1) # only found once in this sentence
            if c1[W] == 0   # never found in other sentence
        ]

        return answer

# NOTE: Accepted on first Submit
# NOTE: Runtime 32 ms Beats 78.21%
# NOTE: Memory 16.66 MB Beats 5.76%
