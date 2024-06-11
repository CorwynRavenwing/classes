class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:

        points = [p1, p2, p3, p4]
        distances = []  # actually recording D^2
        for i, point1 in enumerate(points):
            (x1, y1) = point1
            for j, point2 in enumerate(points):
                if i >= j:
                    # comparing points out of order
                    continue
                (x2, y2) = point2
                dist = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)
                print(f'p[{i}]={point1}; p[{j}]={point2}; dist=SQRT({dist})')
                distances.append(dist)
        print(f'{distances=}')
        distCounts = Counter(distances)
        print(f'{distCounts=}')
        if len(distCounts) != 2:
            print(f'strange number ({len(distCounts)}, not 2) of distances')
            return False
        side_len_squared, diagonal_len_squared = (None, None)
        for (dist, count) in distCounts.items():
            if count == 4:
                side_len_squared = dist
                print(f'{side_len_squared=}')
            elif count == 2:
                diagonal_len_squared = dist
                print(f'{diagonal_len_squared=}')
            else:
                print(f'strange distance {count=}, not 2 or 4')
                return False
        
        if side_len_squared is None or diagonal_len_squared is None:
            print(f'one of {side_len_squared=} {diagonal_len_squared=} is still {None}')
            return False

        if side_len_squared * 2 != diagonal_len_squared:
            print(f'{diagonal_len_squared=} must be twice {side_len_squared=}')
            return False
        
        return True

