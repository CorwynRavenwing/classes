class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        
        print(f'{len(s)=}')
        possible = {0}
        wildcard_s = [
            (
                char
                if isLocked == '1'
                else '*'
            )
            for (char, isLocked) in zip(s, locked)
        ]
        wildcard_s = ''.join(wildcard_s)
        print(f'{wildcard_s=}')
        counts = Counter(wildcard_s)
        print(f'{counts=}')
        openParens = counts['(']
        closeParens = counts[')']
        wildCards = counts['*']
        if abs(openParens - closeParens) > wildCards:
            print(f'Not enough wildcards to make up imbalance in parens')
            print(f'  |{openParens} - {closeParens}| > {wildCards}')
            return False
        allChars = len(wildcard_s)
        expectedOpenAndClose = allChars // 2
        print(f'{allChars=} {expectedOpenAndClose=}')
        addOpenParens = expectedOpenAndClose - openParens
        if addOpenParens > 0:
            print(f'TRY replacing the first {addOpenParens} wildcards with open parenthesis:')
            wildcard_s = wildcard_s.replace('*', '(', addOpenParens)
            print(f'{wildcard_s=}')
        addCloseParens = expectedOpenAndClose - closeParens
        if addCloseParens > 0:
            print(f'TRY replacing the next {addCloseParens} wildcards with close parenthesis:')
            wildcard_s = wildcard_s.replace('*', ')', addCloseParens)
            print(f'{wildcard_s=}')
        print(f'redo counts:')
        counts = Counter(wildcard_s)
        print(f'{counts=}')
        openParens = counts['(']
        closeParens = counts[')']
        wildCards = counts['*']
        if openParens != closeParens:
            print(f'ERROR: parens do not balance: {openParens} != {closeParens}')
            return False
        if wildCards != 0:
            print(f'ERROR: did not use up all wildcards: {wildCards=}')
            return False
        
        mountains = list(itertools.accumulate([
            (
                1 if char == '(' else
                -1 if char == ')' else
                0 if char == '*' else
                None
            )
            for char in wildcard_s
        ]))
        print(f'{mountains=}')
        if min(mountains) < 0:
            print(f'ERROR: Parenthesis balance falls below zero!')
            return False
            
        for char in wildcard_s:
            # print(f'{possible=}')
            # print(f'{char=} {isLocked=}')
            newPossible = set()
            for P in possible:
                # print(f'  {P=}')
                if char in ['(', '*']:
                    # print(f'    Open new paren')
                    newPossible.add(P + 1)
                if char in [')', '*']:
                    if P > 0:
                        # print(f'    Close a paren')
                        newPossible.add(P - 1)
                    else:
                        # print(f'    No paren to close: skip')
                        continue
            possible = newPossible

        # print(f'{possible=}')
        if 0 in possible:
            # print(f'Yes, it is possible')
            return True
        else:
            # print(f'Nope, impossible')
            return False

