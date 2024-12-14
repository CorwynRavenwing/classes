
        def countingSort(input: List[int]) -> List[int]:
            # return list(sorted(input))      # cheat
            value_upper_limit = (10 ** 5)
            counts = [0] * (value_upper_limit + 1)
            maxVal = -1
            for I in input:
                counts[I] += 1
                maxVal = max(I, maxVal)
            del counts[maxVal + 1:]
            print(f'{counts=}')
            answer = []
            for I, count in enumerate(counts):
                if count == 0:
                    continue
                answer.extend(
                    [I] * count
                )
            return answer

