<pre>class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -&gt; int:

        def int_to_digits(N: int) -&gt; List[int]:
            return list(map(int, str(N)))
        
        def digits_to_int_A(D: List[int]) -&gt; int:
            T = tuple(map(str, D))
            S = ''.join(T)
            return int(S)
        # second version is twice as fast
        def digits_to_int_B(D: List[int]) -&gt; int:
            answer = 0
            for digit in D:
                answer *= 10
                answer += digit
            return answer
        # allow choosing which version easily
        def digits_to_int(D: List[int]) -&gt; int:
            # return digits_to_int_A(D)
            return digits_to_int_B(D)

        Digits = []
        
        def clean_digits(limit: int) -&gt; None:
            nonlocal Digits
            # print(f'cd({limit}):')
            while max(Digits) &gt; limit:
                # print(f'  D={Digits}')
                error = max(Digits)
                index = Digits.index(error)
                # print(f'  found {error} at [{index}]')
                if index == 0:
                    Digits = [0] + Digits
                    continue
                Digits[index - 1] += 1
                Digits[index] = 0
            return
        
        def increment_digits(limit: int) -&gt; None:
            Digits[-1] += 1
            clean_digits(limit)
            return
        
        def generatePowerfulInt(start: int, finish: int, limit: int, s: str) -&gt; 
List[int]:
            nonlocal Digits
            # print(f'gPI({start},{finish},{limit},{s})')
            size = len(s)
            mask = 10 ** size
            leftHalf = (start // mask)
            Digits = int_to_digits(leftHalf)
            # print(f'{Digits=}')
            clean_digits(limit)
            leftHalf = digits_to_int(Digits)
            int_S = int(s)
            num = leftHalf * mask + int_S
            # print(f'  {num=} ({start} // {mask}) * {mask} + {int(s)}')
            while num &lt;= finish:
                # print(f'  {num=}')
                if num &lt; start:
                    # print(f'    skip, low')
                    pass
                else:
                    yield num
                
                increment_digits(limit)
                leftHalf = digits_to_int(Digits)
                num = leftHalf * mask + int_S
            
            return
        
        i = 0
        for P in generatePowerfulInt(start, finish, limit, s):
            i += 1
            # print(f'{i=} {P=}')
        
        return i

# NOTE: Acceptance Rate 28.1% (HARD)

# NOTE: Timeout Error</pre>