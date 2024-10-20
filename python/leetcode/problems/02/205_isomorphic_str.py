class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        def getPattern(s: str) -> List[int]:
            print(f'pattern({s}):')
            answer = []
            mappings = {}
            nextValue = 0
            for char in s:
                if char not in mappings:
                    nextValue += 1
                    print(f'  "{char}" -> {nextValue}')
                    mappings[char] = nextValue
                answer.append(mappings[char])
            answer = tuple(answer)
            print(f'-> {answer}')
            return answer
        
        return getPattern(s) == getPattern(t)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 7 ms Beats 99.30%
# NOTE: Memory 17.24 MB Beats 9.95%
