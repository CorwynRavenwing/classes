class Solution:
    def validUtf8(self, data: List[int]) -> bool:

        binary = list(map(
            lambda N: format(N, '08b'),
            data
        ))
        # print(f'{binary=}')
        while binary:
            mainbyte = binary.pop(0)
            morebytes = 0
            if mainbyte.startswith('0'):
                print(f'1: {mainbyte} OK')
                continue
            elif mainbyte.startswith('110'):
                morebytes = 1
            elif mainbyte.startswith('1110'):
                morebytes = 2
            elif mainbyte.startswith('11110'):
                morebytes = 3
            else:
                print(f'X: {mainbyte} INVALID')
                return False
            octets = []
            for i in range(morebytes):
                if not binary:
                    print(f'{morebytes+1}: {mainbyte} {octets} TRUNCATED')
                    return False
                nextbyte = binary.pop(0)
                if not nextbyte.startswith('10'):
                    print(f'{morebytes+1}: {mainbyte} {octets} {nextbyte} BAD OCTET')
                    return False
                octets.append(nextbyte)
            print(f'{morebytes+1}: {mainbyte} {octets} OK')
        
        return True

