class Solution:
    def getMaxLen(self, nums: List[int]) -> int:

        def join(strList: List[str]) -> str:
            return ''.join(strList)

        def makeSigns(nums: List[int]) -> str:
            return join([
                (
                    '+' if N > 0 else
                    '-' if N < 0 else
                    '0' if N == 0 else
                    '?'
                )
                for N in nums
            ])

        def revStr(s: str) -> str:
            return join(reversed(s))

        def hasEvenNegatives(s: str) -> bool:
            if '-' not in s:
                # zero negatives, is an even number
                return True
            C = Counter(s)
            return (C['-'] % 2 == 0)
        
        def replaceFirstNeg(s: str) -> str:
            return s.replace('-', '!', 1)

        def replaceLastNeg(s: str) -> str:
            return revStr(
                replaceFirstNeg(
                    revStr(s)
                )
            )

        def cleanUpSignGroups(signGroups: List[str]) -> List[str]:
            cleanup_1 = []
            for group in signGroups:
                if hasEvenNegatives(group):
                    cleanup_1.append(group)
                else:
                    cleanup_1.append(replaceFirstNeg(group))
                    cleanup_1.append(replaceLastNeg(group))
            # print(f'{cleanup_1=}')
            cleanup_2 = []
            for group in cleanup_1:
                if hasEvenNegatives(group):
                    cleanup_2.append(group.replace('-', '+'))
                else:
                    raise Exception('Error: {group} has odd negatives!')
            # print(f'{cleanup_2=}')
            cleanup_3 = [
                newGroup
                for group in cleanup_2
                for newGroup in group.split('!')
            ]
            return cleanup_3

        def getAnswers(signGroups: List[str]) -> List[int]:
            return [
                len(group)
                for group in signGroups
            ]
        
        allSigns = makeSigns(nums)
        # print(f'{allSigns=}')

        signGroups = allSigns.split('0')
        while '' in signGroups:
            signGroups.remove('')
        # print(f'{signGroups=}')

        signGroups = cleanUpSignGroups(signGroups)
        # print(f'{signGroups=}')

        answers = getAnswers(signGroups)
        print(f'{answers=}')

        return max(answers, default=0)

