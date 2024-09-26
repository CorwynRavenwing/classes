class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        prereqs = {
            course: list([
                P
                for (C, P) in prerequisites
                if C == course
            ])
            for course in range(numCourses)
        }

        all_courses = list(range(numCourses))
        # print(f'{all_courses=}')

        while any((prereqs[C] != [] for C in all_courses)):
            for C in all_courses:
                print(f'{C=}')
                PR = prereqs[C]
                if C in PR:
                    print(f'  found course {C=} in its own prereqs {PR} (before)')
                    return False
                new_PR = []
                for P in PR:
                    Q = prereqs[P]
                    print(f'  {P} -> {Q}')
                    new_PR.extend(Q)
                # print(f':{PR} => {new_PR}')
                if C in PR:
                    print(f'  found course {C=} in its own prereqs {new_PR} (after)')
                    return False
                prereqs[C] = new_PR
        
        if all((prereqs[C] == [] for C in all_courses)):
            print(f'all prereqs blank')
            return True
        
        print(f'Not sure how we got here')
        return False

# NOTE: Runtime 570 ms Beats 5.02%
# NOTE: Memory 20.65 MB Beats 5.96%
