class Solution:
    def convertToBase7(self, num: int) -> str:
        
        negative = (num < 0)
        if negative:
            num = -num

        base7 = [num]
        while max(base7) >= 7:
            if base7[0] >= 7:
                base7 = [0] + base7
            index = base7.index(max(base7))
            carry = base7[index] // 7
            base7[index - 1] += carry
            base7[index] -= carry * 7
        answer = ''.join(map(str, base7))
        if negative:
            answer = '-' + answer
        return answer

