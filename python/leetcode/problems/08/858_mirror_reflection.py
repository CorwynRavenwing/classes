class Solution:

    def reflectFromPoint(self, coord: Tuple[int,int], p: int, q: int) -> int:
        # NOTE: could make this a loop in calling fn rather than recursive
        # print(f'reflect({coord}) ({p},{q})')
        (x1, y1) = coord
        (x2, y2) = (x1 + p, y1 + q)
        assert x2 in [-p, 0, p]
        assert x2 in [0, self.P]
        if y2 < 0:
            y2 = -y2
            q = -q
        elif y2 > self.P:
            # y2 = self.P - (y2 - self.P)
            # y2 = self.P - y2 + self.P
            y2 = (2 * self.P) - y2
            q = -q
        p = -p
        projection = (x2, y2)
        print(f'bounce {projection} {p:+d} {q:+d}')
        if projection in self.receptors:
            answer = self.receptors[projection]
            print(f'FOUND!  {projection=} #{answer}')
            return answer
        return self.reflectFromPoint(projection, p, q)

    def mirrorReflection(self, p: int, q: int) -> int:
        
        self.origin = (0,0)
        self.receptors = {
            (p, 0): 0,
            (p, p): 1,
            (0, p): 2,
            (0, 0): -1,
        }
        self.P = p
        self.Q = q
        print(f'start: {self.origin} {p:+d} {q:+d}')
        return self.reflectFromPoint(self.origin, p, q)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 11 ms Beats 100.00%
# NOTE: Memory 16.99 MB Beats 8.85%
