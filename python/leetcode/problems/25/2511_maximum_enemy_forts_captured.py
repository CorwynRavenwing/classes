class Solution:
    def captureForts(self, forts: List[int]) -> int:
        print(f'{forts=}')

        if 1 not in forts:
            print("no forts under my control")
            return 0

        if -1 not in forts:
            print("no empty squares to move to")
            return 0

        fortsReversed = list(reversed(forts))
        print(f'{fortsReversed=}')

        possibles = []
        for F in [forts, fortsReversed]:
            myFortPos = -1
            while True:
                print(f"seek '1' at {myFortPos+1}:")
                try:
                    myFortPos = F.index(1, myFortPos+1)
                except ValueError:
                    print(f"  {'error'} -> none left")
                    break
                print(f"  seek '-1/1' at {myFortPos+1}:")
                try:
                    emptyPos = F.index(-1, myFortPos+1)
                except ValueError:
                    print(f"    {myFortPos=} {'error'} -> no landing zone")
                    break
                try:
                    myNextPos = F.index(1, myFortPos+1)
                    if myNextPos < emptyPos:
                        print(f"    {myFortPos=} {emptyPos=} {'error'} -> my fort blocks")
                        continue
                except ValueError:
                    pass
                this_block = F[myFortPos:emptyPos+1]
                print(f"    FOUND '{this_block}'")
                possibles.append(len(this_block) - 2)
        print(f'{possibles=}')
        return max(possibles)

