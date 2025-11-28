class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        
        length = 1
        remainder = 1
        remainder %= k
        remainders_seen = set()

        while remainder:
            print(f'{length=} {remainder=}')
            length += 1
            remainder *= 10
            remainder += 1
            remainder %= k
            if remainder in remainders_seen:
                print(f'  SEEN')
                break
            else:
                remainders_seen.add(remainder)
        
        if remainder:
            return -1
        else:
            return length

# NOTE: Acceptance Rate 48.3% (medium)

# NOTE: re-created for challenge after computer crash
# NOTE: Accepted on second Run (edge case K==1)
# NOTE: Accepted on first Submit
# NOTE: Runtime 51 ms Beats 27.16%
# NOTE: Memory 21.90 MB Beats 5.01%
