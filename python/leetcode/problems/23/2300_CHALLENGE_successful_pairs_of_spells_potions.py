class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        # print(f'{spells=}')
        potions.sort()
        # print(f'{potions=}')
        retval = []
        prior_value = 0
        prior_answer = None
        for i, value in enumerate(spells):
            if prior_value == value:
                # print(f'  repeat {prior_answer}')
                retval.append(prior_answer)
                continue
            # print(f'spell[{i}]={value}')
            check = success // value
            if check * value < success:
                check += 1
            OK = (check * value) >= success
            # print(f'  {check=} *={check * value} {success=} {OK=}')
            firstgood = bisect.bisect_left(potions, check)
            # good = potions[firstgood:]
            # print(f'    potions[{firstgood}:]={good}')
            # print(f'    {firstgood} {len(potions)} {len(potions) - firstgood} {len(good)}')
            answer = len(potions) - firstgood
            prior_value = value
            prior_answer = answer
            retval.append(answer)
        return retval

# NOTE: Acceptance Rate 46.2% (medium)

# NOTE: 804ms Beats 97.26% of users with Python3

# NOTE: re-ran for challenge:
# NOTE: Runtime 163 ms Beats 90.23%
# NOTE: Memory 41.89 MB Beats 82.93%
