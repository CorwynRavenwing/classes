class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        
        total_memory = memory1 + memory2

        # number whose triangle function "N*(N + 1)/2" is total_memory:
        max_seconds = int(math.sqrt(2 * total_memory))

        for i in range(max_seconds + 2):
            # starting range at 0 hurts nothing:
            # it subtracts zero, and prints a "before" record.
            if memory1 >= memory2 and memory1 >= i:
                memory1 -= i
            elif memory2 > memory1 and memory2 >= i:
                memory2 -= i
            else:
                print(f'{i}: CRASH!')
                break
            # print(f'{i}: {memory1},{memory2}')
        
        return (i, memory1, memory2)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 117 ms Beats 66.19%
# NOTE: Memory 17.42 MB Beats 6.21%
