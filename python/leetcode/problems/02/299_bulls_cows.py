class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        # SHORTCUT: otherwise known as Mastermind
        # SHORTCUT: otherwise known as Wordle
        # SHORTCUT: otherwise known as NotBeingSuedForCopyrightInfringement

        bull_list = [
            1 if (A == B) else 0
            for A, B in zip(secret, guess)
        ]
        print(f'{bull_list=}')
        bulls = sum(bull_list)
        secretCount = Counter(secret)
        guessCount = Counter(guess)
        cow_list = [
            min(count, guessCount[number])
            for number, count in secretCount.items()
        ]
        print(f'{cow_list=}')
        cows = sum(cow_list)
        cows -= bulls           # don't double-count bulls as a cow
        
        return f'{bulls}A{cows}B'

# NOTE: Accepted on first Submit
# NOTE: Runtime 35 ms Beats 90.62%
# NOTE: Memory 16.80 MB Beats 17.07%
