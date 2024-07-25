class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(A: List[int], B: List[int]) -> List[int]:
            answer = []
            while A and B:
                if A[0] <= B[0]:
                    answer.append(A.pop(0))
                else:
                    answer.append(B.pop(0))
            answer.extend(A)
            answer.extend(B)
            return answer
        
        print(f'sortArray({len(nums)})')

        if min(nums) == max(nums):
            return nums
        
        if len(nums) <= 1:
            return nums
        
        midpoint = len(nums) // 2
        
        left = nums[:midpoint]
        right = nums[midpoint:]

        sortedLeft = self.sortArray(left)
        sortedRight = self.sortArray(right)

        return merge(sortedLeft, sortedRight)

