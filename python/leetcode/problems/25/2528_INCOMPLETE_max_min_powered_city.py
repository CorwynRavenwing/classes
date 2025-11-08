class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:

        def power_sum(stations: List[int], r: int) -> List[int]:
            power_diffs = [0] * (len(stations) + 1)
            for (city, power) in enumerate(stations):
                left = max(city - r, 0)
                right = min(city + r + 1, len(stations))
                power_diffs[left] += power
                power_diffs[right] -= power

            power_sums = tuple(accumulate(power_diffs))
            assert power_sums[-1] == 0
            return power_sums[:-1]
        
        power_sums = power_sum(stations, r)
        # print(f'{power_sums=}')

        def first_index_LT_value(nums: List[int], value: int) -> int:
            indexes = [
                (
                    1 if num < value else 0
                )
                for num in nums
            ]
            # print(f'    1i<v({value},{nums}): {indexes}')
            if 1 not in indexes:
                # print(f'    1i<v({value},{nums}): index=None')
                return None
            else:
                answer = indexes.index(1)
                # print(f'    1i<v({value},{nums}): index={answer}')
                return answer

        def isPossible(target: int) -> bool:
            # print(f'\n?({target}):')
            try_k = k
            try_stations = list(stations)   # copy it
            try_sums = list(power_sums)     # copy it
            while (Min := min(try_sums)) < target and try_k > 0:
                # print(f'  {Min=} {try_k=}')
                index = first_index_LT_value(try_sums, target)
                if index is None:
                    # print(f'  {index=} STOP')
                    break
                value = try_sums[index]
                # print(f'    [{index}]={value}')
                index += r
                index = min(index, len(stations) - 1)
                diff = target - value
                diff = max(diff, 0)
                diff = min(diff, try_k)
                try_k -= diff
                try_stations[index] += diff
                try_sums = power_sum(try_stations, r)
                # print(f'    [{index}]+={diff}: {try_sums}')

            answer = (Min >= target)
            # print(f'?({target}): {answer} ({Min} >? {target})')
            return answer

        L = 0
        left = isPossible(L)
        if not left:
            print(f'Strange, {L=} is false')
            return L
        R = max(power_sums) + k + 1
        right = isPossible(R)
        if right:
            print(f'Strange, {R=} is true')
            return -1
        print(f'[{L},{R}] ({left},{right})')
        while L + 1 < R:
            M = (L + R) // 2
            mid = isPossible(M)
            print(f'[{L},{M},{R}] ({left},{mid},{right})')
            if mid:
                print(f'  True: replace Left')
                (L, left) = (M, mid)
            else:
                print(f'  False: replace Right')
                (R, right) = (M, mid)

        print(f'[{L},{R}] ({left},{right})')
        # L is now the highest possible True value
        return L

# NOTE: Acceptance Rate 38.1% (HARD)

# NOTE: TLE for large inputs
