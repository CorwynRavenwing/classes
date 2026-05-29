class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        
        zeros = [
            index
            for index, value in enumerate(s)
            if value == '0'
        ]
        print(f'{zeros=}')
        
        root = 0
        target = len(s) - 1
        last = zeros[-1]
        if last != target:
            print(f'final character in S is not zero!  {last=} {zeros[-1]=} {s[-1]=}')
            return -1
        
        # strategy: start with reachable = {0}
        # for each value in reachable:
        # find all members of zeros that are within the range [i+min, i+max]
        # and add them to reachable
        # when you're done processing all members,
        # return true if target is in reachable

        return -99999

# NOTE: Acceptance Rate 26.8% (medium)

# NOTE: INCOMPLETE, need to try performing the strategy mentioned above
