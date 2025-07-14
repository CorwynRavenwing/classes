class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        
        players = ['o'] * n
        firstIndex = firstPlayer - 1
        secondIndex = secondPlayer - 1
        players[firstIndex] = 'A'
        players[secondIndex] = 'B'
        players = ''.join(players)
        print(f'{players=}')

        # @cache
        def possibles(players: str) -> List[str]:
            def possibles_gen(players: str) -> List[str]:
                if len(players) in (0, 1):
                    yield players
                    return
                first = players[0]
                last = players[-1]
                middle = players[1:-1]
                # print(f'{players} -> "{first}/{middle}/{last}"')
                assert players == first + middle + last
                for new_middle in possibles(middle):
                    if first in 'AB' and last in 'AB':
                        yield '*' + new_middle + '*'
                    elif first in 'AB':
                        yield first + new_middle
                    elif last in 'AB':
                        yield new_middle + last
                    else:
                        yield first + new_middle
                        yield new_middle + last
            return tuple(sorted(set(possibles_gen(players))))

        def earliest_latest(players:str) -> Tuple[int,int]:
            (min_low, max_high) = (float('+inf'), -1)
            for child in possibles(players):
                if '*' in child:
                    return [1,1]
                low, high = earliest_latest(child)
                min_low = min(low, min_low)
                max_high = max(high, max_high)
            return [min_low + 1, max_high + 1]

        return earliest_latest(players)

# NOTE: Acceptance Rate 50.7% (HARD)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: *** without cache:
# NOTE: Runtime 27 ms Beats 42.86%
# NOTE: Memory 17.80 MB Beats 80.95%
# NOTE: *** with cache:
# NOTE: Runtime 11 ms Beats 42.86%
# NOTE: Memory 18.28 MB Beats 42.86%
# NOTE: twice as fast, but same percent; same memory, twice as small ?!
