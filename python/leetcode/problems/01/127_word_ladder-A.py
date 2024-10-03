class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # we borrow some code from #433:
        
        if endWord not in wordList:
            return 0
        
        def wordDistance(word1: str, word2: str) -> int:
            return sum([
                1 if (A != B) else 0
                for A, B in zip(word1, word2)
            ])

        def neighborsOf(word: str) -> List[str]:
            neighbors = [
                word2
                for word2 in wordList
                if wordDistance(word, word2) == 1
            ]
            return neighbors

        states = {beginWord}
        known = set()
        answer = 1      # we count the first word as well
        while states:
            print(f'{answer}: L={len(states)}')
            new_states = set()
            for word in states:
                print(f'  {word}', end="")
                if word in known:
                    print(f' -> duplicate')
                    continue
                if word == endWord:
                    print(f' -> YES')
                    return answer
                known.add(word)
                neighbors = neighborsOf(word)
                for N in neighbors:
                    new_states.add(N)
            states = new_states
            answer += 1

        print(f'FAILURE')
        return 0

# NOTE: Accpance Rate 40.5% (HARD)
# NOTE: Time Limit Exceeded for large inputs
