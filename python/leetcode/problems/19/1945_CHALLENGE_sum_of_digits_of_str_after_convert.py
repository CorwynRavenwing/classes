class Solution:
    def getLucky(self, s: str, k: int) -> int:

        Alphabet = 'abcdefghijklmnopqrstuvwxyz'
        numbers = [
            Alphabet.index(C) + 1
            for C in s
        ]
        print(f'{numbers}')
        value = ''.join(map(str, numbers))
        print(f'0/{k}: {value=}')
        for _ in range(k):
            value = str(
                sum(
                    map(
                        int,
                        tuple(value)
                    )
                )
            )
            print(f'{_+1}/{k}: {value=}')
        
        return int(value)

# NOTE: Accepted on first Submit
# NOTE: Runtime 41 ms Beats 35.09%
# NOTE: Memory 16.56 MB Beats 37.00%
