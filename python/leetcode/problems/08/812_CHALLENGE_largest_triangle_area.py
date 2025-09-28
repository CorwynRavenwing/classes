class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        
        max_area = 0
        for i, A in enumerate(points):
            (x1, y1) = A
            print(f'[{i}]:{A}')
            for j, B in enumerate(points):
                if j <= i:
                    # print(f'[{i}]:{A} [{j}]:skip')
                    continue
                print(f'[{i}]:{A} [{j}]:{B}')
                (x2, y2) = B
                x12 = (x2 - x1)
                y12 = (y2 - y1)

                for k, C in enumerate(points):
                    if k <= j:
                        # print(f'[{i}]:{A} [{j}]:{B} [{k}]:skip')
                        continue
                    print(f'[{i}]:{A} [{j}]:{B} [{k}]:{C}')
                    (x3, y3) = C
                    x13 = (x3 - x1)
                    y13 = (y3 - y1)
                    area = ((x12 * y13) - (x13 * y12)) / 2
                    area = abs(area)
                    print(f'      {area=}')
                    max_area = max(area, max_area)
        
        return max_area

# NOTE: Acceptance Rate 62.6% (easy)

# NOTE: Accepted on second Run (negative area needs absolute value)
# NOTE: Accepted on first Submit
# NOTE: Runtime 367 ms Beats 5.10%
# NOTE: Memory 18.02 MB Beats 9.89%
