class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        
        mod = 10 ** 9 + 7

        seen = set()
        # queue = {(0,0,0,0),(0,0,1,0)}
        queue = {(0,0,0,0)}     # "no zeros === no ones"
        answer = 0
        while queue:
            state = queue.pop()
            print(f'{state=}')
            if state in seen:
                print(f'  seen')
                continue
            else:
                seen.add(state)

            (a,b,c,d) = state
            if a > zero:
                print(f'  >0')
                continue
            if b > one:
                print(f'  >1')
                continue
            
            if a == zero and b == one:
                answer += 1
                print(f'  {answer=}')
                continue
            
            if d > limit:
                print(f'  >D')
                continue
            
            # add another C:
            print(f'  + C')
            if c == 0:
                state = (a+1, b, c, d+1)
            else:
                state = (a, b+1, c, d+1)
            queue.add(state)

            # add another not-C:
            print(f'  +!C')
            if c == 0:
                not_c = 1
                state = (a, b+1, not_c, 1)
            else:
                not_c = 0
                state = (a+1, b, not_c, 1)
            queue.add(state)

        return answer
        
# NOTE: Acceptance Rate 30.0% (medium)

# NOTE: wrong answer for some inputs
