class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        indexesByValue = {}
        for index, value in enumerate(groupSizes):
            indexesByValue.setdefault(value, [])
            indexesByValue[value].append(index)
        print(f'{indexesByValue=}')

        # we borrow some code from #781:
        # ... and then mangle it out of recognizabiity

        people = []

        for (count, indexes) in sorted(indexesByValue.items()):
            print(f'{len(indexes)} people said {count}')
            while indexes:
                thisGroup = indexes[:count]
                print(f'  {thisGroup}')
                people.append(thisGroup)
                indexes = indexes[count:]

        return people

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 71 ms Beats 23.59%
# NOTE: Memory 16.82 MB Beats 5.83%
