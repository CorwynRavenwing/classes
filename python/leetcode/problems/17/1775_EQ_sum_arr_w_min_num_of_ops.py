class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        
        C1 = Counter(nums1)
        C2 = Counter(nums2)
        T1 = sum(nums1)
        T2 = sum(nums2)
        L1 = len(nums1)
        L2 = len(nums2)
        
        if T1 == T2:
            return 0

        (min1, max1) = (L1 * 1, L1 * 6)
        (min2, max2) = (L2 * 1, L2 * 6)
        if (max1 < min2) or (max2 < min1):
            print(f'({min1},{T1},{max1}) and ({min2},{T2},{max2}) are disjoint')
            return -1
            
        # WLOG make T1 the lower number
        if T1 > T2:
            (T1, T2) = (T2, T1)
            (C1, C2) = (C2, C1)
        
        answer = 0
        diff = T2 - T1
        # range(5) so we skip moving 6 -> 6 and 1-> 1 
        for i in range(5):
            num1 = 1 + i
            num2 = 6 - i

            print(f'{diff}: {T1} {T2}')
            print(f'  {C1=} {C2=}')
            if not diff:
                break
            count = C1[num1]
            if count:
                print(f'  Try {count} "{num1}" -> "{6}"')
                maxChange = count * (6 - num1)
                if maxChange <= diff:
                    answer += count
                    C1[num1] -= count
                    C1[6] += count
                    T1 += maxChange
                    diff -= maxChange
                    print(f'  A: Added {count=} to {answer=} and moved C1[{num1}] -> C1[{6}]')
                    print(f'  A: Added {maxChange=} to {T1=} and subtracted it from {diff=}')
                else:
                    count = diff // (6 - num1)
                    maxChange = count * (6 - num1)
                    assert maxChange <= diff
                    answer += count
                    C1[num1] -= count
                    C1[6] += count
                    T1 += maxChange
                    diff -= maxChange
                    print(f'  B: Added {count=} to {answer=} and moved C1[{num1}] -> C1[{6}]')
                    print(f'  B: Added {maxChange=} to {T1=} and subtracted it from {diff=}')
                    if diff:
                        print(f'{T1=} {T2=} {diff=}')
                        assert diff < 5
                        assert diff < (6 - num1)
                        # newnum = 6 - diff
                        newnum = num1 - diff
                        # print(f'{newnum} = 6 - {diff} ???')
                        print(f'{newnum} = {num1=} - {diff} ???')
                        count = 1
                        maxChange = num1 - newnum
                        print(f'{maxChange=} = {num1=} - {newnum=}')
                        answer += count
                        C1[num1] -= count
                        C1[newnum] += count
                        T1 += maxChange
                        diff -= maxChange
                        print(f'  C: Added {count=} to {answer=} and moved C1[{num1}] -> C1[{newnum}]')
                        print(f'  C: Added {maxChange=} to {T1=} and subtracted it from {diff=}')
                    assert diff == 0
                    break

            print(f'{diff}: {T1} {T2}')
            print(f'  {C1=} {C2=}')
            if not diff:
                break
            count = C2[num2]
            if count:
                print(f'  Try {count} "{num2}" -> "{1}"')
                maxChange = count * (num2 - 1)
                if maxChange <= diff:
                    answer += count
                    C2[num2] -= count
                    C2[1] += count
                    T2 -= maxChange
                    diff -= maxChange
                    print(f'  D: Added {count=} to {answer=} and moved C2[{num2}] -> C2[{1}]')
                    print(f'  D: Subtracted {maxChange=} from {T2=} and {diff=}')
                else:
                    count = diff // (num2 - 1)
                    maxChange = count * (num2 - 1)
                    assert maxChange <= diff
                    answer += count
                    C2[num2] -= count
                    C2[1] += count
                    T2 -= maxChange
                    diff -= maxChange
                    print(f'  E: Added {count=} to {answer=} and moved C2[{num2}] -> C2[{1}]')
                    print(f'  E: Subtracted {maxChange=} from {T2=} and {diff=}')
                    if diff:
                        print(f'{T1=} {T2=} {diff=}')
                        assert diff < 5
                        assert diff < (num2 - 1)
                        newnum = num2 - diff    # *** unsure of this number
                        print(f'{newnum} = {num2=} - {diff} ???')
                        count = 1
                        maxChange = num2 - newnum
                        print(f'{maxChange=} = {num2=} - {newnum=}')
                        answer += count
                        C2[num2] -= count
                        C2[newnum] += count
                        T2 -= maxChange
                        diff -= maxChange
                        print(f'  F: Added {count=} to {answer=} and moved C2[{num2}] -> C2[{newnum}]')
                        print(f'  F: Subtracted {maxChange=} from {T2=} and {diff=}')
                    assert diff == 0
                    break

        return answer

# NOTE: Accepted on second Submit (edge case)
# NOTE: Runtime 31 ms Beats 98.11%
# NOTE: Memory 21.88 MB Beats 63.50%
