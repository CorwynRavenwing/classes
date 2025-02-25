class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        
        if finalSum % 2 != 0:
            return []
        
        stack = []
        value = 2
        print(f'[start] {finalSum}')
        while finalSum:
            if finalSum >= value:
                stack.append(value)
                finalSum -= value
                print(f'+{value} -> {finalSum}')
                value += 2
            else:
                prior = stack.pop(-1)
                oldValue = value
                value = prior + finalSum
                finalSum += prior
                print(f'  {oldValue} too big: pop {prior} -> {finalSum}')
                stack.append(value)
                finalSum -= value
                print(f'+{value} -> {finalSum}')
                value = None
                assert finalSum == 0
                break
        
        return stack

# NOTE: Accepted on second Run (GT vs GE error)
# NOTE: Accepted on first Submit
# NOTE: Runtime 364 ms Beats 5.21%
# NOTE: Memory 27.90 MB Beats 27.14%
