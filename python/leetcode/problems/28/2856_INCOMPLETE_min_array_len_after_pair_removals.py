class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        
        counts = Counter(nums)
        while counts:
            # print(f'DEBUG: {counts=}')
            counts_sorted = tuple(sorted([
                (count, value)
                for value, count in counts.items()
            ]))
            # print(f'{counts_sorted=}')
            (first_count, first_value) = counts_sorted[-1]
            if len(counts_sorted) == 1:
                print(f'All one kind of number ({first_count} * "{first_value}")')
                return first_count
            (second_count, second_value) = counts_sorted[-2]
            if first_count == 1:
                print(f'Max count == 1: delete pairs')
                if len(counts_sorted) % 2 == 0:
                    print(f'  ... even number: delete all')
                    return 0
                else:
                    print(f'  ... odd number: delete all but one')
                    return 1
            if second_count == 1:
                # case like [1 1 1 1 1 2 3 4 5 6]
                count_of_ones = len(counts_sorted) - 1  # all but the "first_count" one
                if count_of_ones <= first_count:
                    print(f'  delete {count_of_ones} singletons and decrement "{first_value}"')
                    counts = Counter()
                    counts[first_value] = first_count - count_of_ones
                    if not counts[first_value]:
                        del counts[first_value]
                    continue
                else:
                    print(f'  delete {first_count} singletons and all of "{first_value}"')
                    counts_sorted = counts_sorted[first_count:-1]
                    counts = Counter([
                        value
                        for (count, value) in counts_sorted
                    ])
                    continue
                    
            print(f'  delete 1 from {first_value}, {second_value}')
            counts[first_value] -= 1
            if not counts[first_value]:
                del counts[first_value]
            counts[second_value] -= 1
            if not counts[second_value]:
                del counts[second_value]

        return 0
# NOTE: Time Limit Exceeded for large inputs
# NOTE: should work the tuple list and avoid recreating it
