class Solution:
    def findProductsOfElements(self, queries: List[List[int]]) -> List[int]:

        '''
        (1)  = (1  + (2 * 0))   1
        (4)  = (2  + (2 * 1))   2 [1 2]
        (12) = (4  + (2 * 4))   4 [1 4] [2 4] [1 2 4]
        (32) = (8  + (2 * 12)   8 [1 8] [2 8] [1 2 8] [4 8] [1 4 8] [2 4 8] [1 2 4 8]
        (80) = (16 + (2 * 32))  16 ... [1 2 4 8 16]

        end[0]: (1)  = (2^0 * 1)  0
        end[1]: (4)  = (2^1 * 2)  1 [0 1]
        end[2]: (12) = (2^2 * 3)  2 [0 2] [1 2] [0 1 2]
        end[3]: (32) = (2^3 * 4)  3 [0 3] [1 3] [0 1 3] [2 3] [0 2 3] [1 2 3] [0 1 2 3]
        end[4]: (80) = (2^4 * 5)  4 [0 4] [1 4] [0 1 4] .. [0 2 3 4] [1 2 3 4] [0 1 2 3 4]
        '''

        def int2bin(n: int) -> List[int]:
            answer = []
            while n:
                answer.append(n % 2)
                n //= 2
            if not answer:
                answer.append(0)
            return answer
        
        def powerful_exp(n: int) -> List[int]:
            return [
                exp
                for exp, bit in enumerate(int2bin(n))
                if bit
            ]

        def powerful(n: int) -> List[int]:
            return [
                2 ** exp
                for exp in powerful_exp(n)
            ]

        def pow_2_mod(p: int, mod: int) -> int:
            answer = 1
            print(f'p2m({p},{mod})')
            print(f'  1:{answer}')
            answer %= mod
            print(f'  %:{answer}')
            for i in range(p):
                answer *= 2
                print(f'  *:{answer}')
                answer %= mod
                print(f'  %:{answer}')
            return answer
        
        big_exp = []
        for i in range(1, 32):
            exp = powerful_exp(i)
            # print(f'{i=} {len(exp)=}')
            big_exp.extend(exp)
        print(f'{big_exp=}')

        answers = []
        for Q in queries:
            print(f'  {Q=}')
            (fromI, toI, modI) = Q
            if fromI <= toI <= len(big_exp):
                rangeI = big_exp[fromI:toI+1]
                print(f'  {rangeI=}')
                S = sum(rangeI)
                print(f'  sum={S}')
                A = pow_2_mod(S, modI)
                answers.append(A)
            else:
                print(f'ERROR: out of range: [{fromI}:{toI}] > {len(big_exp)}')
                answers.append(-99)
                print(f'fromI: {powerful_exp(fromI)}')
                print(f'toI:   {powerful_exp(toI)}')
                return answers

        return answers

# TODO: failing for data sets containing large query values


