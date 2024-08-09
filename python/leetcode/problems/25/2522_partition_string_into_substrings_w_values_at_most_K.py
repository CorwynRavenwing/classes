class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        answer = 0
        inprog = ''
        for D in s:
            print(f'{D}: "{inprog}"')
            if int(inprog + D) > k:
                answer += 1
                print(f'  substring #{answer}="{inprog}"')
                inprog = ''
            inprog += D
            if int(D) > k:
                print(f'  No: "{D}" > {k}')
                return -1
        if inprog:
            answer += 1
            print(f'  (last) substring #{answer}="{inprog}"')
            inprog = ''
        
        return answer
# NOTE: Runtime 318 ms Beats 14.93%
# NOTE: Memory 17.56 MB Beats 23.38%
