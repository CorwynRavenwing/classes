class Solution:
    def countSegments(self, s: str) -> int:
        # while '  ' in s:
        #     # print(f"{s=}")
        #     s = s.replace('  ', ' ')
        
        # if s in ['', ' ']:
        #     return 0
        
        segments = s.split(' ')
        segments = [
            seg
            for seg in segments
            if seg != ''
        ]
        return len(segments)
        
