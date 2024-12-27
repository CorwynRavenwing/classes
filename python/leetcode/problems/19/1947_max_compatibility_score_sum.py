class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:

        @cache
        def compatibility_between(studentIndex: int, mentorIndex: int) -> int:
            S = students[studentIndex]
            M = mentors[mentorIndex]
            CompatBits = [
                (1 if (A == B) else 0)
                for A, B in zip(S, M)
            ]
            count = sum(CompatBits)
            # print(f'  {S=} {M=} {CompatBits=} {count=}')
            return count
        
        @cache
        def DP(studentIndex: int, availableMentorIndexes: List[int]) -> int:
            print(f'DP({studentIndex},{availableMentorIndexes})')
            if not availableMentorIndexes:
                # print(f'  ... Out of mentors')
                return 0
            check = students[studentIndex]

            answers = []
            for mentorIndex in availableMentorIndexes:
                otherMentors = tuple(
                    sorted(
                        set(availableMentorIndexes) - {mentorIndex}
                    )
                )
                # print(f'  DEBUG: {mentorIndex=} {otherMentors=}')
                compat = compatibility_between(studentIndex, mentorIndex)
                # print(f'  DEBUG: compat({studentIndex},{mentorIndex}) -> {compat}')
                answers.append(
                    compat + DP(studentIndex + 1, otherMentors)
                )
            print(f'DP({studentIndex},{availableMentorIndexes}): {answers=}')
            return max(answers)
        
        allMentorIndexes = tuple(range(len(mentors)))
        return DP(0, allMentorIndexes)

# NOTE: Accepted on second Run (forgot that 0==0 is a match)
# NOTE: Accepted on first Submit
# NOTE: Runtime 30 ms Beats 69.09%
# NOTE: Memory 18.50 MB Beats 11.52%
