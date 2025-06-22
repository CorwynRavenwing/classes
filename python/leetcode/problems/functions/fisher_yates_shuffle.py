
        def fisher_yates_shuffle(nums: List[int]) -> List[int]:
            answer = list(nums)
            for i in reversed(range(len(nums))):
                j = randint(0, i)
                # print(f'[{i}]: [{j}] {answer=}')
                (answer[i], answer[j]) = (answer[j], answer[i])
            return tuple(answer)

