class Solution:
    def numSteps(self, s: str) -> int:

        binary = list(map(int, list(s)))
        steps = 0
        print(f'{steps=} {binary=}')
        while binary != [1]:
            if binary[-1] == 0:
                print(f'even')
                del binary[-1]
            else:
                print(f'odd')
                binary[-1] += 1
                # shake number to be binary again
                while max(binary) >= 2:
                    if binary[0] >= 2:
                        binary.insert(0, 0)
                    index = binary.index(max(binary))
                    carry = binary[index] // 2
                    binary[index - 1] += carry
                    binary[index] -= carry * 2
            steps += 1
            print(f'{steps=} {binary=}')

        return steps

