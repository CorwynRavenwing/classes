<pre>class Solution:

    def process(self, n: int) -&gt; int:
        print(f'process({n})')
        digits = tuple(map(int, str(n)))
        print(f'  {digits=}')
        Square = lambda x: x * x
        squares = tuple(map(Square, digits))
        print(f'  {squares=}')
        answer = sum(squares)
        print(f'  {answer=}')
        return answer

    # prime cache with &quot;1 is happy&quot; from problem description
    happy_cache = {1: True}

    def isHappy(self, n: int) -&gt; bool:
        print(f'isHappy({n})')
        print(f'  BEFORE {self.happy_cache=}')
        if n in self.happy_cache:
            answer = self.happy_cache[n]
            print(f'  cache {answer}')
            return answer
        next_number = self.process(n)
        # prime cache with False to detect loops:
        self.happy_cache[n] = False
        self.happy_cache[n] = self.isHappy(next_number)

        print(f'  AFTER: {self.happy_cache=}')

        return self.happy_cache[n]

# NOTE: Approved on second Run (base case error)
# NOTE: Approved on first Submit
# NOTE: Runtime 25 ms Beats 5.21%
# NOTE: Memory 18.05 MB Beats 17.75%</pre>