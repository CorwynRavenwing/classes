class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:

        def powerfulIntsLowerThan(finishStr: str, limit: int, s: str) -> int:
            print(f'PILT({finishStr},{limit},{s}):')
            finish = int(finishStr)
            int_S = int(s)
            if len(finishStr) < len(s):
                print(f'  0, len {len(finishStr)} < {len(s)}')
                return 0
            if len(finishStr) == len(s):
                if finish >= int_S:
                    print(f'  1, {finish=} >= {int_S}')
                    return 1
                else:
                    print(f'  0, {finish=} < {int_S}')
                    return 0
            left_length = len(finishStr) - len(s)
            left_half = finishStr[:left_length]
            right_half = finishStr[left_length:]
            print(f'DEBUG {left_length=} {left_half=} {right_half=}')
            left_digits = list(map(int, left_half))
            print(f'DEBUG   {left_digits=}')

            while max(left_digits) > limit:
                if left_digits[-1] > limit:
                    left_digits[-1] = limit
                    print(f'DEBUG   {left_digits=}')
                    continue
                error = max(left_digits)
                index = left_digits.index(error)
                # print(f'  found {error} at [{index}]')
                left_digits[index] = limit
                left_digits[index + 1] = limit + 1
                print(f'DEBUG   {left_digits=}')

            max_number = 0
            for D in left_digits:
                max_number *= 10
                max_number += D
            print(f'DEBUG    {max_number=} . {s}')
            size = len(s)
            mask = 10 ** size
            max_number *= mask
            max_number += int_S
            print(f'DEBUG    {max_number=}')

            answer = 0
            base = limit + 1
            for D in left_digits:
                answer *= base
                answer += D
            print(f'  {answer=} {s=}')
            # if right_half >= s:
            #     print(f'    +1 because {right_half} >= {s}')
            #     answer += 1
            # else:
            #     print(f'    +0 because {right_half} < {s}')
            if max_number <= finish:
                print(f'    +1 because {max_number} <= {finish}')
                answer += 1
            else:
                print(f'    +0 because {max_number} > {finish}')

            return answer

        return sum([
            powerfulIntsLowerThan(str(finish), limit, s),
            - powerfulIntsLowerThan(str(start - 1), limit, s),
        ])

# NOTE: Acceptance Rate 28.1% (HARD)

# NOTE: Accepted after much fuss
# NOTE: Runtime 11 ms Beats 52.88%
# NOTE: Memory 18.08 MB Beats 39.42%
