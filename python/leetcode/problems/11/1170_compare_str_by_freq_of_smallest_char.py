class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        def f(word: str) -> int:
            C = Counter(word)
            counts = sorted(C.items())
            (letter, count) = counts.pop(0)
            return count
        
        f_words = tuple(sorted([
            f(word)
            for word in words
        ]))
        
        print(f'{f_words=}')
        len_words = len(words)

        def doQuery(Q: List[int]) -> int:
            f_Q = f(Q)
            print(f'{Q=} {f_Q=}')
            index = bisect_right(f_words, f_Q)
            print(f'  {index=}')
            return len_words - index

        return [
            doQuery(Q)
            for Q in queries
        ]

# NOTE: Accepted on first Submit
# NOTE: Runtime 33 ms Beats 38.79%
# NOTE: Memory 17.65 MB Beats 6.65%
