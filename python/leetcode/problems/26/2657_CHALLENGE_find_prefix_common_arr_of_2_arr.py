class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        aSet = set()
        bSet = set()
        answer = []
        for aVal, bVal in zip(A,B):
            aSet.add(aVal)
            bSet.add(bVal)
            commonSet = aSet & bSet
            print(f'A:{aSet}\nB:{bSet}\nC:{commonSet}\n')
            answer.append(len(commonSet))
        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 143 ms Beats 5.21%
# NOTE: Memory 17.91 MB Beats 9.90%
