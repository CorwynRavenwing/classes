class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        while len(arr1) < len(arr2):
            arr1 = [0] + arr1
        while len(arr2) < len(arr1):
            arr2 = [0] + arr2
        print(f'{arr1=}')
        print(f'{arr2=}')
        total = list(map(sum, zip(arr1, arr2)))

        while min(total) < 0 or max(total) > 1:
            print(f'A {total=}')
            if total[0] not in [0, 1]:
                total = [0] + total
                continue
            if min(total) < 0:
                index = total.index(min(total))
                total[index] += 2
                total[index - 1] += 1
                continue
            if max(total) > 1:
                index = total.index(max(total))
                total[index] -= 2
                total[index - 1] -= 1
                continue
        print(f'B {total=}')
        while (len(total) > 1) and (total[0] == 0):
            del total[0]
            print(f'C {total=}')
        return total

