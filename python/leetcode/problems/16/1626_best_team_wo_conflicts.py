class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        age_and_score = tuple(sorted(zip(ages, scores)))
        # print(f'{age_and_score=}')

        possibles = {0: 0}    # {min_score: total_score}

        for (age, score) in age_and_score:
            for (min_score, total_score) in tuple(possibles.items()):
                
                if score < min_score: 
                    # "conflict"
                    continue
                
                new_total_score = total_score + score
                new_min_score = max(score, min_score)

                possibles.setdefault(new_min_score, new_total_score)
                if possibles[new_min_score] < new_total_score:
                    # new best score for this min_score
                    possibles[new_min_score] = new_total_score
        
        print(f'{possibles=}')
        return max(possibles.values())

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 1098 ms Beats 29.73%
# NOTE: Memory 17.12 MB Beats 27.45%
