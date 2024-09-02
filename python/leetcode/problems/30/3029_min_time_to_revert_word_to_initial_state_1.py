class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:

        answer = 0
        W = word
        print(f'{answer}: {W}')
        while True:
            answer += 1
            W = W[k:]
            print(f'{answer}: {W}')
            if word.startswith(W):
                return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 24 ms Beats 98.41%
# NOTE: Memory 16.64 MB Beats 13.49%
