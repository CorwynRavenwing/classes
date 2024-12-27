class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:

        # ignoring the hint, I've created a formula for the
        # number of apples in a square with "radius" R,
        # where L = 2R.
        
        def Triangle(N: int) -> int:
            return (N) * (N + 1) // 2
        
        def X(N: int) -> int:
            return sum([
                Triangle(N + 1) * N,
                Triangle(N - 1) * (N + 1)
            ])
        
        def Apples(N: int) -> int:
            return 4 * X(N)
        
        def Perimeter(R: int) -> int:
            # R is radius; 2R is diameter; 4D is perimeter
            return 4 * 2 * R
        
        R = 0
        while True:
            R += 1
            A = Apples(R)
            # print(f'{R}: {A}')
            if A >= neededApples:
                break
        
        print(f'{R}: {A}')
        return Perimeter(R)

# NOTE: Accepted on second Run (loop exit condition missing)
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 3218 ms Beats 5.94%
# NOTE: Memory 17.82 MB Beats 8.91%
