class Solution:
    def simplifyPath(self, path: str) -> str:

        dirs = path.split('/')
        print(f'A {dirs=}')
        while '' in dirs:
            index = dirs.index('')
            del dirs[index]
            print(f'B {dirs=}')
        while '.' in dirs:
            index = dirs.index('.')
            del dirs[index]
            print(f'C {dirs=}')
        while '..' in dirs:
            index = dirs.index('..')
            del dirs[index]
            if index:
                del dirs[index - 1]
            print(f'D {dirs=}')
        return '/' + '/'.join(dirs)

