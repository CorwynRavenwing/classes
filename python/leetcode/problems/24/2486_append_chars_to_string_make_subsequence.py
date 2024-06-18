class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j = 0
        jVal = None
        for i, iVal in enumerate(s):
            if j >= len(t):
                # matched all of T
                break
            jVal = t[j]
            print(f'{i}:{iVal} {j}:{jVal}')
            if iVal == jVal:
                j += 1
        fragment = t[j:]
        print(f'{fragment=}')
        return len(fragment)

