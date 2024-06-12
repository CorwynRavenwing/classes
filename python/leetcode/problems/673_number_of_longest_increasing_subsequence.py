class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        longestN = [None] * len(nums)
        countN = [None] * len(nums)

        longestN[0] = 1
        countN[0] = 1

        for i in range(1, len(nums)):
            # print(f'N={nums}')
            # print(f'L={longestN}')
            # print(f'C={countN}')

            N = nums[i]
            # print(f'[{i}]={N}')
            indexes_of_lower_numbers = [
                index
                for index, number in enumerate(nums[:i])
                if number < N
            ]
            # print(f'lower={indexes_of_lower_numbers}')
            if indexes_of_lower_numbers:
                # print(f'Case A')
                # case A: there are lower numbers left of here.
                longest_value_list = [
                    longestN[index]
                    for index in indexes_of_lower_numbers
                ]
                # print(f'Longests={longest_value_list}')
                max_longest_value = (
                    max(longest_value_list)
                    if longest_value_list
                    else 0
                )
                # print(f'max={max_longest_value}')
                indexes_matching_max_longest = [
                    index
                    for index in indexes_of_lower_numbers
                    if longestN[index] == max_longest_value
                ]
                # print(f'max indexes={indexes_matching_max_longest}')
                longestN[i] = max_longest_value + 1
                countN[i] = sum([
                    countN[index]
                    for index in indexes_matching_max_longest
                ])
            else:
                # print(f'Case B')
                # case B: there are NOT lower numbers left of here.
                # start a new list of length 1
                longestN[i] = 1
                countN[i] = 1
        print(f'N={nums}')
        print(f'L={longestN}')
        print(f'C={countN}')
        max_longest_value = max(longestN)
        print(f'max={max_longest_value}')
        indexes_matching_max_longest = [
            index
            for index, N in enumerate(longestN)
            if N == max_longest_value
        ]
        print(f'max indexes={indexes_matching_max_longest}')
        print(f'Max Longest Value = {max_longest_value}')
        answer = sum([
            countN[index]
            for index in indexes_matching_max_longest
        ])
        print(f'Count of Max L V = {answer}')
        return answer

