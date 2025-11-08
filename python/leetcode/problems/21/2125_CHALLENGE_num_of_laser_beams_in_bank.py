class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:

        devices_per_row = [
            Counter(row)['1']
            for row in bank
        ]
        print(f'{devices_per_row=}')
        devices_per_row = [
            row
            for row in devices_per_row
            if row  # filter away any zero rows
        ]
        print(f'{devices_per_row=}')

        beams = [
            A * B
            for (A, B) in pairwise(devices_per_row)
        ]
        print(f'{beams=}')

        return sum(beams)

# NOTE: Acceptance Rate 85.6% (medium)

# NOTE: Runtime 191 ms Beats 19.78%
# NOTE: Memory 18.95 MB Beats 6.12%

# NOTE: re-ran for challenge:
# NOTE: Runtime 108 ms Beats 23.39%
# NOTE: Memory 19.87 MB Beats 7.41%
