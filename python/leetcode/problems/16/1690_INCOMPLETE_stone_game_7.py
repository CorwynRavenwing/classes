class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        
        # SHORTCUT 1: Bob trying to minimize the difference, and Alice trying
        # to maximize the difference, amount to each of them doing the
        # exact same thing: trying to maximize their own score.  It's just
        # explaining why we aren't asked whether Alice or Bob wins.  Poor Bob.

        # UPDATE: this turns out not to be the case, as when Bob chooses
        # a higher answer, it may leave Alice with an answer that's higher
        # by a bigger coefficient, which is bad for Bob.  Poor Bob.

        # SHORTCUT 2: "Pick a stone, and receive a score of the sum of all
        # the other stones in the row" === "receive a score of sum(EntireRow) - ChosenStone"

        @cache
        def DP(stones: List[int], isAlice=True) -> Tuple[int,int]:
            print(f'DP({stones},"{"A" if isAlice else "B"}")')
            if len(stones) <= 1:
                # 0 == no stones == no score
                # 1 == 1 stone == picked it, receive score of (all other stones) == no score
                print(f'  -> (0,0)')
                return (0, 0)
            
            Sum = sum(stones)
            answers = []
            choices = {}

            def get_scores_for_choices(picked: int, not_picked: List[int]) -> Tuple[int,int]:
                nonlocal answers
                nonlocal choices
                score = Sum - picked
                (other, myself) = DP(not_picked, not isAlice)
                new_answer = (myself + score, other)
                choices[new_answer] = f'Pick={picked}({score})'
                answers.append(new_answer)

            get_scores_for_choices(stones[0], stones[1:])
            get_scores_for_choices(stones[-1], stones[:-1])

            # ALICE_KEY = lambda X: (max(X) - min(X))
            # ALICE_KEY = lambda X: (X[0], -X[1])
            ALICE_KEY = lambda X: (X[1],  -X[0])    # maximize Alice, minimize Bob, if you're Alice
            # BOB_KEY = lambda X: -ALICE_KEY(X)
            # BOB_KEY = lambda X: (X[1], -X[0])
            # BOB_KEY = lambda X: (X[1], -X[1])
            ALICE_MINUS_BOB_IF_BOB = lambda X: (X[1] - X[0])
            BOB_KEY = lambda X: -ALICE_MINUS_BOB_IF_BOB(X)  # negative, to minimize this instead

            CURRENT_PLAYER_KEY = (ALICE_KEY if isAlice else BOB_KEY)

            answers.sort(
                key=CURRENT_PLAYER_KEY,
                reverse=True
            )
            retval = answers[0]
            chosen = choices[retval]
            print(f'DP({stones},"{"A" if isAlice else "B"}"): {chosen} {retval=} {choices=}')
            return retval
        
        scores = DP(tuple(stones))
        print(f'{scores=}')
        (Alice, Bob) = scores
        return Alice - Bob

# NOTE: I am at a loss as to the criterion Bob is supposed to use to choose a move.
#   if Alice sees (5 3 1), she will pick 1 and Bob 3, giving A,B=(8,3), diff=5.
#   if Alice sees (3 1 4), she will pick 3 and Bob 1, giving A,B=(5,4), diff=1.
#   Therefore when Bob sees (5 3 1 4), he needs to choose between these options:
#   Pick 4, get 9 points, add to Alice's (5 3 1) answer of (8,3), total=(8,12), diff=-4
#   Pick 5, get 8 points, add to Alice's (3 1 4) answer of (5,4), total=(5,12), diff=-7
# But whatever I have Bob pick, it never seems to be the right answer.

# NOTE: incomplete, often giving the wrong answer
