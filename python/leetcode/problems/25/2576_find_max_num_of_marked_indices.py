class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        
        def canMarkThisMany(target: int) -> bool:
            # print(f'TEST({target}):')
            k = (target // 2) + (target % 2)    # 3 and 4 both -> 2
            indexLeft = 0
            indexRight = k
            marks = 0
            while marks < target:
                if indexLeft >= k:
                    # print(f'  No: ran out of Left')
                    return False
                # print(f'? {indexLeft} {indexRight}')
                Left = nums[indexLeft]
                try:
                    while (Right := nums[indexRight]) < 2 * Left:
                        indexRight += 1
                except IndexError:
                    # print(f'  No: ran out of Right')
                    return False
                marks += 2
                # print(f'  Mark #{marks} [{indexLeft}]{Left} and [{indexRight}]{Right}')
                indexLeft += 1
                indexRight += 1
            return True

        nums.sort()
        
        L = 0
        left = canMarkThisMany(L)
        if not left:
            print(f'Strange, {L=} is false')
            return L
        R = len(nums) + 1
        right = canMarkThisMany(R)
        if right:
            print(f'Strange, {R=} is true')
            return -1
        print(f'[{L},{R}] ({left},{right})')
        while L + 1 < R:
            M = (L + R) // 2
            mid = canMarkThisMany(M)
            print(f'[{L},{M},{R}] ({left},{mid},{right})')
            if mid:
                print(f'  True: replace Left')
                (L, left) = (M, mid)
            else:
                print(f'  False: replace Right')
                (R, right) = (M, mid)

        print(f'[{L},{R}] ({left},{right})')
        # L is now the highest possible True value
        return L
# NOTE: Runtime 898 ms Beats 5.13%
# NOTE: Memory 31.22 MB Beats 68.59%
