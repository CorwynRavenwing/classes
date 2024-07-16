class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:

        len1 = len(word1)
        len2 = len(word2)
        (p1, p2) = (0, 0)
        answer = []
        while p1 < len1 and p2 < len2:
            Rest1 = word1[p1:]
            Rest2 = word2[p2:]
            L1 = Rest1[0]
            L2 = Rest2[0]
            print(f'{p1}:{L1} {p2}:{L2}')
            if Rest1 > Rest2:
                answer.append(L1)
                p1 += 1
                print(f'  A: {L1=}')
            elif Rest1 < Rest2:
                answer.append(L2)
                p2 += 1
                print(f'  A: {L2=}')
            elif Rest1 == Rest2:
                if (len1 - p1) > (len2 - p2):
                    answer.append(L1)
                    p1 += 1
                    print(f'  B: {L1=}')
                else:
                    # (len1 - p1) <= (len2 - p2)
                    answer.append(L2)
                    p2 += 1
                    print(f'  B: {L2=}')
        while p1 < len1:
            L1 = word1[p1]
            answer.append(L1)
            p1 += 1
            print(f'C: {L1=}')
        while p2 < len2:
            L2 = word2[p2]
            answer.append(L2)
            p2 += 1
            print(f'C: {L2=}')
        return ''.join(answer)

