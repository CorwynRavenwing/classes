class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        acc = 0
        X = []
        # print(f"- {acc}")
        for bit in nums:
            acc *= 2
            acc += bit
            # print(f"{bit} {acc}")
            X.append(acc)
        # print(f"{X=}")
        div5 = [
            Xi % 5 == 0
            for Xi in X
        ]
        # print(f"{div5=}")
        return div5

