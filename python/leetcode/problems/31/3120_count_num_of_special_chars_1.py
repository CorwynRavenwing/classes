class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        counts = Counter(word)
        print(f'{counts=}')

        answer = 0
        for C in counts.keys():
            if C.islower():
                U = C.upper()
                N = counts[U]
                print(f'{C=} {U=} {N=}')
                if N:
                    answer += 1

        return answer

# NOTE: Accepted on first Submit
# NOTE: Runtime 50 ms Beats 6.23%
# NOTE: Memory 16.61 MB Beats 33.33%
