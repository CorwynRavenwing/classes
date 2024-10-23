class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        tokens = tuple(sorted(tokens))

        @cache
        def DP(score: int, power: int, tokens: List[int]) -> int:

            if not tokens:
                print(f'DP({score},{power},{tokens})')
                return score

            # do nothing
            answers = [score]

            # SHORTCUT: *ALWAYS* use Face up, if possible;
            # if not, then use Face down instead, if possible;

            Min = tokens[0]
            Max = tokens[-1]

            print(f'DP({score},{power},[{Min}..{Max}])')
            if power >= Min:
                # Face up: use minimum-price token
                new_score = score + 1
                new_power = power - Min
                new_tokens = tokens[1:]
                answers.append(
                    DP(new_score, new_power, new_tokens)
                )
            elif score >= 1:
                # Face down: use maximum-price token
                new_score = score - 1
                new_power = power + Max
                new_tokens = tokens[:-1]
                answers.append(
                    DP(new_score, new_power, new_tokens)
                )

            print(f'DP({score},{power},[{Min}..{Max}]): {answers}')
            return max(answers)
        
        return DP(0, power, tokens)

# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 95 ms Beats 6.67%
# NOTE: Memory 46.56 MB Beats 10.00%
