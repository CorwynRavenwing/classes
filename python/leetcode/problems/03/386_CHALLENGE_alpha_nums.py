class Solution:
    def lexicalOrder(self, n: int) -> List[int]:

        def LO_beginning_with(begin: int, maximum: int) -> List[int]:
            print(f'LO_BW({begin},{maximum})')
            if begin > maximum:
                print(f'  -> []')
                return []
            range_begin = 10 * begin
            range_end = min(range_begin + 9, maximum)
            if range_begin:
                answer_this_size = [begin]
            else:
                answer_this_size = []   # skip 0
                range_begin += 1        # start at 1
            if range_begin > maximum:
                print(f'  -> {answer_this_size}')
                return answer_this_size
            print(f'  {range_begin} .. {range_end}')
            answers_larger = [
                flatten
                for NN in range(range_begin, range_end + 1)
                for flatten in LO_beginning_with(NN, maximum)
            ]
            print(f'  -> {answer_this_size} + {answers_larger}')
            return answer_this_size + answers_larger
        
        return LO_beginning_with(0, n)

# NOTE: Accepted on first Submit
# NOTE: Runtime
228ms
Beats5.02%
# NOTE: O(N)
# NOTE: Memory
22.73MB
Beats46.00%
# NOTE: O(N)
