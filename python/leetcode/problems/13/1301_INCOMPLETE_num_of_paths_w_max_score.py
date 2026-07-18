class Solution:
    def pathsWithMaxScore(
        self,
        board: List[str]
    ) -> List[int]:
        
        mod = 10 ** 9 + 7

        def getValue(coords: Tuple[int,int]) -> str:
            (x, y) = coords
            try:
                return board[x][y]
            except IndexError:
                return None

        def translate(value: str) -> int:
            match value:
                case 'S':
                    # start
                    return 0
                case 'E':
                    # end
                    return 0
                case 'X':
                    # blocker
                    return None
                case _:
                    # a number: use that
                    return int(value)
        
        def neighborsOf(coords: Tuple[int,int]) -> List[Tuple[int,int]]:
            (x, y) = coords
            return [
                (x + 1, y + 0),
                (x + 0, y + 1),
                (x + 1, y + 1),
            ]

        def max_not_none(L: list) -> int:
            while None in L:
                L.remove(None)
            return max(L, default=None)

        def sum_not_none(L: list) -> int:
            while None in L:
                L.remove(None)
            return sum(L)

        @cache
        def DP_max_possible_score_ending_at(
            coords: Tuple[int,int]
        ) -> int:
            rawValue = getValue(coords)
            # print(f'DEBUG: DP1({coords}): {rawValue=}')
            if rawValue is None:
                # print(f'  -> OOB')
                return None
            if rawValue == 'S':
                # print(f'  -> "S" @ LR')
                return 0
            if rawValue == 'E':
                # print(f'  (UL)')
                # we start at the end
                pass
            if rawValue == 'X':
                # print(f'  -> X')
                # blocker
                return None
            value = translate(rawValue)
            # print(f'  -> {value=}')
            if value is None:
                raise Exception(
                    f'should not get here {rawValue=}{value=}'
                )
            answers = [
                DP_max_possible_score_ending_at(neighbor)
                for neighbor in neighborsOf(coords)
            ]
            # print(f'DEBUG: DP1({coords}): {answers=}')
            answer = max_not_none(answers)
            # print(f'DEBUG: DP1({coords}): {answer=}')
            if answer is None:
                # print(f'  -> NO PATH')
                return None
            return value + answer

        @cache
        def DP_count_paths_with_score_ending_at(
            score: int,
            coords: Tuple[int,int]
        ) -> int:
            rawValue = getValue(coords)
            if rawValue is None:
                # print(f'  -> OOB')
                return 0
            if rawValue == 'S':
                # have reached the start
                if score == 0:
                    # ... and used up all our score values
                    return 1
                else:
                    # print(f'DEBUG: DP2({score},{coords}): {rawValue=} {score=} TOO LOW')
                    return None
            if rawValue == 'E':
                # we start at the end
                pass
            if rawValue == 'X':
                # blocker
                return None
            value = translate(rawValue)
            if value is None:
                raise Exception(
                    f'should not get here {rawValue=}{value=}'
                )
            # print(f'DEBUG: DP2({score},{coords}): {rawValue=} -> {value}')
            new_score = score - value
            answers = [
                DP_count_paths_with_score_ending_at(new_score, neighbor)
                for neighbor in neighborsOf(coords)
            ]
            # print(f'DEBUG: DP2({score},{coords}): {answers=}')
            answer = sum_not_none(answers)
            answer %= mod
            # print(f'DEBUG: DP2({score},{coords}): {answer=}')
            if answer is None:
                # print(f'  -> NO PATH')
                return None
            return answer

        UL = (0,0)
        max_score = DP_max_possible_score_ending_at(UL)
        print(f'{max_score=}')

        if max_score is None:
            print(f'NO PATH TO END')
            return [0,0]

        answer = DP_count_paths_with_score_ending_at(max_score, UL)

        return [max_score, answer % mod]

# NOTE: Acceptance Rate 42.9% (HARD)

# NOTE: INCOMPLETE: Time Limit Exceeded, even with cache
