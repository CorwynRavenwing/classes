class Solution:
    def minOperations(self, n: int) -> int:
        
        # NOTE: if a bit is not set, do nothing.
        # If a bit is set, and the bit to its left is not set, subtract it.
        # If a bit is set, and the bit to its left is also set, add it.
        # it will cascade upward to give you fewer total add/subtractions.

        binary = f'{n:b}'
        bits = tuple(map(int, binary))
        bitsRev = list(reversed(bits))
        print(f'{n}: {binary} {bits} {bitsRev}')

        answer = 0
        while bitsRev:
            print(f'LOOP: {bitsRev}')
            if bitsRev[0] == 0:
                # this bit is 0
                _ = bitsRev.pop(0)
                print(f'skip 0')
                continue
            # else this bit is 1
            if (len(bitsRev) <= 1) or (bitsRev[1] == 0):
                # next bit is zero or nonexistent
                _ = bitsRev.pop(0)
                print(f'Subtract')
                answer += 1
                continue
            # else next bit is also 1
            print(f'Add')
            answer += 1
            while bitsRev and bitsRev[0] == 1:
                _ = bitsRev.pop(0)
                print(f'  carry ...')
            if bitsRev:
                assert bitsRev[0] == 0
                bitsRev[0] = 1
                print(f'  Done (A)')
            else:
                bitsRev.append(1)
                print(f'  Done (B)')
            continue

        return answer

# NOTE: Acceptance Rate 57.6% (medium)

# NOTE: Accepted on fourth Run (carry to new digit; tuple/list issue; end condition)
# NOTE: Accepted on first Submit
# NOTE: Runtime 4 ms Beats 8.61%
# NOTE: Memory 17.76 MB Beats 56.80%
