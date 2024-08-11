
        def median(arr: List[int]) -> float:
            arr = sorted(arr)
            L = len(arr)
            if L % 2 == 1:
                index = L // 2
                return arr[index]
            else:
                indexA = L // 2 - 1
                indexB = L // 2
                total = sum([
                    arr[indexA],
                    arr[indexB],
                ])
                return total / 2

