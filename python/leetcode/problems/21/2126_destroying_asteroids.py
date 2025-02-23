class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        
        # SHORTCUT: arbitrary order is allowed -> start with smallest
        asteroids.sort()
        for size in asteroids:
            if mass >= size:
                print(f'+{size}')
                mass += size
            else:
                print(f'FAIL: {mass} destroyed by {size}')
                return False
        return True

# NOTE: Accepted on second Run (logic parity error)
# NOTE: Accepted on first Submit
# NOTE: Runtime 346 ms Beats 5.10%
# NOTE: Memory 32.12 MB Beats 6.15%
