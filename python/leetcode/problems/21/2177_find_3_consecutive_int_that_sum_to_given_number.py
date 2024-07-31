class Solution:
    def sumOfThree(self, num: int) -> List[int]:

        # SHORTCUT: (X-1) + (X) + (X+1) === (3 * X)
        # Therefore, return X // 3 (+/- 1) if that's an integer, else []
        
        if num % 3 == 0:
            X = num // 3
            return [X - 1, X, X + 1]
        else:
            return []
# NOTE: Solution accepted upon first submittal
# NOTE: Runtime 31 ms Beats 81.30%
# NOTE: O(1)
# NOTE: Memory 16.53 MB Beats 30.34%
# NOTE: O(1)
