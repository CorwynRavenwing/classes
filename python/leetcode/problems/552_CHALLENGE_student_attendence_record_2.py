class Solution:
    def checkRecord(self, n: int) -> int:
        
        mod = 10 ** 9 + 7

        records = ((1, 0, 0, 'x'), (0, 0, 0, 'x'), ('x'))
        for day in range(n):
            # print(f'{day=} {records=}')
            (A0_old, A1_old, A2_ignore) = records
            (A0L0_old, A0L1_old, A0L2_old, A0L3_ignore) = A0_old
            (A1L0_old, A1L1_old, A1L2_old, A1L3_ignore) = A1_old

            # add a P for each record type:
            # resets all L values, doesn't change A values

            # add an A for each record type:
            # resets all L values, adds 1 to A value
            
            # add an L for each record type:
            # adds 1 to L value, does not change A value

            records = (
                (
                    sum([
                        A0L0_old, # +P
                        A0L1_old, # +P
                        A0L2_old, # +P
                    ]) % mod,
                    A0L0_old, # +L
                    A0L1_old, # +L
                    A0L2_old, # +L
                ),
                (
                    sum([
                        A1L0_old, # +P
                        A1L1_old, # +P
                        A1L2_old, # +P
                        A0L0_old, # +A
                        A0L1_old, # +A
                        A0L2_old, # +A
                    ])% mod,
                    A1L0_old, # +L
                    A1L1_old, # +L
                    A1L2_old, # +L # DISQUALIFIED
                ),
                (
                    sum([
                        A1L0_old, # +A # DISQUALIFIED
                        A1L1_old, # +A # DISQUALIFIED
                        A1L2_old, # +A # DISQUALIFIED
                    ]) % mod,
                    0,
                    0,
                ),
            )
        print(f'{n=} {records=}')
        # sums = tuple(map(sum, records))
        # print(f'{sums=}')
        answer = sum([
            sum(records[0][:3]),  # first 2 items in first group
            sum(records[1][:3]),  # first 2 items in second group
            # completely ignore third group
        ]) % mod
        return answer

