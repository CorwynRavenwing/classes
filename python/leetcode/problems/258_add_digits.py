class Solution:
    def addDigits(self, num: int) -> int:

        # new, O(1) version
        if num == 0:
            return 0
        else:
            return ((num - 1) % 9) + 1

        # original method
        while num >= 10:
            num = (num // 10) + (num % 10)

        return num

