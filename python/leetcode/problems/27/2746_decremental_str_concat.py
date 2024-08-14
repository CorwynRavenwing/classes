class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:

        def AZ_and_Len(i: int) -> Tuple[str,int]:
            thisWord = words[i]
            wordA = thisWord[0]
            wordZ = thisWord[-1]
            wordAZ = wordA + wordZ
            wordLen = len(thisWord)
            return (wordAZ, wordLen)
        
        (wordAZ, wordLen) = AZ_and_Len(0)
        shortestLengthsForAZ = {
            # including word #0:
            0: {
                # first char + last char --> entire length of 0th word
                wordAZ: wordLen
            }
        }
        # print(f'{shortestLengthsForAZ[0]=}')
        for i in range(1, len(words)):
            prior = shortestLengthsForAZ[i - 1]
            print(f'{i-1}: {prior}:')
            (wordAZ, wordLen) = AZ_and_Len(i)
            print(f'{i}: "{wordAZ}",{wordLen}:')
            possibles = [
                (
                    # try prior + word
                    (
                        priorAZ[0] + wordAZ[1],
                        priorLen + wordLen + (
                            -1
                            if (priorAZ[1] == wordAZ[0])
                            else 0
                        )
                    ),
                    # try word + prior
                    (
                        wordAZ[0] + priorAZ[1],
                        priorLen + wordLen + (
                            -1
                            if (wordAZ[1] == priorAZ[0])
                            else 0
                        )
                    ),
                )
                for priorAZ, priorLen in prior.items()
            ]
            # flatten once
            possibles = [
                P
                for Ppair in possibles
                for P in Ppair
            ]
            possibles.sort()
            # print(f'{possibles=}')
            for j in range(1, len(possibles)):
                (priorAZ, priorLen) = possibles[j - 1]
                (thisAZ, thisLen) = possibles[j]
                if priorAZ == thisAZ:
                    # print(f'  Merge "{priorAZ}" {j-1},{j}')
                    possibles[j - 1] = None
                    possibles[j] = (thisAZ, min(priorLen, thisLen))
            while None in possibles:
                possibles.remove(None)
            # print(f'{possibles=}')
            shortestLengthsForAZ[i] = dict(possibles)

        lastAZ = shortestLengthsForAZ[len(words) - 1]
        print(f'{lastAZ=}')
        
        return min(lastAZ.values())
# NOTE: Accepted upon first submit :-)
# NOTE: Runtime 728 ms Beats 14.17%
# NOTE: Memory 23.09 MB Beats 85.04%
