class Solution:
    def wiggleSort(self, nums: List[int]) -> None:

        indexes = None

        def cleanup() -> None:
            nonlocal nums, indexes

            # print(f'N={nums}')
            # print(f'I={indexes}')
            for currentIndex, goodIndex in enumerate(indexes):
                if currentIndex == goodIndex:
                    # print(f'  {currentIndex} OK')
                    continue
                while currentIndex != goodIndex:
                    # pick up changed value
                    goodIndex = indexes[currentIndex]
                    if currentIndex == goodIndex:
                        continue
                    # print(f'  swap {currentIndex}, {goodIndex}')
                    (
                        nums[currentIndex],
                        nums[goodIndex],
                    ) = (
                        nums[goodIndex],
                        nums[currentIndex],
                    )
                    (
                        indexes[currentIndex],
                        indexes[goodIndex],
                    ) = (
                        indexes[goodIndex],
                        indexes[currentIndex],
                    )
                    # print(f'N={nums}')
                    # print(f'I={indexes}')
            # print(f'N={nums}')
            # print(f'I={indexes}')

        nums.sort()
        L = len(nums)
        numbers = list(range(L))
        even = list(filter(lambda x: x % 2 == 0, numbers))
        odds = list(filter(lambda x: x % 2 == 1, numbers))
        indexes = even + odds

        cleanup()

        problem = None
        for i in range(0, L):
            if nums[i] == nums[i-1]:
                print(f'PROBLEM: {i=} {nums[i]=} == {nums[i-1]=}')
                problem = i
                break
        if problem is not None:
            left = numbers[L-problem:]
            right = numbers[:L-problem]
            indexes = left + right
            cleanup()
        """
        Do not return anything, modify nums in-place instead.
        """

