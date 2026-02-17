class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:

        def numbers_with_N_bits(N, maxVal):
            print(f"nwNb({N},{maxVal})")
            answers = []
            check = [(0, N, maxVal)]
            while check:
                (number, bitsLeft, val) = check.pop(0)
                # print(f"{number=}, {bitsLeft=}, {val=}")
                if bitsLeft == 0:
                    answers.append(number)
                    continue
                if val == 0:
                    # no way to use up the rest of the bits
                    continue
                check.extend([
                    (number + val, bitsLeft - 1, val // 2),
                    (number,       bitsLeft    , val // 2),
                ])
            return answers
        
        def filter_max(numbers: List[int], maximum: int) -> List[int]:
            numbers = [
                N
                for N in numbers
                if N <= maximum
            ]
            return tuple(sorted(numbers))

        def filter_hours(hours: List[int]) -> List[int]:
            return filter_max(hours, 11)

        def filter_minutes(minutes: List[int]) -> List[int]:
            return filter_max(minutes, 59)
        
        def format_time(T: Tuple[int, int]) -> str:
            (H, M) = T
            return f"{H}:{M:02}"

        def format_times(TT: List[Tuple[int, int]]) -> List[str]:
            return list(map(format_time, TT))

        # hours = (8, 4, 2, 1)
        # minutes = (32, 16, 8, 4, 2, 1)
        
        print(f"**{turnedOn=}")
        timeTuples = []
        for hourBits in range(0, 1 + min(4, turnedOn)):
            print(f"{hourBits=}")
            possible_hours = numbers_with_N_bits(hourBits, 8)
            print(f"  {possible_hours=}")
            possible_hours = filter_hours(possible_hours)
            print(f"  {possible_hours=}")

            minBits = turnedOn - hourBits
            print(f"  {minBits=}")
            possible_minutes = numbers_with_N_bits(minBits, 32)
            print(f"  {possible_minutes=}")
            possible_minutes = filter_minutes(possible_minutes)
            print(f"  {possible_minutes=}")
            TT = list([
                (H, M)
                for H in possible_hours
                for M in possible_minutes
            ])
            print(f"    {TT=}")
            timeTuples.extend(TT)
        print(f"    {timeTuples=}")

        return format_times(timeTuples)

# NOTE: Acceptance Rate 58.3% (easy)

# NOTE: re-ran for challenge:
# NOTE: Runtime 3 ms Beats 28.29%
# NOTE: Memory 19.57 MB Beats 13.49%
