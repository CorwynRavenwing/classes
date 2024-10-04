class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        playerCount = len(skill)
        print(f'{playerCount=}')
        if playerCount % 2 != 0:
            print(f'NO: non-even number of players.')
            return -1
        teamCount = playerCount // 2
        print(f'{teamCount=}')
        skillSum = sum(skill)
        print(f'{skillSum=}')
        if skillSum % teamCount != 0:
            print(f'NO: skills cannot be divided among teams.')
            return -1
        teamSkill = skillSum // teamCount
        print(f'{teamSkill=}')
        if teamSkill * teamCount != skillSum:
            print(f'NO: {teamSkill * teamCount=} != {skillSum=}')
            return -1
        teams = []
        while skill:
            player1 = skill.pop()
            player2 = teamSkill - player1
            print(f'({player1},{player2})')
            if player2 not in skill:
                print(f'  NO: skill "{player2}" does not exist')
                return -1
            else:
                skill.remove(player2)
            teams.append((player1, player2))
        print(f'{teams=}')
        chemistry = [
            A * B
            for A, B in teams
        ]
        print(f'{chemistry=}')
        return sum(chemistry)

# NOTE: Accepted on first Submit
# NOTE: Runtime 3056ms Beats 5.13%
# NOTE: Memory 28.74 MB Beats 98.41%
