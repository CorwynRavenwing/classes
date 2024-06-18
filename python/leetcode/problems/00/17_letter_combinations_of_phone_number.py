class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        phone = {
            2: 'abc', 3: 'def',
            4: 'ghi', 5: 'jkl', 6: 'mno',
            7: 'pqrs', 8: 'tuv', 9: 'wxyz',
        }
        
        answers = ['']
        print(f'{answers=}')
        for D in map(int, digits):
            answers = list([
                A + L
                for A in answers
                for L in phone[D]
            ])
            print(f'{D=} {answers=}')
        if answers == [""]:
            answers = []
        return answers

