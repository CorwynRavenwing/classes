class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def backspaceExecute(s: str) -> str:
            result = []
            print(f"{s}")
            for ch in s:
                if ch == '#':
                    if result:
                        ignore = result.pop()
                        print(f"  -'{ignore}'")
                else:
                    result.append(ch)
                    print(f"  +'{ch}'")
            return ''.join(result)

        bS = backspaceExecute(s)
        bT = backspaceExecute(t)
        print(f"{bS=}")
        print(f"{bT=}")
        return (bS == bT)

