class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        town = tuple(range(1, n+1))
        # print(f"{n=}")
        # print(f"{trust=}")
        print(f"{town=}")
        for person in town:
            print(f"  {person=}")
            i_trust = tuple([
                B
                for (A, B) in trust
                if A == person
            ])
            print(f"    {i_trust=}")
            if i_trust:
                print("      NOT ME")
                continue
            trust_me = tuple([
                A
                for (A, B) in trust
                if B == person
            ])
            print(f"    {trust_me=}")
            missing_trust = tuple([
                P
                for P in town
                if (P != person) and (P not in trust_me)
            ])
            print(f"    {missing_trust=}")
            if missing_trust:
                print("      NOT ME")
                continue
            print("      YES!")
            return person
        return -1

