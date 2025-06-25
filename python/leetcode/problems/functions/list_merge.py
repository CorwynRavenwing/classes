
        # takes two sorted lists: outputs one sorted list
        # containing all members of both lists (incl. duplicates)

        def listMerge(list1: List[int], list2: List[int]) -> List[int]:
            answer = []
            while list1 and list2:
                if list1[0] < list2[0]:
                    answer.append(list1[0])
                    list1 = list1[1:]
                elif list1[0] > list2[0]:
                    answer.append(list2[0])
                    list2 = list2[1:]
                elif list1[0] == list2[0]:
                    answer.append(list1[0])
                    answer.append(list2[0])
                    list1 = list1[1:]
                    list2 = list2[1:]
            while list1:
                answer.append(list1[0])
                list1 = list1[1:]
            while list2:
                answer.append(list2[0])
                list2 = list2[1:]
            return answer

        # generator version, which allows generators as inputs
        def listMerge(list1: List[int], list2: List[int]) -> List[int]:
            print(f'listMerge():')
            A_iter = iter(list1)
            B_iter = iter(list2)
            # returns a GENERATOR.  May NOT be cached.
            A = next(A_iter, None)
            B = next(B_iter, None)
            # print(f'  {A=} {B=}')
            
            while A is not None and B is not None:      
                if A < B:
                    yield A
                    print(f'USE A: {A} < {B}')
                    A = next(A_iter, None)
                else:
                    yield B
                    print(f'USE B: {A} > {B}')
                    B = next(B_iter, None)
            print(f'Loop exited:')
            print(f'  {A=} {B=}')

            while A is not None:
                yield A
                print(f'USE A: {A} not empty')
                A = next(A_iter, None)
            while B is not None:
                yield B
                print(f'USE B: {B} not empty')
                B = next(B_iter, None)

            return

