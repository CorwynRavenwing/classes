class Solution:

    def size(self, rect: List[int]) -> int:
        (A, B, X, Y) = rect
        # we need "count of integer points within", not "area"
        return (X - A + 1) * (Y - B + 1)

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.sizes = [
            self.size(rect)
            for rect in rects
        ]
        self.total = sum(self.sizes)
        return

    def pick_random_rectangle(self) -> List[int]:
        chosen = random.randint(1, self.total)
        # print(f'{chosen=}')
        for i, rect in enumerate(self.rects):
            print(f'  {i=} {chosen=} size={self.sizes[i]}')
            if chosen <= self.sizes[i]:
                # print(f'    chosen')
                return rect
            else:
                # print(f'    -no-')
                chosen -= self.sizes[i]
        raise Exception(f'{chosen=} ran out of choices!')

    def pick(self) -> List[int]:
        rect = self.pick_random_rectangle()
        (A, B, X, Y) = rect
        point = (
            random.randint(A, X),
            random.randint(B, Y),
        )
        print(f'{point=} chosen in {rect=}')
        return point

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
