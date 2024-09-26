class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # we borrow some code from #207:

        all_courses = list(range(numCourses))
        # print(f'{all_courses=}')

        prereqs = {
            course: [
                P
                for (C, P) in prerequisites
                if C == course
            ]
            for course in all_courses
        }
        dependents_of = {
            course: [
                C
                for (C, P) in prerequisites
                if P == course
            ]
            for course in all_courses
        }

        course_order = []
        while all_courses:
            print()
            print(f'Scheduled: {len(course_order)}')
            print(f'Remaining: {len(all_courses)}')
            no_prereqs = [C for C in all_courses if prereqs[C] == []]
            print(f'  DEBUG: {no_prereqs=}')
            if len(no_prereqs) == 0:
                print(f'  No courses currently lack prerequisites!')
                return []
            for course in no_prereqs:
                print(f'  +{course}')
                all_courses.remove(course)
                course_order.append(course)
                for dependent in dependents_of[course]:
                    prereqs[dependent].remove(course)
                    print(f'    -{dependent}: {len(prereqs[dependent])}')

        return course_order

# NOTE: Accepted on first Submit
# NOTE: Runtime 743 ms Beats 5.03%
# NOTE: Memory 18.40 MB Beats 44.77%
