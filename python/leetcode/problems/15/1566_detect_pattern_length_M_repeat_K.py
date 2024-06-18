class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for startPos in range(len(arr)):
            print(f"{startPos=}")
            pattern = arr[startPos:startPos + m] * k
            print(f"  {pattern=}")
            check = arr[startPos:startPos + (m * k)]
            print(f"  {check=}")
            if len(check) != (m * k):
                print("    SHORT")
                break
            if pattern == check:
                print("    YES")
                return True
            else:
                print("    no")
        return False

