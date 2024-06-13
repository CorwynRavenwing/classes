class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:

        # each student must move the minimum distance, and therefore
        # should move to the Ith seat after sorting
        seats.sort()
        students.sort()
        answer = 0
        for (A, B) in zip(seats, students):
            print(f'{A}-{B}={A-B}')
            answer += abs(A - B)
        return answer

