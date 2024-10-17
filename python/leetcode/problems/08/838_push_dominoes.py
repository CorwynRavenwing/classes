class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        N = len(dominoes)

        def find_all_indexes(char: str, s: str) -> List[int]:
            answers = []
            startIndex = 0
            while True:
                try:
                    index = s.index(char, startIndex)
                except ValueError:
                    break
                answers.append(index)
                startIndex = index + 1
            return answers

        MINUS_1 = lambda x: x - 1
        PLUS_1 = lambda x: x + 1

        MOVE_LEFT = lambda x: set(map(MINUS_1, x))
        MOVE_RIGHT = lambda x: set(map(PLUS_1, x))
        FILTER = lambda x: set([
            val
            for val in x
            if (0 <= val < N)
        ])

        TERM = 'X'
        QUERY = '?'
        DOT = '.'
        RIGHT = 'R'
        LEFT = 'L'
        STOP = '|'
        # dominoes = TERM + dominoes + TERM
        print(f'PD({dominoes}):')
        dominoes_mutable = list(dominoes)

        indexes_dotL = find_all_indexes(DOT + LEFT, dominoes)
        # print(f'{indexes_dotL=}')
        indexes_L = set(indexes_dotL)           # dotL = index of the dot
        print(f'{indexes_L=}')
        indexes_Rdot = find_all_indexes(RIGHT + DOT, dominoes)
        # print(f'{indexes_Rdot=}')             # Rdot = index of the R
        indexes_R = MOVE_RIGHT(indexes_Rdot)    # index of the dot
        print(f'{indexes_R=}')

        while indexes_L or indexes_R:
            # print(f'DEBUG: {dominoes_mutable}')
            # print(f'    L: {indexes_L}')
            # print(f'    R: {indexes_R}')
            
            indexes_both = indexes_L & indexes_R
            print(f' both: {indexes_both}')
            if indexes_both:
                for index in indexes_both:
                    assert dominoes_mutable[index] == DOT
                    dominoes_mutable[index] = STOP
                indexes_L -= indexes_both
                indexes_R -= indexes_both
            for index in tuple(indexes_L):
                if dominoes_mutable[index] != DOT:
                    print(f'    L,{index=} data="{dominoes_mutable[index]}"')
                    indexes_L.remove(index)
                else:
                    dominoes_mutable[index] = LEFT
            for index in tuple(indexes_R):
                if dominoes_mutable[index] != DOT:
                    print(f'    R,{index=} data="{dominoes_mutable[index]}"')
                    indexes_R.remove(index)
                else:
                    dominoes_mutable[index] = RIGHT
            indexes_L = FILTER(MOVE_LEFT(indexes_L))
            indexes_R = FILTER(MOVE_RIGHT(indexes_R))

        # print(f'DEBUG: {dominoes_mutable}')

        result = [
            (
                DOT
                if D == STOP
                else D
            )
            for D in dominoes_mutable
        ]
        return ''.join(result)

# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 216 ms Beats 49.92%
# NOTE: Memory 24.26 MB Beats 37.31%
