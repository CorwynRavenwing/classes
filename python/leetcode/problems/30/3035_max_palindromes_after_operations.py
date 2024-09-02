class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:

        lengths = tuple(map(len, words))
        print(f'{lengths=}')

        counts = Counter([
            letter
            for word in words
            for letter in word
        ])
        print(f'{counts=}')

        pairs = sum([
            count // 2
            for item, count in counts.items()
        ])
        print(f'{pairs=}')

        answer = 0
        for L in sorted(lengths):
            print(f'{L=}')
            half = L // 2
            if half <= pairs:
                print(f'  Consume {half} pairs for 1 length-{L} word')
                pairs -= half
                answer += 1
            else:
                print(f'  Length-{L} word ({half=}) is too long: only have {pairs=} left')
        
        return answer

# NOTE: Accepted on first Submit
# NOTE: Runtime 126 ms Beats 67.16%
# NOTE: Memory 18.49 MB Beats 5.97%
