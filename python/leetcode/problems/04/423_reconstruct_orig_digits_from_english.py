class Solution:
    def originalDigits(self, s: str) -> str:
        spellDigits = {
            '0': 'zero',
            '1': 'one',
            '2': 'two',
            '3': 'three',
            '4': 'four',
            '5': 'five',
            '6': 'six',
            '7': 'seven',
            '8': 'eight',
            '9': 'nine',
        }
        digitCounts = {}
        letterUses = {}
        for digit, letters in spellDigits.items():
            digitCounts[digit] = Counter(letters)
            for letter in letters:
                letterUses.setdefault(letter, set())
                letterUses[letter].add(digit)
        # print(f'{digitCounts=}')
        # print(f'{letterUses=}')
        letterUseRules = []
        while letterUses:
            # print(f'=' * 60)
            # print(f'{letterUses=}')
            rules = {
                letter: numbers.pop()
                for letter, numbers in letterUses.items()
                if len(numbers) == 1
            }
            # print(f'{rules=}')
            numbersWithRules = set(rules.values())
            print(f'{numbersWithRules=}')
            letterUseRules.append(rules)
            # filter 1: don't point to any numbers found in this rule
            letterUses = {
                letter: (numbers - numbersWithRules)
                for letter, numbers in letterUses.items()
            }
            # filter 2: don't keep any letters pointing to nothing
            letterUses = {
                letter: numbers
                for letter, numbers in letterUses.items()
                if len(numbers) > 0
            }
        print(f'=' * 60)
        # print(f'{letterUseRules=}')

        counts = Counter(s)
        answer = []
        for Rule in letterUseRules:
            print(f'{answer=} {counts=}')
            print(f'  {Rule=}')
            for letter, number in Rule.items():
                print(f'    rule {letter} -> {number}')
                letterCount = counts[letter]
                if letterCount:
                    # print(f'      {letterCount=}')
                    answer.extend(
                        [number] * letterCount
                    )
                    # subtract = digitCounts[number] * letterCount
                    # print(f'      counts -= {subtract}')
                    # counts -= subtract
                    print(f'      counts -= {digitCounts[number]} * {letterCount}')
                    for _ in range(letterCount):
                        counts -= digitCounts[number]
                    print(f'  DEBUG: new {counts=}')

        return ''.join(sorted(answer))

# NOTE: Accepted on first Submit
# NOTE: Runtime 150 ms Beats 5.20%
# NOTE: Memory 17.33 MB Beats 7.07%
