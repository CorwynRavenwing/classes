class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # Algorithm:
        # 1. Find the position, in array "arr", of element target[0]
        # 2a. if it does not exist, return FALSE
        # 2b. if it is already in position 0, move on to step 3.
        # 2c. otherwise, reverse subarray [0 .. position of that element]
        # 3. now we have an array whose 0th element is in the right place
        # 4. repeat algoritm for subarray arr[1:] and element target[1], etc.
        # 5. at the end of this process, the arrays will be equal.
        # 6. return TRUE

        # Conclusion:
        # if the two strings contain all the same elements, TRUE, else FALSE.
        # therefore this is equivalent:
        return (sorted(arr) == sorted(target))
# NOTE: yes, 14 lines of comment and 1 line of code
# NOTE: Runtime 78 ms Beats 33.83%
# NOTE: Memory 16.70 MB Beats 59.96%
