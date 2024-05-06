class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:

        num[-1] += k
        while max(num) >= 10:
            if num[0] >= 10:
                num = [0] + num
            index = num.index(max(num))
            carry = num[index] // 10
            num[index - 1] += carry
            num[index] -= carry * 10
        
        return num

