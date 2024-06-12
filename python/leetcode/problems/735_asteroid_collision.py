class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        working = True
        while working:
            working = False
            # print(f'{asteroids}')
            for i in range(1, len(asteroids)):
                left = asteroids[i - 1]
                right = asteroids[i]
                if left > 0 and right < 0:
                    print(f'index {i-1},{i} asteroids {left},{right} crash!')
                    working = True
                    if abs(left) < abs(right):
                        print(f'  {right=} wins!')
                        asteroids[i - 1] = None
                        break
                    elif abs(left) > abs(right):
                        print(f'  {left=} wins!')
                        asteroids[i] = None
                        break
                    else:
                        print(f'  both destroyed!')
                        asteroids[i - 1] = None
                        asteroids[i] = None
                        break
            while None in asteroids:
                asteroids.remove(None)
        return asteroids

