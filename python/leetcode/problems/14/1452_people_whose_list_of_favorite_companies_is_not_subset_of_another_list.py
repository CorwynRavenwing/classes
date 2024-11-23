class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        
        favoriteCompanySets = tuple(map(set, favoriteCompanies))
        # print(f'{favoriteCompanySets=}')

        # SHORTCUT 1: because of the "favorite lists are distinct" constraint,
        # we don't need to check people whose set is smaller than ours.
        sets_by_size = {}
        for mySet in favoriteCompanySets:
            myLength = len(mySet)
            sets_by_size.setdefault(myLength, [])
            sets_by_size[myLength].append(mySet)
        # print(f'{sets_by_size=}')

        answer = []
        for index, mySet in enumerate(favoriteCompanySets):
            print(f'[{index}]:{mySet}')
            myLength = len(mySet)
            is_a_subset = False
            for hisLength, allSets in sets_by_size.items():
                if myLength >= hisLength:
                    continue
                for hisSet in allSets:
                    myUnique = mySet - hisSet
                    if not myUnique:
                        print(f'  subset of {hisSet}')
                        is_a_subset = True
                        break
                if is_a_subset:
                    break

            if not is_a_subset:
                print(f'  NOT a subset')
                answer.append(index)
        
        return answer

# NOTE: Accepted on second Run (first was inverted logic error)
# NOTE: Accepted on first Submit
# NOTE: Runtime 75 ms Beats 87.50%
# NOTE: Memory 32.53 MB Beats 61.45%
