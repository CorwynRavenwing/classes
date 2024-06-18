class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        commands = list(zip(indices, sources, targets))
        # print(f'{commands=}')
        for i, C in enumerate(commands):
            (index, source, target) = C
            length = len(source)
            frag = s[index:index+length]
            # print(f'{i}: [{index}+{length}] "{frag}/{source}"')
            if frag != source:
                # print(f'  MISMATCH!')
                commands[i] = None
        # print(f'{commands=}')
        while None in commands:
            commands.remove(None)
        commands.sort(reverse=True)     # start at highest index
        # print(f'{commands=}')
        print(f'{s=}')
        for i, C in enumerate(commands):
            (index, source, target) = C
            length = len(source)
            frag = s[index:index+length]
            print(f'{i}: [{index}+{length}] "{frag}/{source}"')
            if frag != source:
                print(f'  MISMATCH!')
                return "mismatch -- should be impossible"
            before = s[:index]
            after = s[index+length:]
            print(f'"{before}" "{frag}"->"{target}" "{after}"')
            s = before + target + after
            print(f'{s=}')
        
        return s

