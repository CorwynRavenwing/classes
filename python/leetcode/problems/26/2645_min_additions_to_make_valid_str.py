class Solution:
    def addMinimum(self, word: str) -> int:
        
        answer = 0
        pattern = "abc"
        word_index = 0
        pattern_index = 0
        while word_index < len(word):
            W = word[word_index]
            P = pattern[pattern_index]
            print(f'[{pattern_index},{word_index}]: {P}/{W}')
            if W == P:
                word_index += 1
            else:
                print(f'  +{P}')
                answer += 1
            pattern_index += 1
            pattern_index %= 3
        while pattern_index != 0:
            P = pattern[pattern_index]
            print(f'[{pattern_index},EOF]: {P}/-')
            print(f'  +{P}')
            answer += 1
            pattern_index += 1
            pattern_index %= 3
        return answer

# NOTE: Acceptance Rate 50.3% (medium)

# NOTE: Accepted on second Run (edge case with addition after string)
# NOTE: Accepted on first Submit
# NOTE: Runtime 18 ms Beats 5.88%
# NOTE: Memory 17.89 MB Beats 40.11%
