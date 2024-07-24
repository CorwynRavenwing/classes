class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        def mappedValue(num: int) -> int:
            numStr = str(num)
            answerStr = ''.join([
                str(mapping[int(D)])
                for D in numStr
            ])
            answer = int(answerStr)
            print(f'MV({num}) -> "{answerStr}" {answer}')
            return answer
        
        sortable = [
            (mappedValue(N), i, N)
            for i, N in enumerate(nums)
        ]
        sortable.sort()
        answers = [
            N
            for (mv, i, N) in sortable
        ]
        return answers

