class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:

        tape = [
            {
                'chars': "",
                'prev': 0,
                'size': 0,
                'total': 0,
                'repeat': 1,
            }
        ]
        
        L = len(tape)
        tip = tape[-1]
        for C in s:
            print(f'  {L=} {tip=}')
            if C.isdigit():
                count = int(C)
                print(f'"{C}": repeat {count}')
                tip['repeat'] *= count
            else:
                # non-digit
                if tip['repeat'] > 1:
                    print(f'--- add loop ---')
                    tapeLen = tip['total'] * tip['repeat']
                    tape.append(
                        {
                            'chars': "",
                            'prev': tapeLen,
                            'size': 0,
                            'total': tapeLen,
                            'repeat': 1,
                        }
                    )
                    L = len(tape)
                    tip = tape[-1]
                    print(f'  {L=} {tip=}')
                print(f'"{C}": write')
                tip['chars'] += C
                tip['size'] += 1
                tip['total'] += 1
            tapeLen = tip['total'] * tip['repeat']
            if tapeLen >= k:
                print(f'Enough tape decoded: {tapeLen} >= {k}')
                break
        print(f'  {L=} {tip=}')
        if tip['repeat'] == 1 and tip['total'] == k:
            return C

        k -= 1  # zero-index instead

        while L:
            print(f'if you seek {k=}')
            if k > tip['total']:
                k %= tip['total']
                print(f'  %= {tip["total"]} -> {k=}')
            else:
                print(f'  no %= because {k} <= {tip["total"]}')
            
            if k >= tip['prev']:
                print(f'{k} >= {tip["prev"]}: answer is on this level')
                k -= tip['prev']
                print(f'  seek {k=} on tip section')
                assert k < tip['size']
                return tip['chars'][k]
            else:
                print(f'{k} < {tip["prev"]}: answer is on a lower level')
                trash = tape.pop(-1)
                L = len(tape)
                tip = tape[-1]

        return "FAIL"

