class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        while name:
            print(f"N '{name}'")
            print(f"T '{typed}'")
            N0 = name[0]
            name = name[1:]
            N1 = name[0] if name else '#'
            if not typed:
                print("  {typed=}")
                return False
            T0 = typed[0]
            typed = typed[1:]
            T1 = typed[0] if typed else '#'
            print(f"  {N0}{N1} {T0}{T1}")
            if N0 != T0:
                print("    N0 != T0")
                return False
            if N0 != N1:
                if T1 == N0:
                    print("    LONG")
                while (typed) and (typed[0] == N0):
                    print("      -")
                    typed = typed[1:]
        if typed:
            print(f"    {typed=}")
            return False
        else:
            return True

