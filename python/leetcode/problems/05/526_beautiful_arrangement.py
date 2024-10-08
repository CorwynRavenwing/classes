class Solution:
    def countArrangement(self, n: int) -> int:
        # Dict[int,Set[int]]
        legal_locations = {
            1 : {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16},
            2 : {1,2,4,6,8,10,12,14,16},
            3 : {1,3,6,9,12,15},
            4 : {1,2,4,8,12,16},
            5 : {1,5,10,15},
            6 : {1,2,3,6,12},
            7 : {1,7,14},
            8 : {1,2,4,8,16},
            9 : {1,3,9},
            10: {1,2,5,10},
            11: {1,11},
            12: {1,2,3,4,6,12},
            13: {1,13},
            14: {1,2,7,14},
            15: {1,3,5,15},
            16: {1,2,4,8,16},
        }
        location_counts = [
            (value, len(locations))
            for value, locations in legal_locations.items()
        ]
        print(f'{location_counts=}')
        values_by_location_count = [
            value
            for (value, location_count) in sorted(
                location_counts,
                key=lambda x: x[1]      # sort by count_of_locations
            )
        ]
        print(f'{values_by_location_count=}')
        bitmasks = {0: 1}
        print(f'Bitmasks:')
        print('\n'.join([
            f'\t{B:0{n}b}({count})'
            for B, count in bitmasks.items()
        ]))
        for v in values_by_location_count:
            # print(f'{v=}')
            if v > n:
                # print(f'  (skip)')
                continue
            print(f'{v=}')
            new_bitmasks = defaultdict(int)
            for B, count in bitmasks.items():
                for location in legal_locations[v]:
                    # print(f'  Try {B:0{n}b} + {location} ({count}):')
                    if location > n:
                        # print(f'      (skip)')
                        continue
                    # print(f'  Try {B:0{n}b} + {location} ({count}):')
                    bit = 1 << (location - 1)
                    # print(f'  Loc {bit:0{n}b}')
                    if B & bit:
                        # print(f'      (crash)')
                        continue
                    else:
                        newB = B | bit
                        # print(f'  OK: {newB:0{n}b}')
                        # print(f'  ' + ('-' * 20))
                        new_bitmasks[newB] += count
            bitmasks = new_bitmasks
            print(f'Bitmasks:')
            print('\n'.join([
                f'\t{B:0{n}b}({count})'
                for B, count in bitmasks.items()
            ]))
        
        bitmask_data = tuple(bitmasks.items())
        assert len(bitmask_data) == 1
        only_bitmask = bitmask_data[0]
        only_count = only_bitmask[1]
        return only_count

# NOTE: Accepted on first Submit
# NOTE: Runtime 47 ms Beats 98.46%
# NOTE: Memory 16.92 MB Beats 15.35%
