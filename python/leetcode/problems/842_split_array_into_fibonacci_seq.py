class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:

        MAXINT = 2 ** 31
        MAXLEN = len(str(MAXINT))
        print(f'{MAXINT=} {MAXLEN=}')

        states = [
            ([], num)
        ]
        while len(states):
            S = states.pop(0)
            print(f'{S=}')
            (arr, string) = S
            if string == "":
                if len(arr) > 2:
                    print(f'  FOUND {arr}')
                    return arr
                else:
                    print(f'  out of characters')
                    continue
            if len(arr) < 2:
                print(f'{len(arr)} < 2, anything')
                # grab any number of digits up to MAXLEN
                max_number_len = min(MAXLEN, len(string))
                print(f'  i in range({1},{max_number_len+1})')
                for i in range(1, max_number_len + 1):
                    fragment = string[:i]
                    remain = string[i:]
                    # print(f'  try {fragment},{remain}')
                    if fragment[0] == "0" and fragment != "0":
                        print(f'    {fragment}: no leading zeros')
                        break
                    states.append(
                        (arr + [int(fragment)], remain)
                    )
            else:
                print(f'{len(arr)} >= 2, ABC')
                (A, B) = arr[-2:]
                C = A + B
                expected = str(C)
                L = len(expected)
                fragment = string[:L]
                remain = string[L:]
                print(f'  ({A}+{B})={C}/{fragment}')
                if expected == fragment:
                    if C > MAXINT:
                        print(f'    C > MAXINT')
                        continue
                    states.insert(
                        0,
                        (arr + [C], remain)
                    )
                else:
                    print(f'    nope')
        return []

