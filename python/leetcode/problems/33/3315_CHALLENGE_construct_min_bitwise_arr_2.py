class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        
        # we borrow some code from #3314:

        @cache
        def magic(i: int) -> int:
            iPlus1 = i + 1
            Or = i | iPlus1     # "|": bitwise or operator
            # print(f'{i}|{iPlus1} = {Or}')
            return Or
        
        def find_magic(N: int) -> int:
            print(f'quick({N}):')

            REV = lambda L: tuple(reversed(L))

            binary_str = f'0{N:b}'      # add a leading zero: doesn't change value
            print(f'  {binary_str=}')
            binary_arr = tuple(binary_str)
            print(f'  {binary_arr=}')
            binary_rev = REV(binary_arr)
            print(f'  {binary_rev=}')
            zero_index = binary_rev.index('0')
            print(f'  {zero_index=}')
            if zero_index == 0:
                print(f'  even numbers are impossible!')
                return -1
            last_one_index = zero_index - 1
            answer_rev = list(binary_rev)
            assert answer_rev[last_one_index] == '1'
            answer_rev[last_one_index] = '0'
            print(f'  {answer_rev=}')
            answer_arr = REV(answer_rev)
            print(f'  {answer_arr=}')
            answer_str = ''.join(answer_arr)
            print(f'  {answer_str=}')
            answer = int(answer_str, 2)
            print(f'  {answer=}')
            M = magic(answer)
            print(f'  magic={M}')
            assert M == N
            return answer
            
        answer = [
            find_magic(N)
            for N in nums
        ]
        
        return answer

# NOTE: Acceptance Rate 42.3% (medium)

# NOTE: re-used some code, but old version gave Memory Exceeded for large inputs
# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Memory Exceeded)
# NOTE: Runtime 125 ms Beats 5.23%
# NOTE: Memory 19.56 MB Beats 8.36%
