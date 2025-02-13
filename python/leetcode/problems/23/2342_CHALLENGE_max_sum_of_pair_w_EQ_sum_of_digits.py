class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        def sum_of_digits(n: int) -> int:
            strN = str(n)
            digits = tuple(map(int, strN))
            answer = sum(digits)
            # print(f'SOD({n}) {digits=} {answer=}')
            return answer
        
        SoD = {}
        for n in nums:
            Sum = sum_of_digits(n)
            SoD.setdefault(Sum, [])
            SoD[Sum].append(n)
        # print(f'{SoD=}')

        answers = set()
        for Sum, EqualSum in SoD.items():
            if len(EqualSum) < 2:
                # print(f'{Sum=} <2 items')
                continue
            EqualSum = sorted(EqualSum, reverse=True)
            EqualSum = EqualSum[:2]
            total = sum(EqualSum)
            # print(f'{Sum=} {EqualSum=} {total=}')
            answers.add(total)
        # print(f'{answers=}')

        return max(answers, default=-1)

# NOTE: Runtime 491 ms Beats 29.25%
# NOTE: Memory 33.41 MB Beats 78.99%
