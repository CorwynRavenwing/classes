class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:

        digits = list(map(int, list(str(n))))
        print(f'{digits}')
        mono = digits.copy()
        i = 0
        while i + 1 < len(digits):
            print(f'{mono}')
            i += 1
            if mono[i - 1] > mono[i]:
                print(f'[{i}] update {mono[i]} -> {9}')
                mono[i] = 9
                if mono > digits:
                    print(f'too high, [{i-1}] update {mono[i-1]} -> {mono[i-1] - 1}')
                    mono[i - 1] -= 1
                    i = 0
                    continue
        print(f'=' * 70)
        print(f'{digits}')
        print(f'{mono}')
        answer_str = ''.join(map(str, mono))
        return int(answer_str)

