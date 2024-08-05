class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        counts = Counter(arr)
        distinct = [
            word
            for word, count in counts.items()
            if count == 1
        ]
        # print(f'{distinct=}')
        i = 0
        for word in arr:
            if word in distinct:
                i += 1
                print(f'{word} distinct #{i}')
                if i == k:
                    return word
            # else:
            #     print(f'{word} multiple')
        print(f'not found')
        return ""
# NOTE: Runtime 89 ms Beats 32.31%
# NOTE: Memory 16.86 MB Beats 35.47%
