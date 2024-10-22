class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        print(f'{len(fruits)=}')
        fruitGroups = [
            (F, 1)
            for F in fruits
        ]
        # print(f'DEBUG: {fruitGroups=}')
        for i in range(1, len(fruitGroups)):
            # print(f'DEBUG: {i=} FG={fruitGroups[i]}')
            (A, count) = fruitGroups[i]
            (B, prior) = fruitGroups[i - 1]
            if A == B:
                fruitGroups[i] = (A, count + prior)
                fruitGroups[i - 1] = None
        fruitGroups = [
            FG
            for FG in fruitGroups
            if FG is not None
        ]
        print(f'{len(fruitGroups)=}')
        # print(f'DEBUG: {fruitGroups[:10]=}')

        answer = 0
        i = 0
        while i < len(fruitGroups):
            (F, treeSize) = fruitGroups[i]
            count = treeSize
            answer = max(answer, count)
            allow = set([F])
            # print(f'[{i=}]{F=} {count=} {allow=}')
            j = i + 1
            k = j
            while j < len(fruitGroups):
                prior = F
                (F, treeSize) = fruitGroups[j]
                count += treeSize
                # print(f'[{j=}]{F=} {count=} {allow=}')
                if F != prior:
                    if F not in allow:
                        if len(allow) < 2:
                            allow.add(F)
                        else:
                            # print(f'    STOP')
                            break
                    k = j
                answer = max(answer, count)
                j += 1
            print(f'->{k=}')
            i = k

        return answer

# NOTE: Runtime 223 ms Beats 98.09%
# NOTE: Memory 27.35 MB Beats 5.63%
