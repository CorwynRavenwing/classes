class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        AZ = lambda x: alphabet.index(x)

        mod = 10 ** 9 + 7

        ModItem = lambda x: x % mod
        ModList = lambda L: tuple(map(ModItem, L))
        
        # if t > 100:
        #     return 37

        freq = [0] * 26
        for letter, count in Counter(s).items():
            freq[AZ(letter)] = count
        freq = tuple(freq)

        def Transform26(freq: List[int]) -> List[int]:
            assert len(freq) == 26
            first = freq[0]
            last = freq[-1]
            rest = freq[1:-1]
            second = first + last
            addB = (last, second) + rest
            answer = tuple(
                map(
                    sum,
                    zip(freq, addB)
                )
            )
            assert len(answer) == 26
            return ModList(answer)
        
        def Transform1(freq: List[int]) -> List[int]:
            assert len(freq) == 26
            first = freq[0]
            last = freq[-1]
            rest = freq[1:-1]
            second = first + last
            answer = tuple(
                (last, second) + rest
            )
            assert len(answer) == 26
            return ModList(answer)

        while t >= 26:
            # print(f'{t}: {freq}')
            freq = Transform26(freq)
            t -= 26
        
        while t:
            # print(f'{t}: {freq}')
            freq = Transform1(freq)
            t -= 1
        
        # print(f'{t}: {freq}')

        answer = sum(freq)
        
        return answer % mod

# NOTE: Acceptance Rate 32.5% (medium)

# NOTE: needed several Runs to get it working
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 475 ms Beats 83.66%
# NOTE: Memory 18.21 MB Beats 62.09%
