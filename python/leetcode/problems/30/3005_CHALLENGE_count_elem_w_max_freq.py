class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        counts = Counter(nums)
        print(f'{counts=}')

        freq = tuple(counts.values())
        print(f'{freq=}')

        freq_count = Counter(freq)
        print(f'{freq_count=}')

        max_freq = max(freq)
        answer = max_freq * freq_count[max_freq]
        print(f'{answer} =  {max_freq} * {freq_count[max_freq]}')
        return answer

# NOTE: Acceptance Rate 78.0% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 8 ms Beats 3.13%
# NOTE: Memory 17.87 MB Beats 34.33%
