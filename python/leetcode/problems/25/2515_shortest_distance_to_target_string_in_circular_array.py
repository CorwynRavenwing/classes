class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:

        targetIndexes = []
        endIndex = -1
        while True:
            try:
                endIndex = words.index(target, endIndex + 1)
                targetIndexes.append(endIndex)
            except ValueError:
                break
        print(f"{targetIndexes=}")
        if not targetIndexes:
            return -1
        
        N = len(words)
        answers = []
        print(f"{words=}")
        for endIndex in targetIndexes:
            print(f"{target=} {startIndex=} {endIndex=} {N=}")
            F = (endIndex - startIndex) % N
            B = (startIndex - endIndex) % N
            print(f"{F=} {B=}")
            answers.append(min(F,B))
        print(f"{answers=}")
        return min(answers)

