class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        def is_distict_starting_at(index: int) -> bool:
            frag = nums[index:]
            counter = Counter(frag)
            print(f'{index}: {counter}')
            if not frag:
                return True
            counts = set(counter.values())
            # print(f'  {counts=}')
            counts -= {1}
            # print(f'  {counts=}')
            return (len(counts) == 0)
        
        not_distinct_starting_at = lambda x: not is_distict_starting_at(x)

        answer = 0
        index = 0
        while not_distinct_starting_at(index):
            answer += 1
            index += 3
        
        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 63 ms Beats 5.10%
# NOTE: Memory 18.08 MB Beats 9.05%
