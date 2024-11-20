class Solution:
    def printVertically(self, s: str) -> List[str]:

        words = s.split(' ')
        maxLen = max(
            map(len, words)
        )
        print(f'{maxLen=}')
        for i, W in enumerate(words):
            while len(W) < maxLen:
                W += ' '
                words[i] = W
        # print(f'{words=}')

        answers = list(zip(*words))

        for j, A in enumerate(answers):
            while A and A[-1] == ' ':
                A = A[:-1]
                answers[j] = A
            A = ''.join(A)
            answers[j] = A
        # print(f'{answers=}')

        return answers

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 41 ms Beats 15.75%
# NOTE: Memory 16.67 MB Beats 13.39%
