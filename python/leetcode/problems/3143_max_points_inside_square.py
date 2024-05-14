class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:

        points_distance_tag = list([
            (max(abs(X), abs(Y)), (X, Y), s[i])
            for i, (X, Y) in enumerate(points)
        ])
        points_distance_tag.sort()
        print(f'{points_distance_tag=}')

        distances = [
            D
            for (D, P, T) in points_distance_tag
        ]
        distances = list(sorted(list(set(distances))))
        print(f'{distances=}')

        answer = 0
        tags = []
        for dist in distances:
            points_dist = [
                (D, P, T)
                for (D, P, T) in points_distance_tag
                if D == dist
            ]
            tags = tags + [
                T
                for (D, P, T) in points_dist
            ]
            tags.sort()
            print(f'{dist=} {tags=} {points_dist}')
            if len(tags) != len(set(tags)):
                print("DUPLICATE TAG")
                break
            
            answer += len(points_dist)

        return answer

