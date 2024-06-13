class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:

        faces = fronts + backs
        faces.sort()
        cards = tuple(zip(fronts, backs))

        print(f'{faces=}')
        print(f'{cards=}')

        for F in faces:
            if (F, F) not in cards:
                return F
        return 0

