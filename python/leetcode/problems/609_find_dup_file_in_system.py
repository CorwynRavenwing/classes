class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:

        path_by_content = {}
        for path in paths:
            split_path = path.split()
            file_path = split_path.pop(0)
            print(f'{file_path=}')
            for data in split_path:
                # print(f'  {data}')
                file_name, contentsPlus = data.split('(')
                contents = contentsPlus[:-1]
                print(f'  {file_name}: "{contents}"')
                path_by_content.setdefault(contents, [])
                path_by_content[contents].append(f'{file_path}/{file_name}')
        print(f'{path_by_content=}')
        answer = [
            full_paths
            for (content, full_paths) in path_by_content.items()
            if len(full_paths) > 1
        ]
        return answer

