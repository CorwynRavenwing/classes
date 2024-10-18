class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:

        N = len(quiet)
        richerThan = {}
        for i in range(N):
            richerThan.setdefault(i, set())
        for (Ai, Bi) in richer:
            richerThan[Bi].add(Ai)
        
        @cache
        def peopleRicherThan(Id: int) -> Set[int]:
            print(f'PRT({Id}): RT={richerThan[Id]}')
            answer = {
                secondLevel
                for firstLevel in richerThan[Id]
                for secondLevel in peopleRicherThan(firstLevel)
            }
            answer.add(Id)
            print(f'->PRT({Id}): {answer}')
            return answer
        
        def leastQuietOf(IdList: Set[int]) -> int:
            quietnesses = [
                (quiet[Id], Id)
                for Id in IdList
            ]
            quietnesses.sort()
            print(f'{quietnesses=}')
            quietest = quietnesses[0]
            (volume, person) = quietest
            return person

        answer = []
        for i in range(N):
            RicherPeople = peopleRicherThan(i) 
            print(f'peopleRicherThan({i})={RicherPeople}')
            LQ = leastQuietOf(RicherPeople)
            print(f'  leastQuietOf()={LQ=}')
            answer.append(LQ)

        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 543 ms Beats 11.06%
# NOTE: Memory 37.27 MB Beats 5.40%
