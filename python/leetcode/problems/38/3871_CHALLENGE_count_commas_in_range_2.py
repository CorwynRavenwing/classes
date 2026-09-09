class Solution:
    def countCommas(self, n: int) -> int:
        
	# we borrow some code from #3870:
        answer = 0
        while n > 0:
            L = len(str(n))
            G = (L - 1) // 3
            print(f'{G=} {L=} {n=}')
            A = G * 3
            B = (10 ** A) - 1
            print(f'  {A=} {B=}')
            sub_answer = (n - B) * G
            answer += sub_answer
            n = B
            print(f'  {answer=} ({sub_answer})')

        return answer

# NOTE: Acceptance Rate 41.4% (medium)

# NOTE: re-used all code from prior version without changes
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 3 ms Beats 19.73%
# NOTE: Memory 19.42 MB Beats 13.61%
