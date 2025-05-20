class Solution:
    def divisorGame(self, n: int) -> bool:
        
        # STEP 1: if n == 1, you lose.

        # STEP 2: if n == 2, your move is "-1";
        # your opponent gets 1 and loses,
        # you win.

        # STEP 3: if n is odd, all divisors are odd;
        # odd - odd === even;
        # your opponent will have an even number, lower than n.
        # If this continues, your opponent will get the
        # even number 2, and win.

        # STEP 4: this does continue, because if n is even,
        # you can always subtract 1 and give your opponent
        # an odd number, lower than n.

        # STEP 5: Therefore, all odd numbers lose, all even numbers win.

        return (n % 2 == 0)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.83 MB Beats 41.01%
