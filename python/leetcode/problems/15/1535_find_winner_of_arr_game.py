class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        
        # SHORTCUT: if a number loses a round and moves to the end,
        # and if it ever returns to position 1, the number in position 0
        # will either be (A) the number it lost to, or (B) a higher number.
        # Therefore it will *NOT* win any future round.
        # And so, we can *remove* any losing number, from the list.
        # ... but I'm not sure this speeds us up any, unless we'd otherwise
        # be simulating k=1_000_000 or something

        if k > len(arr):
            return max(arr)
        
        wins = 0    # number in position 0 hasn't actually won once yet
        while wins < k:
            try:
                (A, B) = arr[:2]
            except ValueError:
                wins += 1
                continue
            print(f'{wins}: ({A},{B})')
            if A < B:
                wins = 1    # new winner supplants champion
                del arr[0]
            else:
                wins += 1   # champion wins again
                del arr[1]
        
        print(f'{wins}: ({A},{B})')
        return arr[0]

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (edge case in increasing order)
# NOTE: Runtime 2089 ms Beats 22.12%
# NOTE: Memory 25.95 MB Beats 100.00%
