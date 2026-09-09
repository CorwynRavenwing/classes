class Solution:
    def countCommas(self, n: int) -> int:
        
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

# NOTE: Acceptance Rate 69.4% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 19.17 MB Beats 86.58%
