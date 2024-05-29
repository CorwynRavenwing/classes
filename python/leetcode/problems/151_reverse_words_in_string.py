class Solution:
    def reverseWords(self, s: str) -> str:

        s = s.strip()
        while '  ' in s:
            s = s.replace('  ', ' ')
        
        # print(f'{s=}')
        Words = s.split(' ')
        sdroW = reversed(Words)
        answer = ' '.join(sdroW)
        return answer

