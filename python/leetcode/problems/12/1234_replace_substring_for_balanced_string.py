class Solution:
    def balancedString(self, s: str) -> int:

        balanced = len(s) // 4
        print(f'{balanced=}')
        countEverything = Counter(s)
        print(f'{countEverything=}')
        unbalanced = {
            letter: max(count - balanced, 0)
            for letter, count in countEverything.items()
            if balanced < count
        }
        print(f'{unbalanced=}')

        if not unbalanced:
            return 0

        def verifyFrag(countFrag: Counter) -> bool:
            # nonlocal unbalanced
            stillProblem = {
                letter: max(count - countFrag[letter], 0)
                for letter, count in unbalanced.items()
            }
            # print(f'  {stillProblem}')
            stillProblem = {
                letter: count
                for letter, count in stillProblem.items()
                if count > 0
            }
            # print(f'  {stillProblem}')
            if stillProblem:
                return False
            else:
                return True
        
        answer = float('+inf')
        (i, j) = (0, 0)
        letterI = s[i]
        letterJ = s[j]
        print(f'{j=} ="{letterJ}"')
        countFrag = Counter(letterJ)    # begin with letter #0
        while i < len(s):
            if verifyFrag(countFrag):
                print(f'    YES: {i}:{j} ={j - i + 1}')
                answer = min(answer, j - i + 1)
                # "yes" answer: shrink frag from left
                countFrag[letterI] -= 1
                # print(f'{i=} -"{letterI}"')
                i += 1
                if j >= len(s):
                    print(f'      I out of bounds')
                    break
                letterI = s[i]
                # print(f'{i=} now at "{letterI}"')
            else:
                # print(f'    NO: {i}:{j}')
                # "no" answer: grow frag to right
                j += 1
                if j >= len(s):
                    print(f'      J out of bounds')
                    break
                letterJ = s[j]
                # print(f'{j=} +"{letterJ}"')
                countFrag[letterJ] += 1
        return answer

