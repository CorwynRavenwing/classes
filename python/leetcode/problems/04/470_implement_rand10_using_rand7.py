# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):

        # print(f' 7^6 = {7 ** 6}')     #  7^6 = 117649
        # print(f'10^5 = {10 ** 5}')    # 10^5 = 100000
        cutoff = (10 ** 5)

        while True:
            number = 0
            for i in range(6):
                number *= 7
                number += (rand7() - 1)
            if number >= cutoff:
                print(f'{number} too high: loop again')
                continue
            # print(f'{number=}')
            return (number % 10) + 1
        """
        :rtype: int
        """

