class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        coordinates.sort()
        print(f'{coordinates=}')
        pairs = list(zip(coordinates, coordinates[1:]))
        print(f'{pairs=}')
        diffs = [
            (B[0] - A[0], B[1] - A[1])
            for A, B in pairs
        ]
        print(f'{diffs=}')
        slopes = [
            str(1_000_000_000 * A // B) if B else 'INF'
            for (A, B) in diffs
        ]
        print(f'{slopes=}')
        check = slopes.pop(0)
        for slope in slopes:
            if slope != check:
                print(f"error: {slope=} {check=}")
                return False
        return True

