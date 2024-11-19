        def listIntersect(list1: List[int], list2: List[int]) -> List[int]:
            answer = []
            while list1 and list2:
                if list1[0] < list2[0]:
                    list1 = list1[1:]
                elif list1[0] > list2[0]:
                    list2 = list2[1:]
                elif list1[0] == list2[0]:
                    answer.append(list1[0])
                    list1 = list1[1:]
                    list2 = list2[1:]
            return answer

