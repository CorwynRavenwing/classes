class Solution:
    def flipLights(self, n: int, presses: int) -> int:

        def bulbs_after_press(button: int, bulbs_before: List[int]) -> List[int]:
            bulbs = list(bulbs_before)
            if button == 1:
                for j in range(1, n+1, 1):
                    bulbs[j-1] = 0 if (bulbs[j-1] == 1) else 1
                    # print(f'  {j}: {bulbs[j-1]}')
            elif button == 2:
                for j in range(2, n+1, 2):
                    bulbs[j-1] = 0 if (bulbs[j-1] == 1) else 1
                    # print(f'  {j}: {bulbs[j-1]}')
            elif button == 3:
                for j in range(1, n+1, 2):
                    bulbs[j-1] = 0 if (bulbs[j-1] == 1) else 1
                    # print(f'  {j}: {bulbs[j-1]}')
            elif button == 4:
                for j in range(1, n+1, 3):
                    bulbs[j-1] = 0 if (bulbs[j-1] == 1) else 1
                    # print(f'  {j}: {bulbs[j-1]}')
            else:
                raise ValueError(f'invalid value {button=} (range 1..4')
            return tuple(bulbs)

        n = min(n, 6)
        bulbs = (0,) * n
        # print(f'{0}: {bulbs}')
        possibles = {bulbs}
        for i in range(1, presses+1):
            print(f'{possibles=}')
            new_possibles = set()
            for bulbs in possibles:
                for button in [1,2,3,4]:
                    after = bulbs_after_press(button, bulbs)
                    print(f'{bulbs} + b{button} = {after}')
                    new_possibles.add(after)
            possibles = new_possibles
        print(f'{possibles=}')
        return len(possibles)

