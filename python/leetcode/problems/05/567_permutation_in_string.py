class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        count1 = Counter(s1)
        count2 = Counter(s2)

        for (letter, C1) in count1.items():
            if letter not in count2:
                print(f'{letter=} not in s2!')
                return False
            C2 = count2[letter]
            if C1 > C2:
                print(f'Not enough "{letter}" in s2!  {C1} > {C2}')
                return False
        
        del count2  # we will reuse this variable later

        # print(f'{count1=}')
        for i, letter in enumerate(s2):
            print(f's2[{i}]="{letter}":')
            if letter not in s1:
                print(f'  not in s1')
                continue
            count2 = Counter(letter)
            fragment = letter
            for j in range(i + 1, i + len(s1)):
                if j >= len(s2):
                    # print(f'    {j=} >= {len(s2)} OOB')
                    break
                letter = s2[j]
                # print(f'  s2[{j}] = "{letter}"')
                if letter not in s1:
                    # print(f'    not in s1')
                    break
                count2[letter] += 1
                fragment += letter
            # print(f'{fragment=} {count2=}')
            if count1 == count2:
                return True
        return False

