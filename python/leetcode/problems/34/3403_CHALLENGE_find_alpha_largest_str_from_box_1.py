class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        
        if numFriends == 1:
            print(f'1 friend -> no splits possible')
            return word
        
        min_letters_in_other_buckets = numFriends - 1
        max_size = len(word) - min_letters_in_other_buckets
        possibles = {
            word[i:i + max_size]
            for i in range(len(word))
        }
        # print(f'{possibles=}')
        return max(possibles)

# NOTE: Accepted on first Run
# NOTE: Accepted on third Submit (Output Exceeded)
# NOTE: Runtime 48 ms Beats 17.46%
# NOTE: Memory 30.35 MB Beats 5.56%

# NOTE: re-ran for challenge:
# NOTE: Runtime 51 ms Beats 18.94%
# NOTE: Memory 30.62 MB Beats 5.30%
