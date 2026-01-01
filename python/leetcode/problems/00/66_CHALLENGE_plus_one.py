class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        digits[-1] += 1
        while max(digits) >= 10:
            print(f"{digits=}")
            if digits[0] >= 10:
                digits = [0] + digits
                continue
            index = digits.index(max(digits))
            carry = digits[index] // 10
            digits[index - 1] += carry
            digits[index] -= carry * 10
        print(f"{digits=}")
        return digits

# NOTE: Acceptance Rate 48.5% (easy)

# NOTE: re-ran for challenge:
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.52 MB Beats 77.57%
