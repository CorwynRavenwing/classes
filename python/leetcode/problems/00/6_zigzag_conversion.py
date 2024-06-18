class Solution:
    def convert(self, s: str, numRows: int) -> str:

        buckets = list([
            []
            for _ in range(numRows)
        ])
        print(f'{buckets=}')

        index = 0
        direction = 1
        dir_show = {
            1: 'D',
            -1: 'U',
        }
        for char in s:
            # print(f'{index} {dir_show[direction]} "{char}"')
            buckets[index].append(char)
            index += direction
            if index <= 0:
                direction = 1
            elif index >= numRows - 1:
                direction = -1
            if index < 0 or index > numRows - 1:
                # print(f'  (correction)')
                index += direction
        # print(f'{buckets=}')
        bucket_values = [
            ''.join(B)
            for B in buckets
        ]
        print(' '.join(bucket_values))
        answer = ''.join(bucket_values)
        return answer

