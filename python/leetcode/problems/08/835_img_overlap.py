class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        
        def coords_of_ones(img: List[List[int]]) -> List[Tuple[int,int]]:
            return tuple([
                (X,Y)
                for X, row in enumerate(img)
                for Y, val in enumerate(row)
                if val == 1
            ])

        ones1 = coords_of_ones(img1)
        ones2 = coords_of_ones(img2)
        print(f'{ones1=}')
        print(f'{ones2=}')
        translations = tuple([
            (X1 - X2, Y1 - Y2)
            for (X1, Y1) in ones1
            for (X2, Y2) in ones2
        ])
        print(f'{translations=}')
        votes = Counter(translations)
        print(f'{votes=}')
        for trans, count in votes.most_common(1):
            print(f'{trans=} got {count} votes')
            return count

        return 0

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 544 ms Beats 39.76%
# NOTE: Memory 64.94 MB Beats 10.25%
