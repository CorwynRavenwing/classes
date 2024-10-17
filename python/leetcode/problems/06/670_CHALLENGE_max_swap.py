class Solution:
    def maximumSwap(self, num: int) -> int:

        digits = list(str(num))
        print(f'{digits=}')

        for i, D in enumerate(digits):
            frag = digits[i:]
            M = max(frag)
            if D == M:
                print(f'{D} == max({frag})')
                continue
            else:
                indexes = []
                start = i + 1
                while True:
                    try:
                        index = digits.index(M, start)
                    except ValueError:
                        break
                    print(f'found {M} at [{index}]')
                    indexes.append(index)
                    start = index + 1
                print(f'{indexes=}')
                index_of_max = indexes[-1]
                print(f'swap positions [{i}] and [{index_of_max}]')
                (digits[i], digits[index_of_max]) = (digits[index_of_max], digits[i])
                break
        
        return int(''.join(digits))

# NOTE: Runtime 40 ms Beats 17.59%
# NOTE: Memory 16.50 MB Beats 42.30%
