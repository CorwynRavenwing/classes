class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:

        properties.sort()
        characters_by_attack = sorted(
            range(len(properties)),
            key=lambda x: properties[x][0]
        )
        characters_by_defense = sorted(
            range(len(properties)),
            key=lambda x: properties[x][1]
        )
        # print(f'{characters_by_attack=}')
        print(f'{characters_by_defense=}')

        answer = 0
        for Char1 in characters_by_attack:
            defense_position = characters_by_defense.index(Char1)
            for Char2 in characters_by_defense[defense_position + 1:]:
                if Char2 > Char1:
                    print(f'    {Char1} is weak to {Char2}')
                    answer += 1
                    # don't double-count Char1 being weak to every Char2
                    break
        return answer
# NOTE: also Time Limit Exceeded for large inputs.
# NOTE: a comment compares it to Russian Doll Envelopes,
#   which I am also having problems with.
