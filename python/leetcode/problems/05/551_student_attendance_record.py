from collections import Counter

class Solution:
    def checkRecord(self, s: str) -> bool:
        counts = Counter(s)
        print(f"{s}")
        if counts['A'] >= 2:
            print(f"  Fail: {counts['A']} >= 2")
            return False
        
        if 'LLL' in s:
            print(f"  Fail: three consecutive Late")
            return False

        return True

