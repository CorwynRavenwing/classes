class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center
        return

    def randPoint(self) -> List[float]:
        while True:
            # random point within bounding square
            x = random.uniform(self.x - self.r, self.x + self.r)
            y = random.uniform(self.y - self.r, self.y + self.r)
            print(f'trying {(x, y)}')
            distance_from_center = sqrt(
                sum([
                    (x - self.x) ** 2,
                    (y - self.y) ** 2,
                ])
            )
            print(f'  distance = {distance_from_center}')
            if distance_from_center > self.r:
                print(f'    TOO FAR, try again')
                # this will rerun (1 - PI/4) of the time, which is a bit under 1/4
                # (1 - PI/4) = (4 - PI)/4 ~= 0.85851/4 ~= 0.21463 ~= 21.5%
                # (okay, Math says actually a bit over 1/5, which is much better)
                continue
            else:
                print(f'    okay')
                return (x, y)

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
