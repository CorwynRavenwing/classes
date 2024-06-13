class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:

        def splitByLetter(w: str) -> List[str]:
            groups = [
                (1, C)
                for C in w
            ]
            while True:
                if len(groups) == 1:
                    break
                for i in range(1, len(groups)):
                    this = groups[i]
                    prev = groups[i-1]
                    (count1, char1) = this
                    (count0, char0) = prev
                    if char1 == char0:
                        groups[i] = (count1 + count0, char1)
                        groups[i-1] = None
                if None not in groups:
                    break
                while None in groups:
                    groups.remove(None)
            blocks = [
                char * count
                for (count, char) in groups
            ]
            return blocks
        
        def canStretchTo(w: str, t: str) -> bool:
            print(f'CST({w},{t})')

            groupW = splitByLetter(w)
            groupT = splitByLetter(t)
            if len(groupW) != len(groupT):
                print(f'  different # of letter groups!')
                print(f'  {groupW=}')
                print(f'  {groupT=}')
                print(f'  {len(groupW)} != {len(groupT)}')
                return False
            pairs = tuple(zip(groupW, groupT))
            for (A, B) in pairs:
                print(f'  "{A}" -> "{B}"')
                if A == B:
                    print(f'    same: OK')
                    continue
                if A[0] != B[0]:
                    print(f'    different letters!')
                    return False
                if len(A) >= len(B):
                    print(f'    A too long')
                    return False
                # if len(A) + 1 == len(B):
                #     print(f'    length difference of 1')
                #     return False
                if len(B) < 3:
                    print(f'    new length ({len(B)}) < 3')
                    return False
                else:
                    print(f'    OK')
            print(f'  all pairs ok')
            return True
        
        answers = [
            1
            for w in words
            if canStretchTo(w, s)
        ]
        return sum(answers)

