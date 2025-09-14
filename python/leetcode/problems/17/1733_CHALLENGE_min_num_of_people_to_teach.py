class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:

        personLanguageSet = tuple(map(set, languages))
        # print(f'{personLanguageSet=}')

        min_teach = float('+inf')
        for Language in range(1, n + 1):
            teach = set()
            for A, B in friendships:
                A -= 1  # zero-index
                B -= 1
                # print(f'({A},{B})')
                setA = personLanguageSet[A]
                setB = personLanguageSet[B]
                shared_languages =  setA & setB     # set intersection
                if shared_languages:
                    # print(f'  {shared_languages=}')
                    continue
                A_knows_now = Language in setA or A in teach
                B_knows_now = Language in setB or B in teach
                if A_knows_now and B_knows_now:
                    # print(f'  shared language #{Language}')
                    continue
                if not A_knows_now:
                    teach.add(A)
                    # print(f'  teach {A} #{Language}')
                if not B_knows_now:
                    teach.add(B)
                    # print(f'  teach {B} #{Language}')
            min_teach = min(len(teach), min_teach)

        return min_teach

# NOTE: Acceptance Rate 49.2% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 5656 ms Beats 5.22%
# NOTE: Memory 31.82 MB Beats 7.98%

# NOTE: re-ran for challenge:
# NOTE: Runtime 5597 ms Beats 6.10%
# NOTE: Memory 31.64 MB Beats 76.83%
