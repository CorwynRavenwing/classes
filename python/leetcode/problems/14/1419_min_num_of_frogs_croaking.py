class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        
        COF = croakOfFrogs
        for (index, letter) in enumerate('croak'):
            COF = COF.replace(letter, str(index))
        croakList = list(map(int, COF))
        # print(f'{croakList=}')

        inProgress = Counter()
        answer = 0
        frogs = 0
        for letter in croakList:
            if letter == 0:
                frogs += 1
                answer = max(answer, frogs)
                inProgress[letter] += 1
                # print(f'  {frogs=} {sorted(inProgress.items())}')
                continue

            if inProgress[letter - 1] <= 0:
                print(f'Error: {letter} without {letter - 1}')
                return -1

            inProgress[letter - 1] -= 1
            if letter == 4:
                frogs -= 1
            else:
                inProgress[letter] += 1
            
            # print(f'  {frogs=} {sorted(inProgress.items())}')

        if frogs:
            print(f'Error: Croakus Interruptus')
            return -1

        return answer

# NOTE: Runtime 155 ms Beats 26.41%
# NOTE: Memory 18.09 MB Beats 5.14%
