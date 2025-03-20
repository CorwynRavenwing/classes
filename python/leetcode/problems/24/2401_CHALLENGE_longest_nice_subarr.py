class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:

        def IntToBits(N: int) -> List[int]:
            binary = f'{N:b}'
            bits = tuple(reversed(binary))
            used = [
                index
                for index, bit in enumerate(bits)
                if bit == '1'
            ]
            # print(f'{N=} {binary=} {bits=} {used=}')
            return tuple(used)
        
        def BitsToInt(used: List[int]) -> int:
            print(f'{used=}')
            bits = [
                (
                    '1' if bit in used else '0'
                )
                for bit in range(max(used, default=0) + 1)
            ]
            print(f'{bits=}')
            binary = ''.join(reversed(bits))
            print(f'{binary=}')
            N = int(binary,2)
            print(f'{N=}')
            return N
        
        longest = 1
        L = 0
        R = 0
        bits_count = Counter()
        while L <= R <= len(nums):
            bits_check = [
                bit
                for bit, count in bits_count.items()
                if count > 1
            ]
            if (bits_check == []) or (L == R):
                # print(f'[{L},{R}]: {bits_check} {bits_count} YES, expand right')
                longest = max(longest, R - L)
                try:
                    B = nums[R]
                except IndexError:
                    print(f'{R=} out of bounds')
                    break
                R += 1
                bits_B = IntToBits(B)
                bits_count += Counter(bits_B)
                # print(f'  {bits_B=}')
            else:
                # print(f'[{L},{R}]: {bits_check} {bits_count} NO, shrink left')
                A = nums[L]
                bits_A = IntToBits(A)
                # print(f'  {bits_A=}')
                bits_count -= Counter(bits_A)
                bits_count = +bits_count        # throw away zeros
                L += 1

        return longest

# NOTE: Runtime 9113 ms Beats 5.16%
# NOTE: Memory 31.38 MB Beats 85.11%
