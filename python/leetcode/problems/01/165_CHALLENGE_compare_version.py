class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        list1 = list(map(int, version1.split('.')))
        list2 = list(map(int, version2.split('.')))
        print(f"{list1=}")
        print(f"{list2=}")
        updated = False
        while len(list1) < len(list2):
            list1 += [0]
            updated = True
        while len(list2) < len(list1):
            list2 += [0]
            updated = True
        if updated:
            print(f"{list1=}")
            print(f"{list2=}")
        
        if list1 < list2:
            return -1
        elif list1 > list2:
            return 1
        else:
            return 0

# NOTE: Acceptance Rate 43.0% (medium)

# NOTE: re-ran for challenge:
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.78 MB Beats 60.47%
