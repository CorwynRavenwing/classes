class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:

        onesDigitOfNum = str(num)[-1]
        strK = str(k)
        print(f'{k=} {onesDigitOfNum=}')

        # This table is created by looking at the last digit
        # of each entry in the "times by X" table, until a
        # zero is reached.  (After a zero this pattern repeats.)
        # e.g. 4: [4, 8, 12, 16, 20] 
        digits_reachable = {
            '0': '0',
            '1': '1234567890',
            '2': '24680',
            '3': '3692581470',
            '4': '48260',
            '5': '50',
            '6': '62840',
            '7': '7418529630',
            '8': '86420',
            '9': '9876543210',
        }
        
        # special case for "sum of nothing"
        if num == 0:
            print(f'  Number zero is the sum of []')
            return 0
        
        if strK == onesDigitOfNum:
            print(f'  Just use {num=} as the number ending in {k=}')
            return 1

        digits = digits_reachable[strK]
        if onesDigitOfNum in digits:
            index = digits.index(onesDigitOfNum)
            print(f'{k}: [{digits}]')
            print(f'  Reachable with {index+1} numbers')
            min_value = k * (index + 1)
            if min_value <= num:
                return index + 1
            else:
                print(f'    ERROR: {min_value=} > {num=}')
                return -1
        else:
            print(f'  {k} can only reach {digits=}, not {onesDigitOfNum}')
            return -1
# NOTE: Runtime 31 ms Beats 82.19%
# NOTE: Memory 16.62 MB Beats 16.44%
