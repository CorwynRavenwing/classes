class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        def show(s: str) -> str:
            t = f'{s[:10]}...{s[-10:]}({len(s)})'
            return (
                t
                if len(t) < len(s)
                else s
            )
        
        def filter_away_EQ(group: List[str], target: str) -> List[str]:
            if target not in group:
                return group
            return [
                G
                for G in group
                if G != target
            ]

        def filter_away_GT(group: List[str], target: str) -> List[str]:
            return [
                G
                for G in group
                if G <= target
            ]
        
        answer = ""
        work = s
        while work:
            print(f'"{answer}" <- "{show(work)}"')
            letters = sorted(list(set(work)))
            for L in letters:
                index = work.index(L)
                print(f'  "{L}": [{index}]')
                left = work[:index]
                center = work[index]
                right = work[index+1:]
                assert center == L
                print(f'    "{show(left)}" "{center}" "{show(right)}"')
                missing = set(left) - set(right)
                if missing:
                    missingStr = "".join(sorted(list(missing)))
                    print(f'      missing="{missingStr}"')
                    continue
                else:
                    answer += L
                    workList = filter_away_EQ(right, L)
                    work = ''.join(workList)
                    # print(f'      -> "{show(work)}"')
                    break

        return answer

# NOTE: Runtime 21 ms Beats 5.18%
# NOTE: Memory 17.14 MB Beats 12.46%
