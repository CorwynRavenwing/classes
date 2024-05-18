class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        sorted_intervals = sorted([
            (interval, index)
            for index, interval in enumerate(intervals)
        ])
        print(f'{sorted_intervals[:5]=}...')
        answers = []
        for index, interval in enumerate(intervals):
            (startI, endI) = interval
            print(f'interval {index} = [{startI},{endI}]')
            L = 0
            left = sorted_intervals[L][0][0]
            R = len(intervals) - 1
            right = sorted_intervals[R][0][0]
            print(f'[{L},{R}] = ({left},{right}) {endI=}')
            if left > endI:
                print(f'  fail L, {left} > {endI}')
                answers.append(-1)
                continue
            if right < endI:
                print(f'  fail R, {right} < {endI}')
                answers.append(-1)
                continue
            while L + 1 < R:
                M = (L + R) // 2
                mid = sorted_intervals[M][0][0]
                # print(f'B [{L},{M},{R}] = ({left},{mid},{right}) {endI=}')
                if mid >= endI:
                    # print('  replace R')
                    (R, right) = (M, mid)
                    continue
                if mid < endI:
                    # print('  replace L')
                    (L, left) = (M, mid)
                    continue
                # if mid == endI:
                #     print(f'[{L},{M},{R}] = ({left},{mid},{right}) {endI=}')
                #     raise Exception('not sure what to do here')

            print(f'after loop: [{L},{R}] = ({left},{right}) {endI=}')
            found = -1
            if left >= endI:
                print(f'  found {L=}')
                found = L
            elif right >= endI:
                print(f'  found {R=}')
                found = R
            if found > -1:
                print(f'  ... found {found=}')
                S_I = sorted_intervals[found]
                print(f'    {S_I=}')
                (intervalJ, J) = S_I
                print(f'      {intervalJ=}')
                intervalI = intervals[J]
                print(f'      {intervalI=}')
                assert intervalI == intervalJ
                answers.append(J)
            else:
                print('  not found')
                answers.append(-1)

        return answers

