class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        ORD = lambda char: alphabet.index(char)
        DIST = lambda A, B: abs(ORD(A) - ORD(B))
        AEC = lambda A, B: (DIST(A, B) <= 1)
        answer = 0
        index = 1   # character 0 is always fine
        while index < len(word):
            prev = word[index - 1]
            this = word[index]
            if AEC(prev, this):
                print(f'[{index}]: {prev}/{this}')
                answer += 1
                index += 1      # skip an *extra* character
            else:
                print(f'[{index}]: --')
            index += 1
        return answer

# NOTE: Acceptance Rate 52.0% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 16 ms Beats 5.06%
# NOTE: Memory 17.93 MB Beats 15.95%
