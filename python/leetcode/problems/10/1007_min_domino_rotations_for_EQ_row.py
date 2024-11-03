class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        REV = lambda x: tuple(reversed(tuple(x)))

        dominos = tuple(zip(tops,bottoms))
        # print(f'{dominos=}')
        
        sonimod = tuple(map(REV, dominos))
        # print(f'{sonimod=}')

        possible_numbers = set(dominos[0])
        # print(f'{possible_numbers=}')

        def getNumberOfRotates(number: int, dominos: List[Tuple[int,int]]) -> int:
            # returns the number of rotations needed, to get 'number' into
            # slot [0] of each domino, or None if this is impossible.
            rotations = [
                (
                    0
                    if A == number
                    else 1
                    if B == number
                    else None
                )
                for A, B in dominos
            ]
            # print(f'GNOR({number},{dominos}):')
            # print(f'  {rotations=}')
            return None if None in rotations else sum(rotations)
        
        answers = []
        for number in possible_numbers:
            rotates = getNumberOfRotates(number, dominos)
            answers.append(rotates)
            setator = getNumberOfRotates(number, sonimod)
            answers.append(setator)

        while None in answers:
            answers.remove(None)
        
        return min(answers, default=-1)

# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 225 ms Beats 5.26%
# NOTE: Memory 20.76 MB Beats 5.63%
