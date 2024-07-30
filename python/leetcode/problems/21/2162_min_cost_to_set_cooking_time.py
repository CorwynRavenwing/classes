class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:

        def CostPush(mm: int, ss: int) -> int:
            # the cost to push the buttons in this order
            if not ((0 <= mm <= 99) and (0 <= ss <= 99)):
                print(f'Error: CostPush({mm},{ss}): input OOB')
                return float('+inf')
            MM = str(mm)
            SS = str(ss)
            if mm == 0:
                # No minutes: do not press '0' for minutes
                MM = ''
            elif ss < 10:
                # nonzero minutes + single-digit seconds: must press '0' between
                SS = '0' + SS
            digits = MM + SS
            move_to_first_digit = (
                0
                if (int(digits[0]) == startAt)
                else moveCost
            )
            move_between_digits = [
                0 if (A == B) else moveCost
                for (A, B) in zip(digits, digits[1:])
            ]
            push_each_digit = pushCost * len(digits)
            cost = sum([
                move_to_first_digit,
                *move_between_digits,
                push_each_digit,
            ])
            print(f'CostPush({mm},{ss}) = "{digits}" = ${cost}')
            return cost
        
        mm = targetSeconds // 60
        ss = targetSeconds - 60 * mm
        print(f'Shooting for {targetSeconds=} = {mm}:{ss}')
        normalWay = CostPush(mm, ss)
        plus60Way = CostPush(mm - 1, ss + 60)
        print(f'  {normalWay=} {plus60Way=}')

        return min(normalWay, plus60Way)

