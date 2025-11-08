class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        
        def x_sum(frag: List[int]) -> int:
            # print(f'x_sum({frag}):')
            count = Counter(frag)
            # print(f'  {count=}')
            data = [
                (freq, num)
                for (num, freq) in count.items()]
            data.sort(reverse=True)
            data = data[:x]
            # print(f'  {data=}')
            sums = [
                freq * num
                for (freq, num) in data
            ]
            # print(f'  {sums=}')
            return sum(sums)

        answer = []

        for i in range(len(nums) - k + 1):
            frag = nums[i:i+k]
            # print(f'[{i}:{i+k}] {frag}')
            answer.append(
                x_sum(frag)
            )

        return answer

# NOTE: Acceptance Rate 25.0% (HARD)

# NOTE: TLE for large inputs
