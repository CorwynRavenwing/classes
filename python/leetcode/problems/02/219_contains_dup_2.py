<pre>class Solution:

    # we borrow some code from #217:
    def containsDuplicate(self, nums: List[int]) -&gt; bool:
        return len(nums) != len(set(nums))

    def containsNearbyDuplicate(self, nums: List[int], k: int) -&gt; bool:

        if not self.containsDuplicate(nums):
            return False
        
        indexes_by_value = {}
        for index, value in enumerate(nums):
            indexes_by_value.setdefault(value, [])
            indexes_by_value[value].append(index)
        print(f'{indexes_by_value=}')

        for value, indexes in indexes_by_value.items():
            print(f'&quot;{value}&quot;: {indexes}')
            if len(indexes) == 1:
                continue
            distances = [
                B - A
                for A, B in pairwise(indexes)
            ]
            print(f'  {distances=}')
            if min(distances) &lt;= k:
                print(f'    YES')
                return True
        
        print(f'  NO')
        return False

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 115 ms Beats 5.04%
# NOTE: Memory 49.68 MB Beats 5.19%</pre>