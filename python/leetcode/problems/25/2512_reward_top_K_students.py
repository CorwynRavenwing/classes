class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positive_set = set(positive_feedback)
        negative_set = set(negative_feedback)
        RawScores = [
            (
                Student,
                [
                    (
                        3 if word in positive_set else
                        -1 if word in negative_set else
                        0
                    )
                    for word in Report.split(' ')
                ]
            )
            for Report, Student in zip(report, student_id)
        ]
        print(f'{RawScores=}')
        scores = [
            (Student, sum(scoreList))
            for (Student, scoreList) in RawScores
        ]
        scores.sort(
            key=lambda x: (-x[1], x[0])     # by score DESC then id ASC
        )
        print(f'{scores=}')

        return [
            Student
            for (Student, Score) in scores[:k]
        ]
# NOTE: Runtime 342 ms Beats 10.74%
# NOTE: Memory 27.21 MB Beats 5.18%
