class Solution:
    def maxOperations(self, s: str) -> int:

        letters_and_counts = [
            (key, len(tuple(values)))
            for key, values in groupby(s)
        ]
        print(f'{letters_and_counts=}')

        try:
            # delete 0 from first position
            (key, count) = letters_and_counts[0]
            if key == '0':
                print(f'Delete 0 from first position')
                del letters_and_counts[0]
            
            # delte 1 from last position
            (key, count) = letters_and_counts[-1]
            if key == '1':
                print(f'Delete 1 from last position')
                del letters_and_counts[-1]
        except IndexError:
            print(f'No relevant data')
            return 0
        
        one_counts = [
            count
            for (key, count) in letters_and_counts
            if key == '1'
        ]
        print(f'{one_counts=}')

        # each group is counted, then counted again as part of the
        # following group, and so forth.
        partialSums = tuple(accumulate(one_counts))
        print(f'{partialSums=}')

        return sum(partialSums)

# NOTE: Accepted on first Submit
# NOTE: Runtime 245 ms Beats 5.00%
# NOTE: Memory 24.21 MB Beats 5.22%
