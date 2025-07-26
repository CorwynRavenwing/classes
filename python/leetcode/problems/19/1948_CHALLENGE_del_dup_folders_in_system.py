class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        
        paths = tuple(map(tuple, paths))
        contents = {}
        for path in paths:
            # print(f'{path=}')
            for i in range(1, len(path)):
                front = path[:i]
                back = path[i:]
                # print(f'  {front=} {back=}')
                contents.setdefault(front, [])
                contents[front].append(back)
        # print(f'{contents=}')

        contents = {
            parent: tuple(sorted(children))
            for parent, children in contents.items()
        }
        # print(f'{contents=}')

        parents_by_contents = {}
        for parent, children in contents.items():
            parents_by_contents.setdefault(children, [])
            parents_by_contents[children].append(parent)
        # print(f'{parents_by_contents=}')

        duplicates = {
            item
            for contents, parents in parents_by_contents.items()
            for item in parents
            if len(parents) > 1
        }
        print(f'{duplicates=}')

        answer = set(paths)
        for path in paths:
            # print(f'{path=}')
            if path in duplicates:
                # print(f'  DELETE')
                answer.remove(path)
                continue
            for i in range(1, len(path)):
                front = path[:i]
                back = path[i:]
                # print(f'  {front=} {back=}')
                if front in duplicates:
                    # print(f'    DELETE')
                    answer.remove(path)
                    break
                    # break i == continue path

        return tuple(answer)

# NOTE: Acceptance Rate 55.5% (HARD)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 3697 ms Beats 5.56%
# NOTE: Memory 292.60 MB Beats 5.56%
