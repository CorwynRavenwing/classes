class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        
        counts = Counter(tasks)

        if 1 in counts.values():
            return -1
        
        @cache
        def count_to_rounds(count: int) -> int:
            print(f'CTR({count}):')
            answer = 0
            while count:
                mod = count % 3
                if mod == 0:
                    print(f'  take all {count}')
                    answer += count // 3
                    count = 0
                else:
                    answer += 1
                    print(f'  take 2 from {count}')
                    count -= 2

            return answer
        
        answer = 0
        for (task, count) in counts.items():
            answer += count_to_rounds(count)
        
        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Time Limit Exceeded)
# NOTE: Runtime 35 ms Beats 90.80%
# NOTE: Memory 33.18 MB Beats 54.48%
