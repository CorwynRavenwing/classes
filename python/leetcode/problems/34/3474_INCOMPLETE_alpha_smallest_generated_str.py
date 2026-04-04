class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        
        N = len(str1)
        M = len(str2)
        string = "X" * (N + M - 1)
        rules = tuple(enumerate(str1))
        rules_yes = [
            rule
            for (rule, value) in rules
            if value == 'T'
        ]
        rules_no = [
            rule
            for (rule, value) in rules
            if value == 'F'
        ]
        # print(f'{rules_yes=}')
        # print(f'{rules_no =}')

        def split_string(rule: int, string: str) -> Tuple[str,str,str]:
            left = string[:rule]
            center = string[rule:rule + M]
            right = string[rule + M:]
            # print(f'{string=} {rule=} {M=}')
            # print(f'  {left=} {center=} {right=}')
            return (left, center, right)

        def relevant_rule(rule: int) -> bool:
            (left, center, right) = split_string(rule, string)
            diffs = [
                a + b
                for (a, b) in zip(center, str2)
                if a not in [b, 'X']
            ]
            if diffs:
                # print(f'  irrelevant: {diffs=}')
                return False
            elif 'X' not in center:
                # print(f'  no X: {center=}')
                return False
            else:
                return True

        for rule in rules_yes:
            (left, center, right) = split_string(rule, string)
            if len(center) != M:
                raise Exception(f'{len(center)=} != {M=}')
            diffs = [
                a + b
                for (a, b) in zip(center, str2)
                if a not in [b, 'X']
            ]
            if diffs:
                # print(f'  FAIL YES: {diffs=}')
                return ""
            string = left + str2 + right
            # print(f'YES[{rule}]: {string=}')
        
        def rules_no_has_conflict(string: str) -> bool:
            for rule in rules_no:
                (left, center, right) = split_string(rule, string)
                if len(center) != M:
                    raise Exception(f'{len(center)=} != {M=}')
                diffs = [
                    a + b
                    for (a, b) in zip(center, str2)
                    if a not in [b]
                ]
                if not diffs:
                    # print(f'  FAIL NO: {center=} {str2=} {diffs=}')
                    return True
                # print(f'NO[{rule}]: {string=}')
            return False
        
        if rules_no_has_conflict(string):
            return ""

        rules_no = [
            rule
            for rule in rules_no
            if relevant_rule(rule)
        ]
        # print(f'relevant {rules_no =}')

        if not rules_no:
            string = string.replace('X', 'a')
            # print(f'[X]: {string=}')
        
        queue = [string]    # they stay in alpha order
        while queue:
            string = queue.pop(0)
            # print(f'  {string=}')
            if 'X' not in string:
                return string
            for AB in ['a', 'b']:
                newString = string.replace('X', AB, 1)
                # print(f'    [{AB}]: {newString}')
                if rules_no_has_conflict(newString):
                    # print(f'      ERR')
                    continue
                else:
                    bisect.insort(queue, newString)

        return string

# NOTE: Acceptance Rate 34.7% (HARD)

# NOTE: incomplete: Time Limit Exceeded for large inputs
