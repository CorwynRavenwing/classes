class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:

        k = 0
        answer = ''
        while answer in sequence:
            k += 1
            answer = word * k
            print(f'{k=} {answer=} found={answer in sequence}')
        return (k-1)

