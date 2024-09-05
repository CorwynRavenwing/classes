class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:

        # if mean = total / (n + m), then total = mean * (n + m)
        # n == given, m == len(rolls)
        # also total == sum([answer]) + sum(rolls)
        # and therefore [answer] = [total - sum(rolls)]
        
        m = len(rolls)
        total = mean * (n + m)
        missing = total - sum(rolls)
        print(f'{n=} {m=} {total=} {missing=}')
        answer = [1] * n
        while (sum(answer) < missing) and (1 in answer):
            index = answer.index(1)
            diff = missing - sum(answer)
            print(f'{sum(answer)=} < {missing}: ({diff=})')
            if diff > 5:
                if index == 0:
                    old_len = len(answer)
                    # print(f'{old_len=} {answer=}')
                    replacements = min(diff // 5, old_len)
                    print(f'  Replace {replacements} copies of {1} with {6}')
                    answer = [6] * replacements + [1] * (old_len - replacements)
                    new_len = len(answer)
                    # print(f'{new_len=} {answer=}')
                    assert old_len == new_len
                    new_diff = missing - sum(answer)
                    print(f'    {new_diff=}')
                    assert (new_diff < 5) or (replacements == new_len)
                    continue
                else:
                    diff = 5
            print(f'  Replace {1} at {index=} with {1 + diff}')
            answer[index] += diff
        diff = missing - sum(answer)
        comparison_string = (
            '=' if sum(answer) == missing else
            '<' if sum(answer) < missing else
            '>' if sum(answer) > missing else
            '?!?'
        )
        print(f'{sum(answer)} {comparison_string} {missing}: ({diff=})')
        if diff == 0:
            answer.sort()
            print(f'answer={Counter(answer)}')
            return answer
        else:
            print(f'FAIL')
            return []

# NOTE: Runtime 1075 ms Beats 15.51%
# NOTE: Memory 27.73 MB Beats 22.73%
