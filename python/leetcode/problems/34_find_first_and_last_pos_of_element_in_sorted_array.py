class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        NOT_FOUND = [-1, -1]
        if not nums:
            return NOT_FOUND
        
        L = 0
        R = len(nums) - 1
        M = None
        left = nums[L]
        right = nums[R]
        while (left != right) and (L + 1 < R):
            M = (L + R) // 2
            mid = nums[M]
            print(f'= [{L},{M},{R}] = ({left},{mid},{right}) {target=}')
            if target < mid:
                print('  target in left half')
                (R,right) = (M,mid)
                continue
            elif target > mid:
                print('  target in right half')
                (L,left) = (M,mid)
                continue
            elif target == mid:
                ranges = ((L,left), (M,mid), (R,right))
                # find left end
                (A, B, C) = ranges
                (L, left) = A
                (M, mid) = B
                (R, right) = B  # ignore C
                while L + 1 < R:
                    M = (L + R) // 2
                    mid = nums[M]
                    print(f'< [{L},{M},{R}] = ({left},{mid},{right}) {target=}')
                    if target <= mid:
                        print('  target in left half')
                        if R == M:
                            print('    right half already missing')
                            break
                        (R, right) = (M, mid)
                        continue
                    elif target > mid:
                        print('  target in right half')
                        if M == L:
                            print('    left half already missing')
                            break
                        (L, left) = (M, mid)
                        continue
                    pass
                print(f'LEFT LOOP ENDED: [{L},{M},{R}] = ({left},{mid},{right}) {target=}')
                left_answer = L if left == target else R
                print(f'  LEFT ANSWER = {left_answer}')
                # find right end
                (A, B, C) = ranges
                (L, left) = B   # ignore A
                (M, mid) = B
                (R, right) = C
                while L + 1 < R:
                    M = (L + R) // 2
                    mid = nums[M]
                    print(f'> [{L},{M},{R}] = ({left},{mid},{right}) {target=}')
                    if target < mid:
                        print('  target in left half')
                        if R == M:
                            print('    right half already missing')
                            break
                        (R, right) = (M, mid)
                        continue
                    elif target >= mid:
                        print('  target in right half')
                        if M == L:
                            print('    left half already missing')
                            break
                        (L, left) = (M, mid)
                        continue
                    pass
                print(f'RIGHT LOOP ENDED: [{L},{M},{R}] = ({left},{mid},{right}) {target=}')
                right_answer = R if right == target else L 
                print(f'  RIGHT ANSWER = {right_answer}')
                return [left_answer, right_answer]

        print(f'X [{L},,{R}] = ({left},,{right}) {target=}')
        if left == target and target == right:
            return [L, R]
        elif left == target:
            return [L,L]
        elif target == right:
            return [R,R]
        else:
            return NOT_FOUND

