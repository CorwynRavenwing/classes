class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:

        def calendar() -> List[str]:
            month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            return list([
                f'{m:02}-{d:02}'
                for m in range(1,12+1)
                for d in range(1,month_days[m-1]+1)
            ])
        
        C = calendar()
        # print(f'{C=}')
        AAindex = C.index(arriveAlice)
        LAindex = C.index(leaveAlice)
        ABindex = C.index(arriveBob)
        LBindex = C.index(leaveBob)
        Aindex = max(AAindex, ABindex)
        Lindex = min(LAindex, LBindex)
        together = C[Aindex:Lindex+1]
        print(f'[{Aindex}:{Lindex}] {together}')

        return len(together)

