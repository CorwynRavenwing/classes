class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        def HHMM_to_minutes(HHMM: str) -> int:
            (HH, MM) = map(int, HHMM.split(':'))
            return HH * 60 + MM
        
        minutes = list(sorted(map(HHMM_to_minutes, timePoints)))
        minutes += [minutes[0]]     # wrap first number onto the end
        print(f'{minutes=}')
        diffs = [
            D % (24*60)
            # modulo minutes-in-a-day (not in problem description!)
            for (A, B) in pairwise(minutes)
            for D in [(A - B), (B - A)]
            # either positive or negative (not in problem description)
        ]
        print(f'{diffs=}')
        return min(diffs)

# NOTE: Runtime 74 ms Beats 40.18%
# NOTE: Memory 20.22 MB Beats 5.18%
