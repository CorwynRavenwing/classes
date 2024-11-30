class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:

        # make each one hashable
        pairs = list(map(tuple, pairs))
        pairs.sort()
        # print(f'{pairs=}')

        (all_starts, all_ends) = zip(*pairs)
        # print(f'{all_starts=}')
        # print(f'{all_ends  =}')

        start_counts = Counter(all_starts)
        end_counts = Counter(all_ends)
        # print(f'{start_counts=}')
        # print(f'{end_counts  =}')
        
        free_start = start_counts - end_counts
        free_end = end_counts - start_counts
        # print(f'{free_start=}')
        # print(f'{free_end  =}')

        assert len(free_start) < 2  # else constraints are violated
        assert len(free_end) < 2    # ditto
        assert len(free_start) == len(free_end)     # also ditto

        def find_pair_beginning_with(value: int) -> int:
            # returns index if found, or None if not
            if not pairs:
                return None
            match = (value, 0)
            index = bisect_left(pairs, match)
            # print(f'{value=}: found {match} at {index=}')
            try:
                (startI, toI) = pairs[index]
            except IndexError:
                # index fell off end of array: match not found
                return None
            return (
                index
                if startI == value
                else None
            )

        def pop_pair_beginning_with(value: int) -> Tuple[int,int]:
            nonlocal pairs
            index = find_pair_beginning_with(value)
            return (
                pairs.pop(index)
                if index is not None
                else None
            )
        
        def extract_chain_beginning_with(value: int) -> List[Tuple[int,int]]:
            nonlocal pairs
            answer = []
            prev_end = value
            while pairs:
                element = pop_pair_beginning_with(prev_end)
                if element is None:
                    break
                answer.append(element)
                (prev_start, prev_end) = element
            return answer

        answer_front = []
        answer_back = []
        if len(free_start) == 0:
            # pick any arbitrary element
            element = pairs.pop(0)
        else:
            # there is one specific start element
            value = tuple(free_start.keys())[0]
            element = pop_pair_beginning_with(value)
        # print(f'{element=} {pairs=}')

        answer_front.append(element)
        while pairs:
            (prev_start, prev_end) = answer_front[-1]
            # print(f'{answer_front=}({prev_end}){answer_back} | {pairs=}')
            new_loop = extract_chain_beginning_with(prev_end)
            if new_loop:
                answer_back = new_loop + answer_back    # push it onto the front
                continue
            else:
                # nothing matched: move one element from "back" to "front"
                element = answer_back.pop(0)
                answer_front.append(element)
                continue

        answer = answer_front + answer_back
        return answer

# NOTE: Acceptance Rate 46.3% (HARD)
# NOTE: Runtime 2304 ms Beats 5.43%
# NOTE: Memory 71.22 MB Beats 100.00%
