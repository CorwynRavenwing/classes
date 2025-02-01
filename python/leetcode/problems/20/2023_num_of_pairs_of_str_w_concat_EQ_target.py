class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:

        counts = Counter(nums)

        answer = 0
        for (A, countA) in counts.items():
            if not target.startswith(A):
                print(f'No: doesnt start with "{A}"')
                continue

            B = target[len(A):]
            otherNums = counts - Counter([A])
            print(f'  (DEBUG: {otherNums=}')
            countB = otherNums[B]
            if not countB:
                print(f'No: "{B}" not in other nums')
            
            print(f'Yes: "{A}" + "{B}", {countA} * {countB}')
            answer += countA * countB
        
        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 20 ms Beats 21.57%
# NOTE: Memory 18.16 MB Beats 18.43%
