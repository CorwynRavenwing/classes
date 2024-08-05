class Solution:
    def countBadPairs(self, nums: List[int]) -> int:

        # SHORTCUT: "j - i != nums[j] - nums[i]" may be rearranged as:
        # "nums[i] - i != nums[j] - j", which separates I and J to different sides,
        # as well as makes the thing we're calculating, the same for each side.

        # SHORTCUT: it's easier to find ALL pairs and all GOOD pairs, and subtract
        # one from the other to get BAD pairs.

        N = len(nums)

        def Nchoose2(N: int) -> int:
            return N * (N - 1) // 2

        AllPairs = Nchoose2(N)
        print(f'{AllPairs=}')

        pairingNumber = [
            nI - I
            for I, nI in enumerate(nums)
        ]
        print(f'{pairingNumber=}')
        pairingCounts = Counter(pairingNumber)
        print(f'{pairingCounts=}')

        GoodPairs = 0
        for pairNumber, count in sorted(pairingCounts.items()):
            pairs = Nchoose2(count)
            print(f'  {pairNumber=}: {count=} ({pairs=})')
            GoodPairs += pairs

        print(f'{GoodPairs=}')
        BadPairs = AllPairs - GoodPairs
        print(f'{BadPairs=}')

        return BadPairs

