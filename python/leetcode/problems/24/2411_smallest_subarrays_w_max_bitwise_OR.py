class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:

        binary_size = len(f'{max(nums):b}')
        print(f'{binary_size=}')
        binary_strings = [
            f'{N:0{binary_size}b}'
            for N in nums
        ]
        # print(f'{binary_strings=}')
        bits = tuple(zip(*binary_strings))
        # print(f'{bits=}')

        REV = lambda x: tuple(reversed(tuple(x)))

        bitsReversed = tuple(
            map(
                REV,
                bits
            )
        )
        # print(f'{bitsReversed=}')

        def checkDistance(arr: List[int]) -> List[int]:
            # print(f'checkDistance({arr}):')
            answer = []
            lastSeen = None
            for i, A in enumerate(arr):
                # print(f'  {i}:{A}')
                if A == '1':
                    # print(f'    now')
                    lastSeen = i
                    answer.append(1)
                elif lastSeen is None:
                    # print(f'    never')
                    answer.append(1)
                else:
                    # print(f'    {i} - {lastSeen} = {i - lastSeen}')
                    answer.append(i - lastSeen + 1)
            return answer

        distancesReversed = tuple(
            map(
                checkDistance,
                bitsReversed
            )
        )
        # print(f'{distancesReversed=}')
        distances = tuple(
            map(
                REV,
                distancesReversed
            )
        )
        # print(f'{distances=}')
        distancesByBits = tuple(
            zip(*distances)
        )
        # print(f'{distancesByBits=}')
        maxDistance = tuple(
            map(
                max,
                distancesByBits
            )
        )
        # print(f'{maxDistance=}')
        return maxDistance
# NOTE: Runtime 1148 ms Beats 55.17%
# NOTE: O(N log M)
# NOTE: Memory 238.51 MB Beats 5.17%
# NOTE: O(N)
