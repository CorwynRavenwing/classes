class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:

        final_score = [None, None]
        for (i, scores) in enumerate([player1, player2]):
            print(f"{i=} {scores=}")
            (prev10, this10) = (False, False)
            score = 0
            for j, S in enumerate(scores):
                add = S
                if prev10 or this10:
                    add *= 2
                score += add
                print(f"  {j=} [{S}] {add} {score}")
                (prev10, this10) = (this10, S == 10)
            final_score[i] = score
        
        print(f'{final_score=}')
        (P1, P2) = final_score
        if P1 > P2:
            return 1
        if P2 > P1:
            return 2
        if P1 == P2:
            return 0
        raise Exception("{P1=} and {P2=} are not comparable")

