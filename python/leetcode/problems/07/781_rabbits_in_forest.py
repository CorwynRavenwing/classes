class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        counts = Counter(answers)
        rabbits = 0
        for (answer, count) in sorted(counts.items()):
            groupSize = answer + 1  # rabbit does not count himself
            print(f'{count} rabbits said {answer} ({groupSize=})')
            fullGroups = count // groupSize
            thisType = fullGroups * groupSize
            if fullGroups:
                print(f'  {fullGroups=} -> {thisType=}')
                count -= thisType
                rabbits += thisType
            else:
                print(f'  no full groups')
            if count:
                print(f'  + {count} leftover rabbits in one more group of {groupSize}')
                rabbits += groupSize
                count -= count

        return rabbits

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 47 ms Beats 36.83%
# NOTE: Memory 16.82 MB Beats 9.21%
