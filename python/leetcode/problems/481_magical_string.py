class Solution:
    def magicalString(self, n: int) -> int:

        def generateMagicString() -> List[str]:

            string = ['1', '2', '2']
            pointer = 2

            for S in string:
                yield S
            
            while True:
                P = string[pointer]
                print(f'  got "{P}": return {P} ones')
                for i in range(int(P)):
                    yield '1'
                    string.append('1')
                pointer += 1

                P = string[pointer]
                print(f'  got "{P}": return {P} twos')
                for i in range(int(P)):
                    yield '2'
                    string.append('2')
                pointer += 1
        
        magic = generateMagicString()

        ones = 0
        for _ in range(n):
            D = next(magic)
            if D == '1':
                ones += 1
            print(f'{_+1}/{n}: {D} ({ones})')
        
        return ones

