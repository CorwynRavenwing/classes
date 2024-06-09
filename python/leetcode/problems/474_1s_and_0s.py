class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counters = [
            Counter(S)
            for S in strs
        ]
        numbers = [
            (C['0'], C['1'])
            for C in counters
        ]
        print(f'{numbers=}')

        states = {(0, m, n)}  # length, 0's allowed, 1's allowed
        for (zeros, ones) in numbers:
            print(f'{len(states)} states + {(zeros, ones)}')
            new_states = set([
                (length + 1, zeros_left - zeros, ones_left - ones)
                for (length, zeros_left, ones_left) in states
            ])
            new_states = set([
                (length, zeros_left, ones_left)
                for (length, zeros_left, ones_left) in new_states
                if (zeros_left >= 0) and (ones_left >= 0)
            ])
            print(f'  add {len(new_states)} new states')
            states |= new_states

        # print(f'{states=}')
        max_length = max([
            length
            for (length, zeros_left, ones_left) in states
        ])

        return max_length

# NOTE: 630 ms; Beats 98.17% of users with Python3
