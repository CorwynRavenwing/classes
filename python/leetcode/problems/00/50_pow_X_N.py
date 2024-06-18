class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n < 0:
            is_neg = True
            n = -n
        else:
            is_neg = False

        largest_power = 1
        powers_of_x = [(1, x)]
        print(f'power: {powers_of_x[0]}')
        while largest_power < n:
            (I, PI) = powers_of_x[-1]
            I2 = 2 * I
            PI2 = PI * PI
            powers_of_x.append( (I2, PI2) )
            print(f'power: ({I2},{PI2})')
            largest_power = I2
        
        answer = 1.0
        i = n
        print(f'{i=} {answer=}')
        while i:
            (I, PI) = powers_of_x.pop()
            while i >= I:
                i -= I
                answer *= PI
                print(f'{i=} ({I},{PI}) {answer=}')
        
        if is_neg:
            answer = 1/answer
        
        return answer

