class Solution:
    def minSwaps(self, s: str) -> int:

        openBracketIndex = [
            index
            for index, value in enumerate(s)
            if value == '['
        ]
        # print(f'{openBracketIndex=}')
        mutable_S = list(s)

        depth = 0
        swaps = 0
        for i in range(len(mutable_S)):
            value = mutable_S[i]
            if value == '[':
                depth += 1
            elif value == ']':
                if depth > 0:
                    depth -= 1
                else:
                    print(f'{i=}: Must swap, {depth=}')
                    swaps += 1
                    index = openBracketIndex.pop(-1)
                    mutable_S[i] = mutable_S[index]
                    mutable_S[index] = value
                    # now, get new value
                    value = mutable_S[i]
                    assert value == '['
                    depth += 1

        return swaps

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 485 ms Beats 9.10%
# NOTE: Memory 49.53 MB Beats 5.02%
