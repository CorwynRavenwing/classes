class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        REV = lambda x: tuple(reversed(tuple(x)))

        print(f'forward:')
        array = []
        depth = 0
        for C in s:
            print(f'  {C=}')
            match C:
                case '(':
                    depth += 1
                    array.append(C)
                case ')':
                    if depth >= 1:
                        depth -= 1
                        array.append(C)
                    # else drop it on the floor
                case _:
                    array.append(C)

        s = REV(array)
        print(f'backward:')
        array = []
        depth = 0
        for C in s:
            print(f'  {C=}')
            match C:
                case ')':
                    depth += 1
                    array.append(C)
                case '(':
                    if depth >= 1:
                        depth -= 1
                        array.append(C)
                    # else drop it on the floor
                case _:
                    array.append(C)
        
        s = REV(array)
        return ''.join(s)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 285 ms Beats 10.93%
# NOTE: Memory 20.72 MB Beats 5.28%
# NOTE: could probably be faster if we did a single pass,
#       recording the index of each '('.  If we encounter
#       a ')', we delete the last such index; if the list
#       is currently empty, we add the ')' index to a second
#       list of indexes.  When done, we return the entire string
#       except the indexes that are still in either list.
