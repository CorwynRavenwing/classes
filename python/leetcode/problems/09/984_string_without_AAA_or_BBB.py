class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:

        answers = []
        if a < b:
            print(f'{a=} {b=}')
            orphanBs = min(2, b)
            this = 'b' * orphanBs
            print(f'  "{this}"')
            answers.append(this)
            b -= orphanBs
        while a and b:
            print(f'{a=} {b=}')
            if a > b:
                this = 'aab'
                print(f'  "{this}"')
                answers.append(this)
                a -= 2
                b -= 1
            elif a < b:
                this = 'abb'
                print(f'  "{this}"')
                answers.append(this)
                a -= 1
                b -= 2
            elif a == b:
                this = 'ab'
                print(f'  "{this}"')
                answers.append(this)
                a -= 1
                b -= 1
            else:
                raise Exception(f'comparison of {a} <=> {b} failed!')
        if 0 < a <= 2:
                this = 'a' * a
                print(f'  "{this}"')
                answers.append(this)
                a -= a
        if b == 1:
                this = 'b'
                print(f'  "{this}"')
                answers.append(this)
                b -= 1
        if a or b:
            # raise Exception(f'leftover values {a=} {b=}')
            print(f'leftover values {a=} {b=}')
            return 'FAIL'
        
        return ''.join(answers)

# NOTE: 29 ms; Beats 93.63%
