class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        
        bucket = {0: [], 1: [], 2: []}
        total = 0
        for D in digits:
            bucket[D % 3].append(str(D))
            total += D
        mode = total % 3

        print(f'{mode=}')
        for B in range(3):
            bucket[B].sort()
            print(f'bucket[{B}]={bucket[B]}')
        
        if mode == 0:
            print(f'mode 0: No changes')
            pass

        elif mode == 1:
            if len(bucket[1]) >= 1:
                discard = []
                discard.append(bucket[1].pop(0))
                print(f'mode 1: {discard=} from bucket 1')
            elif len(bucket[2]) >= 2:
                discard = []
                discard.append(bucket[2].pop(0))
                discard.append(bucket[2].pop(0))
                print(f'mode 1: {discard=} from bucket 2')
            else:
                print(f'mode 1: FAIL')
                return ""

        elif mode == 2:
            if len(bucket[2]) >= 1:
                discard = []
                discard.append(bucket[2].pop(0))
                print(f'mode 2: {discard=} from bucket 2')
            elif len(bucket[1]) >= 2:
                discard = []
                discard.append(bucket[1].pop(0))
                discard.append(bucket[1].pop(0))
                print(f'mode 2: {discard=} from bucket 1')
            else:
                print(f'mode 2: FAIL')
                return ""

        else:
            assert mode in (0, 1, 2)
        
        print(f'AFTER:')
        digits_left = []
        for B in range(3):
            print(f'bucket[{B}]={bucket[B]}')
            digits_left.extend(bucket[B])
        
        digits_left.sort(reverse=True)
        answer = ''.join(digits_left)

        if len(answer) == 0:
            return answer

        while answer[:1] == "0":
            print(f'{answer=}: trim leading zero')
            answer = answer[1:]
        
        if len(answer) == 0:
            print(f'{answer=} put one zero back')
            return "0"
        
        return answer

# NOTE: Acceptance Rate 33.5% (HARD)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (edge case with multiple leading zeros)
# NOTE: Runtime 31 ms Beats 9.48%
# NOTE: Memory 20.36 MB Beats 12.93%
