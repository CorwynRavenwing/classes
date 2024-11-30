class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        # we borrow some code from #2097:

        # make each one hashable
        tickets = list(map(tuple, tickets))
        tickets.sort()

        (all_starts, all_ends) = zip(*tickets)

        start_counts = Counter(all_starts)
        end_counts = Counter(all_ends)
        
        free_start = start_counts - end_counts
        free_end = end_counts - start_counts

        def find_pair_beginning_with(value: int) -> int:
            # returns index if found, or None if not
            if not tickets:
                return None
            match = (value, '')
            index = bisect_left(tickets, match)
            # print(f'{value=}: found {match} at {index=}')
            try:
                (startI, toI) = tickets[index]
            except IndexError:
                # index fell off end of array: match not found
                return None
            return (
                index
                if startI == value
                else None
            )

        def pop_pair_beginning_with(value: int) -> Tuple[int,int]:
            nonlocal tickets
            index = find_pair_beginning_with(value)
            return (
                tickets.pop(index)
                if index is not None
                else None
            )
        
        def extract_chain_beginning_with(value: int) -> List[Tuple[int,int]]:
            nonlocal tickets
            answer = []
            prev_end = value
            while tickets:
                element = pop_pair_beginning_with(prev_end)
                if element is None:
                    break
                answer.append(element)
                (prev_start, prev_end) = element
            return answer

        answer_front = []
        answer_back = []

        # there is one specific start element
        value = 'JFK'
        element = pop_pair_beginning_with(value)

        answer_front.append(element)
        while tickets:
            (prev_start, prev_end) = answer_front[-1]
            # print(f'{answer_front=}({prev_end}){answer_back} | {tickets=}')
            new_loop = extract_chain_beginning_with(prev_end)
            if new_loop:
                answer_back = new_loop + answer_back    # push it onto the front
                continue
            else:
                # nothing matched: move one element from "back" to "front"
                if not answer_back:
                    print(f'  ERROR: out of flights!')
                    break
                element = answer_back.pop(0)
                answer_front.append(element)
                continue

        answer = answer_front + answer_back
        A0, B0 = answer[0]
        clean_answer = [A0] + [
            B
            for A, B in answer
        ]
        return clean_answer

# NOTE: Acceptance Rate 43.3% (HARD)
# NOTE: gets wrong answer for some inputs.  Needs work.
