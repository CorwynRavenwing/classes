class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:

        # first, the fact that it's a matrix is irrelevant,
        # since we can migrate negative numbers to anywhere we like

        flatten = [
            cell
            for row in matrix
            for cell in row
        ]
        flatten.sort()
        print(f'{flatten=}')
        negatives = [
            F
            for F in flatten
            if F < 0
        ]
        zeros = [
            F
            for F in flatten
            if F == 0
        ]
        positives = [
            F
            for F in flatten
            if F > 0
        ]
        print(f'{negatives=}')
        print(f'{zeros=}')
        print(f'{positives=}')
        even_negatives = (len(negatives) % 2 == 0)
        any_zeros = (len(zeros) > 0)

        least_negative = (negatives[-1] if negatives else 0)
        all_other_negatives = negatives[:-1]
        least_positive = (positives[0] if positives else 0)
        all_other_positives = positives[1:]

        sum_zeros = sum(zeros)
        print(f'{sum_zeros=}')
        assert sum_zeros == 0
        current_sum = sum(flatten)
        print(f'{current_sum=}')
        checksum = sum(positives) + least_negative + sum(all_other_negatives)
        print(f'{checksum=}')
        assert current_sum == checksum

        if positives and negatives:
            # only makes sense to swap these, if there are actually
            # both kinds of numbers available:
            if (- least_negative) > least_positive:
                # swap them
                all_other_negatives.append(least_negative)  # add LN back in
                positives = all_other_positives             # remove LP
                least_negative = (- least_positive)         # use LP as LN
                negatives.append(- least_positive)          # so LN + AON === N

        answer_with_one_remaining_negative = sum([
            sum(positives),
            least_negative,
            - sum(all_other_negatives),
        ])
        answer_fixing_everything = sum([
            sum(positives),
            - sum(negatives)
        ])

        if even_negatives:
            print('Even negatives:')
            print('  Move all the negatives around and cancel them all out')
            return answer_fixing_everything
        elif any_zeros:
            print('Odd negatives, but some zeros:')
            print('  Move all the negatives around, dropping the uncancelled negative on a zero')
            return answer_fixing_everything
        else:
            print('Odd negatives and no zeros:')
            print('  Cancel out all the negatives but one.')
            print('  Leave the least magnitude number of any sort (+/-) being negative')
            # print(f'+ {positives}')
            # print(f'+ {least_negative}')
            # print(f'- {all_other_negatives}')
            return answer_with_one_remaining_negative

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 177 ms Beats 5.33%
# NOTE: Memory 27.08 MB Beats 6.16%
