class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        side_length = None

        def use_matches(method: List[int], matches_available: List[int]) -> List[int]:
            retval = matches_available.copy()
            for M in method:
                if M in retval:
                    retval.remove(M)
                else:
                    # print(f'USE(): missing {M}')
                    return None
            return retval

        total = sum(matchsticks)
        print(f'{total=}')
        if total % 4 != 0:
            print(f'  not divisible by 4!')
            return False
        
        side_length = total // 4
        print(f'{side_length=}')

        matchsticks.sort()
        reachable_numbers = {(0, ())}   # a list of no matches sums to length 0
        # print(f'reachable numbers:\n  {reachable_numbers}')
        for stick in matchsticks:
            # print(f'{stick=}')
            new_reachable = set([
                (RN + stick, combo + (stick,))
                for (RN, combo) in reachable_numbers
                if RN + stick <= side_length
            ])
            # print(f'  nr={new_reachable}')
            reachable_numbers |= new_reachable  # union operator
        # print(f'reachable: {reachable_numbers}')
        side_length_methods = [
            combo
            for (RN, combo) in reachable_numbers
            if RN == side_length
        ]
        # print(f'ways of getting {side_length}: {side_length_methods}')

        if not side_length_methods:
            print(f'No way to do it!')
            return False
        
        to_check = [
            (0, [], matchsticks)
        ]

        while to_check:
            check = to_check.pop(0)
            print(f'{check=}')
            (lowest_index, sides_so_far, matches_available) = check
            if len(sides_so_far) == 4:
                if not matches_available:
                    print(f'  SUCCESS: {sides_so_far}')
                    return True
            if not matches_available:
                print(f'  Out of matches')
                continue
            for index, method in enumerate(side_length_methods):
                if index < lowest_index:
                    # print(f'    skip: {index} < {lowest_index}')
                    continue
                matches_left = use_matches(method, matches_available)
                if matches_left is None:
                    # print(f'    skip: missing some matches')
                    continue
                print(f'  method[{index}]: {method}')
                to_check.append(
                    (index, sides_so_far + [method], matches_left)
                )

        print(f'ran out of possible answers')
        return False

# NOTE: a much cleaner version which runs a ton faster
