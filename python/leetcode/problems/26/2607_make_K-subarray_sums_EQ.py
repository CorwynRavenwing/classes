class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        
        # Euclidian Algorithm for GCD, as described in Wikipedia
        def GCD(A: int, B: int) -> int:
            # print(f'GCD({A},{B})')
            if B == 0:
                return A
            else:
                return GCD(B, A % B)
        
        def median(arr: List[int]) -> float:
            arr = sorted(arr)
            L = len(arr)
            if L % 2 == 1:
                index = L // 2
                return arr[index]
            else:
                indexA = L // 2 - 1
                indexB = L // 2
                total = sum([
                    arr[indexA],
                    arr[indexB],
                ])
                return total / 2

        N = len(arr)
        gcd = GCD(N,k)
        print(f'{N=} {k=} GCD(N,k)={gcd}')

        # group_ids_their_way_per_Hint_2 = [
        #     (gcd % i) if i else '?Div0?'
        #     for i in range(len(arr))
        # ]
        # print(f'{group_ids_their_way_per_Hint_2=}')
        # The prior is completely incorrect.  Instead, we use:
        group_ids = [
            i % gcd
            for i in range(len(arr))
        ]
        print(f'{group_ids=}')
        groupIndexes = {}
        groupData = {}

        for index, GroupId in enumerate(group_ids):
            # groupIndexes.setdefault(GroupId, [])
            # groupIndexes[GroupId].append(index)
            groupData.setdefault(GroupId, [])
            groupData[GroupId].append(arr[index])
        # print(f'{groupIndexes=}')
        print(f'{groupData=}')
        answer = 0
        for GroupId, data in groupData.items():
            print(f'{GroupId}: {data}')
            target = median(data)
            difference = 0
            for D in data:
                difference += abs(D - target)
            print(f'  median={target} diff={difference}')
            answer += int(difference)

        return answer
# NOTE: Runtime 817 ms Beats 10.11%
# NOTE: Memory 32.30 MB Beats 15.73%
