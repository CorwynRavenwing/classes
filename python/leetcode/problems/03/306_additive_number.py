class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        def translate(string: str) -> int:
            if len(string) == 0:
                return None
            if string[0] == '0' and len(string) > 1:
                return None
            return int(string)

        for i in range(1, len(num)):
            numbers = 1
            print(f'{i=}')
            Afrag = num[:i]
            if len(Afrag) != i:
                # print(f'    too short')
                break
            if num[0] == '0' and i > 1:
                # print(f'    leading zero')
                break
            A = translate(Afrag)
            origA = A
            print(f'  {Afrag=} {A=} {numbers=}')
            for j in range(1, len(num)):
                A = origA
                numbers = 2
                print(f'{i=} {j=}')

                Bfrag = num[i:i+j]
                if len(Bfrag) != j:
                    # print(f'      too short')
                    break
                if num[i] == '0' and j > 1:
                    # print(f'    leading zero')
                    break
                B = translate(Bfrag)
                print(f'    {Bfrag=} {B=} {numbers=}')

                ptr = i + j
                while True:
                    C = A + B
                    Cstr = str(C)
                    Clen = len(Cstr)
                    Cfrag = num[ptr:ptr+Clen]
                    if len(Cfrag) == 0:
                        if numbers < 3:
                            print(f'    not enough {numbers=}')
                            break
                        else:
                            return True
                    if len(Cfrag) != Clen:
                        print(f'      too short: {Clen}:{len(Cfrag)}')
                        break
                    if num[ptr] == '0' and Clen > 1:
                        print(f'    leading zero')
                        break
                    if Cfrag != Cstr:
                        print(f'    {Cfrag=} {Cstr=} {C=} ({A}+{B})')
                        print(f'      wrong answer {Cfrag}:{Cstr}')
                        break
                    numbers += 1
                    print(f'    {Cfrag=} {Cstr=} {C=} {numbers=}')
                    (A, B) = (B, C)
                    ptr += Clen

