class Solution:
    def removeDigit(self, number: str, digit: str) -> str:

        answers = []
        for i, D in enumerate(number):
            if D != digit:
                continue
            print(f"{i=} {D=}")
            answer = number[:i] + number[i+1:]
            print(f"  {answer=}")
            answers.append(answer)
        
        answers.sort(
            key=lambda x: int(x)
        )

        return answers[-1]

