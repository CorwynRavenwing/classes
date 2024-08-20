class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        @cache
        def bestPair(Player: int, Index: int, M: int, depth=0) -> Tuple[int,int]:
            margin = ' ' * depth
            PlayerName = "AB"
            # print(f'{margin}bestPair({PlayerName[Player]},I={Index},{M=})')
            max_X = 2 * M
            if Index + max_X >= len(piles):
                # print(f'{margin}  {Index} + {max_X} >= {len(piles)}: Take everything!')
                new_index = Index + max_X
                taken_frag = piles[Index:new_index]
                taken_value = sum(taken_frag)
                # print(f'{margin}  (take {taken_frag})')
                answer = [0, 0]
                answer[Player] += taken_value
                return tuple(answer)

            possible_outcomes = []
            for X in range(1, max_X + 1):
                # print(f'{margin}  Try taking {X}/{max_X}:')
                other_player = 1 - Player
                new_index = Index + X
                new_M = max(M, X)
                taken_frag = piles[Index:new_index]
                taken_value = sum(taken_frag)
                # print(f'{margin}  (take {taken_frag})')
                outcome = bestPair(
                    other_player,
                    new_index,
                    new_M,
                    depth + 1
                )
                (A, B) = outcome
                answer = [A, B]
                answer[Player] += taken_value
                # print(f'{margin}  {X} -> {tuple(answer)}')
                possible_outcomes.append(tuple(answer))
            possible_outcomes.sort(
                reverse=True,
                key=lambda x: x[Player]     # sort by best score for *this player*
            )
            # print(f'{margin}{possible_outcomes=}')
            return possible_outcomes[0]

        (Alice, Bob) = bestPair(0, 0, 1)
        
        return Alice
# NOTE: Runtime 4296 ms Beats 5.10%
# NOTE: Memory 83.62 MB Beats 5.10%
