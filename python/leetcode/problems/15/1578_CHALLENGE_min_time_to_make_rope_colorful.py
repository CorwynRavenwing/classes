class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        pairs = list(zip(colors, neededTime))
        # print(f'{pairs=}')
        print(f'{len(pairs)=}')

        seconds = 0
        prev_color = 'guaranteed not to be a balloon color'
        prev_time = float('+inf')
        count = 0
        time_sum = 0
        time_max = 0
        for (this_color, this_time) in pairs:
            if prev_color != this_color:
                # start a new color
                if count == 0:
                    pass
                elif count > 1:
                    # we remove all baloons except the one with the maximum time
                    new_seconds = (time_sum - time_max)
                    # print(f'{new_seconds} sec removing {count-1} "{prev_color}" balloons')
                    seconds += new_seconds
                # else:
                #     print(f'Skip: only {count} "{prev_color}" balloon')
                prev_color = this_color
                count = 0
                time_sum = 0
                time_max = 0
            count += 1
            time_sum += this_time
            time_max = max(this_time, time_max)

        # clean up last group
        if count == 0:
            pass
        elif count > 1:
            # we remove all baloons except the one with the maximum time
            new_seconds = (time_sum - time_max)
            # print(f'{new_seconds} sec removing {count-1} "{prev_color}" balloons')
            seconds += new_seconds
        # else:
        #     print(f'Skip: only {count} "{prev_color}" balloon')

        return seconds

# NOTE: Acceptance Rate 63.5% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 150 ms Beats 22.04%
# NOTE: Memory 30.19 MB Beats 5.00%

# NOTE: re-ran for challenge:
# NOTE: Runtime 176 ms Beats 17.99%
# NOTE: Memory 31.22 MB Beats 5.14%
