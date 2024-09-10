class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        
        # we borrow some code from #443:

        groups = []
        number = 1

        for readI, C in enumerate(s):
            atEndOfList = ((readI + 1) >= len(s))
            nextC = ('-' if atEndOfList else s[readI + 1])
            nextCDifferent = (C != nextC)
            if nextCDifferent:
                print(f'{readI=} "{nextC}" "{C}" x {number}')
                toWrite = [C]
                if number > 1:
                    toWrite += list(str(number))
                groups.append(
                    (C, number, len(toWrite))
                )
                number = 1
            else:
                number += 1

        print(f'{groups=}')
        length_without_deletions = sum(
            length
            for (char, count, length) in groups
        )
        print(f'{length_without_deletions=}')

        @cache
        def useful_numbers_to_delete(N: int) -> Set[int]:
            # print(f'UNTD({N}):')
            answers = {0, N}    # delete everything, delete nothing
            if N > 1:
                answers.add(N-1)    # delete all but one: len("a") < len("a2")
            # print(f'  {answers=}')
            length = len(str(N))
            for new_len in range(1, length):
                new_num = int('9' * new_len)
                diff = N - new_num
                # print(f'    +{new_len=} {new_num=} {diff=}')
                answers.add(diff)
            return answers
        
        @cache
        def useful_numbers_under_K(N: int, K: int) -> Set[int]:
            # print(f'UNUK({N},{K}):')
            return {
                num
                for num in useful_numbers_to_delete(N)
                if num <= K
            }
        
        possibles = {
            # we start with only one possibility:
            (
                0,      # length so far
                k,      # K characters left to delete
                '-',    # last character used: something impossible
                0,      # count of last character
                0,      # length of last group
            )
        }

        for G in groups:
            print(f'{G=}')
            (char, immutable_count, length) = G
            new_possibles = set()
            for P in possibles:
                count = immutable_count
                # print(f'  {P=}')
                (
                    length_so_far,
                    remaining_k,
                    prior_char,
                    prior_count,
                    prior_length, 
                ) = P
                allow_delete_all = True
                if char == prior_char:
                    # print(f'    Merge prior group into this one')
                    length_so_far -= prior_length
                    count += prior_count
                    allow_delete_all = False
                    # print(f'    ({length_so_far=})')
                    # print(f'    ({count=})')
                delete_options = useful_numbers_under_K(count, remaining_k)
                # print(f'    {delete_options=}')
                for D in delete_options:
                    trial_count = count - D
                    # print(f'    {D=} {trial_count=}')
                    
                    if trial_count == 0:
                        if not allow_delete_all:
                            # print(f'      Cannot delete all {count} "{char}"')
                            pass
                        
                        else:
                            # print(f'      Deleted all {count} "{char}"')
                            Q = (
                                length_so_far,
                                remaining_k - D,
                                prior_char,
                                prior_count,
                                prior_length,
                            )
                            # print(f'      {Q=}')
                            new_possibles.add(Q)
                        continue

                    trial_length = 1 + (
                        0
                        if trial_count == 1
                        else len(str(trial_count))
                    )
                    Q = (
                        length_so_far + trial_length,
                        remaining_k - D,
                        char,
                        trial_count,
                        trial_length,
                    )
                    # print(f'      {Q=}')
                    new_possibles.add(Q)
            possibles = new_possibles

        print(f'DONE')
        print(f'{possibles=}')

        return min([
            length
            for (length, remaining_k, prior_char, prior_count, prior_length) in possibles
        ])

# NOTE: Runtime 7740 ms Beats 5.24%
# NOTE: Memory 29.56 MB Beats 64.29%
