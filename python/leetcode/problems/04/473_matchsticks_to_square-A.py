class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        side_length = None

        def calculateNeeds(configuration: List[List[int]]) -> List[int]:
            nonlocal side_length
            return [
                side_length - sum(side_list)
                for side_list in configuration
            ]

        total = sum(matchsticks)
        print(f'{total=}')
        if total % 4 != 0:
            print(f'  not divisible by 4!')
            return False
        
        side_length = total // 4
        print(f'{side_length=}')

        sides = ([], [], [], [])
        matchsticks.sort()
        while matchsticks:
            print(f'{sides=} {matchsticks=}')
            stick = matchsticks.pop()   # start at highest
            if stick > side_length:
                print(f'  {stick=} too big!  > {side_length}')
                return False
            if stick == side_length:
                print(f'  {stick=} entire {side_length=}')
                if [] in sides:
                    index = sides.index([])
                    sides[index].append(stick)
                    continue
                else:
                    print(f'    Nowhere to put it!')
                    print(f'    {sides=}')
                    return False
            if (stick * 2) >= side_length:
                print(f'  {stick=} >= half sidelength ({side_length / 2})')
                if [] in sides:
                    index = sides.index([])
                    sides[index].append(stick)
                    need = side_length - stick
                    if need in matchsticks:
                        print(f'    found the other half: {need}')
                        sides[index].append(need)
                        matchsticks.remove(need)
                        continue
                    possible = [
                        S
                        for S in matchsticks
                        if S <= need
                    ]
                    if not possible:
                        print(f'  nothing small enough for {need}')
                        return False
                    
                    continue
                else:
                    print(f'    Nowhere to put it!')
                    print(f'    {sides=}')
                    return False
            print(f'    Put {stick}, and all smaller, aside for later')
            matchsticks.append(stick)   # we had popped it: put it back
            break
        #
        print(f'{sides=} {matchsticks=}')
        if not matchsticks:
            return True

        for side_list in sides:
            need = side_length - sum(side_list)
            if not need:
                continue
            possible = [
                S
                for S in matchsticks
                if S <= need
            ]
            if not possible:
                print(f'{side_list=} {matchsticks=}')
                print(f'  nothing small enough for {need}')
                return False
        
        reachable_numbers = {0}
        # print(f'reachable numbers:\n  {reachable_numbers}')
        for stick in matchsticks:
            new_reachable = set([
                RN + stick
                for RN in reachable_numbers
                if RN + stick <= side_length
            ])
            # print(f'  {new_reachable}')
            reachable_numbers |= new_reachable  # union operator
        # print(f'all reachable: {reachable_numbers}')

        print(f'\n... "later"')
        to_check = [sides]
        while matchsticks:
            print(f'\n#####\n\nto_check={len(to_check)} {matchsticks=}')
            stick = matchsticks.pop()   # start at highest
            print(f'\n{stick=}')
            new_to_check = []
            already_skipping = []
            for sides_check in to_check:
                old_needs = calculateNeeds(sides_check)
                print(f'\n  {sides_check} needs={old_needs}')
                if stick in old_needs:
                    index = old_needs.index(stick)
                    new_sides = sides_check
                    new_sides[index].append(stick)
                    needs = calculateNeeds(new_sides)
                    print(f'    =>{new_sides} {needs=}')
                    if new_sides not in new_to_check:
                        new_to_check.append(new_sides)
                    else:
                        print(f'      DUP')
                    # and don't try any other location for "stick"
                    continue
                # else, try all four locations
                (A, B, C, D) = sides_check
                T = [stick]
                new_check = [
                    (A+T, B, C, D),
                    (A, B+T, C, D),
                    (A, B, C+T, D),
                    (A, B, C, D+T),
                ]
                # but new_check might include some with sides that are too long: so,
                for new_sides in new_check:
                    new_sides = tuple(sorted(new_sides, reverse=True))
                    if new_sides in new_to_check:
                        # print(f'    (DUP)')
                        continue
                    if new_sides in already_skipping:
                        # print(f'    [DUP]')
                        continue
                    needs = calculateNeeds(new_sides)
                    if any([
                        need < 0
                        for need in needs
                    ]):
                        already_skipping.append(new_sides)
                        # print(f'      discard: side too long')
                        continue
                    print(f'    ->{new_sides} {needs=}')
                    unreachable = [
                        N
                        for N in needs
                        if N not in reachable_numbers
                    ]
                    if unreachable:
                        print(f'      SKIP: {unreachable=}')
                        already_skipping.append(new_sides)
                        continue
                    if new_sides not in new_to_check:
                        new_to_check.append(new_sides)
                    else:
                        print(f'      DUP')
            to_check = new_to_check
        
        print(f'check answers:')
        for sides_check in to_check:
            needs = calculateNeeds(sides_check)
            print(f'  {sides_check} {needs=}')
            if needs == [0,0,0,0]:
                return True

        return False

# NOTE: works usually, but has occasional failures.
