class Solution:
    def wonderfulSubstrings(self, word: str) -> int:

        letters = "abcdefghij"
        Index = lambda L: letters.index(L)
        Bit = lambda L: 1 << Index(L)

        prefixBits = [0] + [None] * len(word)
        
        for i, L in enumerate(word):
            bit = Bit(L)
            prefixBits[i + 1] = prefixBits[i] ^ bit
            # print(f'[{i}]{L} ({bit}): {prefixBits}')
        
        prefixCounts = Counter(prefixBits)
        answer = 0
        for prefix, count in prefixCounts.items():
            print(f'{prefix}: {count}')
            triangle = count * (count - 1) // 2
            print(f'  Triangle({count}) = {triangle}')
            answer += triangle
            for L in letters:
                bit = Bit(L)
                withBit = prefix | bit
                if prefix == withBit:
                    # print(f'    {L}: {bit} {prefix} == {withBit}')
                    continue
                count2 = prefixCounts[withBit]
                if not count2:
                    # print(f'    {L}: {bit} {prefix} -> {withBit} no {count2=}')
                    continue
                # print(f'    {L}: {bit} {prefix} -> {withBit} YES')
                product = count * count2
                print(f'    {L}: {count=} * {count2=} = {product=}')
                answer += product
        
        return answer

# NOTE: Accepted on second Run (variable name typo)
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 595 ms Beats 99.40%
# NOTE: Memory 22.30 MB Beats 6.02%
