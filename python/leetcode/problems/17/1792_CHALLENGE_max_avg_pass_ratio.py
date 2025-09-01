class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        
        def class_average(passing: int, total: int) -> float:
            return passing / total
        
        def average_increase_object(passing: int, total: int) -> Tuple[float,int,int]:
            increase = class_average(passing + 1, total + 1) - class_average(passing, total)
            return (increase, passing, total)
        
        def show_pass_ratio(objects: List[Tuple[float,int,int]]) -> float:
            pass_ratio_total = 0.0
            pass_ratio_count = 0
            for index, (increase, passing, total) in enumerate(objects):
                pass_ratio = class_average(passing, total)
                print(f'  {index}:\t{passing}/{total}\t-> {pass_ratio}')
                pass_ratio_total += pass_ratio
                pass_ratio_count += 1
            answer = pass_ratio_total / pass_ratio_count
            print(f'TOTAL: {pass_ratio_total} / {pass_ratio_count}\t-> {answer}')
            return answer
        
        class_list = []
        for (passing, total) in classes:
            obj = average_increase_object(passing, total)
            bisect.insort(class_list, obj)

        answer = show_pass_ratio(class_list)
        for student in range(extraStudents):
            # print(f'Add student #{student + 1}')
            (increase, passing, total) = class_list.pop(-1)     # highest increase
            obj = average_increase_object(passing + 1, total + 1)
            bisect.insort(class_list, obj)
            # answer = show_pass_ratio(class_list)

        answer = show_pass_ratio(class_list)
        
        return answer

# NOTE: Acceptance Rate 71.8% (medium)

# NOTE: Accepted on second Run (one-char typo)
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 3066 ms Beats 5.55%
# NOTE: Memory 54.69 MB Beats 26.32%

# NOTE: re-ran for challenge:
# NOTE: Runtime 2830 ms Beats 5.33%
# NOTE: Memory 54.83 MB Beats 16.67%

# NOTE: Another challenge:
# NOTE: Runtime 2989 ms Beats 5.65%
# NOTE: Memory 55.26 MB Beats 7.39%
