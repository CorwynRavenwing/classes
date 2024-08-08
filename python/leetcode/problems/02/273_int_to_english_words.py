class Solution:
    def numberToWords(self, num: int) -> str:

        numberWords = {
            0: 'Zero',
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen',
            20: 'Twenty',
            30: 'Thirty',
            40: 'Forty',
            50: 'Fifty',
            60: 'Sixty',
            70: 'Seventy',
            80: 'Eighty',
            90: 'Ninety',
            100: 'Hundred', # not used the same way
        }

        groupNames = [
            None,
            'Thousand',
            'Million',
            'Billion',
            'Trillion',
            'Quadrillion',
            'Quintillion',
            'Hexillion',
            'Heptillion',
            'Octillion',
            'Nonillion',
            'Decillion',
            'Hopefully we wont have numbers this high'
        ]

        def intToWords(num: int) -> str:
            if num in numberWords:
                return numberWords[num]
            
            tens = num // 10
            ones = num % 10
            tensMult = tens * 10
            answer = []
            answer.append(
                intToWords(tensMult)
            )
            answer.append(
                intToWords(ones)
            )
            return ' '.join(answer)

        def groupToWords(num: int) -> str:
            answer = []
            if num >= 100:
                hundreds = num // 100
                num = num % 100
                answer.append(
                    intToWords(hundreds)
                )
                answer.append(
                    intToWords(100)
                )
                if num:
                    answer.append(
                        intToWords(num)
                    )
            else:
                answer.append(
                    intToWords(num)
                )
            return ' '.join(answer)

        def intToGroupsOf3(num: int) -> List[int]:
            if not num:
                return [0]
            answer = []
            while num:
                answer.append(num % 1000)
                num //= 1000
                # if not num:
                #     break
            return answer

        groups = intToGroupsOf3(num)
        print(f'{groups=}')
        wordGroups = tuple(map(groupToWords, groups))
        print(f'{wordGroups=}')
        
        wordGroupsWithNames = [
            (
                ' '.join([group, name])
                # this makes the "ones" group not have a label like "Thousands"
                if name is not None
                else group
            )
            for group, name in zip(wordGroups, groupNames)
            if not (
                # this skips things like "Zero Thousand"
                (group == 'Zero') and (name is not None)
            )
        ]
        print(f'{wordGroupsWithNames=}')
        if 'Zero' in wordGroupsWithNames:
            # this allows the number 'Zero' itself
            if wordGroupsWithNames != ['Zero']:
                # this skips things like "One Thousand Zero"
                wordGroupsWithNames.remove('Zero')
                print(f'{wordGroupsWithNames=}')

        return ' '.join(
            reversed(
                wordGroupsWithNames
            )
        )
# NOTE: Runtime 35 ms Beats 68.95%
# NOTE: Memory 16.98 MB Beats 7.73%
