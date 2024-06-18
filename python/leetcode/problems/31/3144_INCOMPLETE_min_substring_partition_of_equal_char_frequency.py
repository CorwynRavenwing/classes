from collections import Counter

class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:

        def is_balanced(s: str) -> bool:
            if len(s) == 1:
                return 1
            letters = Counter(s)
            counts = Counter(letters.values())
            return (len(counts) == 1)
        
        if is_balanced(s):
            return 1
        
        score_at_length = {
            0: 0
            # at beginning of string, score is zero
        }
        length_for_score = {
            0: [0]
        }
        checks = 0
        for i in range(1, len(s)+1):
            # print(f'{i=} "{s[i-1]}"')
            min_answer = len(s) + 1     # answer guaranteed to be lower than this
            for score_j, j_for_that_score in length_for_score.items():
                if score_j + 1 >= min_answer:
                    # print(f"    STOP: {score_j + 1} >= {min_answer}")
                    break
                # print(f'  {score_j=}')
                for j in reversed(j_for_that_score):
                    # reversed() so we try shorter test strings first
                    test = s[j:i]
                    # print(f'    {j=} {test=}')
                    checks += 1
                    if is_balanced(test):
                        # print(f'    {j=} {test=}')
                        # print(f'      score[{j-1}]={score_j}')
                        min_answer = min(min_answer, score_j + 1)
                        # re-run test with new min_answer
                        if score_j + 1 >= min_answer:
                            # print(f"      STOP: {score_j + 1} >= {min_answer}")
                            break
                    # else:
                    #     print(f'    unbalanced')
            score_i = min_answer
            score_at_length[i] = score_i
            length_for_score.setdefault(score_i, [])
            length_for_score[score_i].append(i)
            # print(f'{i=} set LFS[{score_i}] = {length_for_score[score_i]}')
        print(f'Total calls to is_balanced(): {checks}')
        return score_at_length[len(s)]

# TODO: still timing out for large data sets

