class Solution:
    def lengthLongestPath(self, input: str) -> int:

        # print(f'{input=}')
        stack = []
        answer = 0
        lines = input.split('\n')
        for line in lines:
            # print(f'{stack=}')
            # print(f'{line=}')
            depth = 0
            while line[0] == '\t':
                depth += 1
                line = line[1:]
            is_file = ('.' in line)
            print(f'{"  " * depth}{"FILE" if is_file else "DIR:"} {line}')
            if is_file:
                fullpath = stack[:depth] + [line]
                filename = '/'.join(fullpath)
                print(f'*** {len(filename)} "{filename}"')
                answer = max(answer, len(filename))
            else:
                # is directory
                stack = stack[:depth]
                stack.append(line)
        return answer

