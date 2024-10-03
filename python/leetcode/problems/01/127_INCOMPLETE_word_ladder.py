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

        totalDistanceTo = {}
        answer = 1      # we count the first word as well
        states = [(1, beginWord)]
        queueing = set()
        while states:
            print(f'L={len(states)}')
            (answer, word) = states.pop(0)
            print(f'  {answer}: {word}', end="")
            if word in totalDistanceTo:
                print(f' -> duplicate')
                continue
            totalDistanceTo[word] = answer
            if word == endWord:
                print(f' -> YES')
                break
            print(f' -> check:')
            neighbors = neighborsOf(word)
            for N in neighbors:
                if N in queueing:
                    print(f'  skip {N}')
                    continue
                else:
                    print(f'  +{N=}')
                    queueing.add(N)
                    bisect.insort(states, (answer + 1, N))

        print(f'{totalDistanceTo=}')
        if endWord in totalDistanceTo:
            print(f'Found!')
            return totalDistanceTo[endWord]
        else:
            print(f'FAILURE')
            return 0

# NOTE: Accpance Rate 40.5% (HARD)
# NOTE: still Time Limit Exceeded, not sure where the bottleneck is
