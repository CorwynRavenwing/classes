class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        prefixSums = list(itertools.accumulate(nums))

        averages = [
            (
                (
                    (
                        (
                            prefixSums[i + k]
                        ) - (
                            prefixSums[i - k - 1]
                            if (i - k - 1) >= 0
                            else 0
                        )
                    ) // (
                        (2 * k) + 1
                    )
                )
                if 0 <= (i - k) <= (i + k) < len(nums)
                else
                -1
            )
            for i in range(len(nums))
        ]

        return averages
# NOTE: accepted on first submittal :-)
