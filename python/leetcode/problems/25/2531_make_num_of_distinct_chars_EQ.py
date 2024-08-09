class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:

        count1 = Counter(word1)
        count2 = Counter(word2)
        print(f'{count1=}')
        print(f'{count2=}')

        len1 = len(count1)
        len2 = len(count2)
        print(f'{len1=} {len2=}')

        changeAs = []
        for letter, count in count1.items():
            print(f'  {letter=} {count=}')
            change1 = (-1 if count == 1 else 0)
            change2 = (0 if letter in count2 else +1)
            changeAs.append((letter, change1, change2))
        changeBs = []
        for letter, count in count2.items():            # swapped from prior section
            print(f'  {letter=} {count=}')
            change1 = (-1 if count == 1 else 0)
            change2 = (0 if letter in count1 else +1)   # swapped
            changeBs.append((letter, change2, change1)) # swapped
        
        print(f'{changeAs=}')
        print(f'{changeBs=}')

        for (letterA, change1A, change2A) in changeAs:
            for (letterB, change1B, change2B) in changeBs:
                if letterA == letterB:
                    newLen1 = len1
                    strLen1 = f'{letterA}:{len1} (no change)'
                    newLen2 = len2
                    strLen2 = f'{letterB}:{len2} (no change)'
                else:
                    newLen1 = len1 + change1A + change1B
                    strLen1 = f'{letterA}:({len1} + {change1A} + {change1B})'
                    newLen2 = len2 + change2A + change2B
                    strLen2 = f'{letterB}:({len2} + {change2A} + {change2B})'
                print(f'{strLen1} = {newLen1} ?= {strLen2} = {newLen2}')
                if newLen1 == newLen2:
                    return True

        return False
# NOTE: Runtime 125 ms Beats 64.29%
# NOTE: Memory 17.98 MB Beats 5.19%
