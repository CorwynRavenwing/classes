class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        # Gotta love those hints.  "Hint: do what the description said, using brute force"
        array = tuple(range(1, m + 1))

        def doQuery(Q: List[int]) -> int:
            nonlocal array
            print(f'{Q=}')
            index = array.index(Q)
            print(f'  :{index}')
            array = (Q,) + array[:index] + array[index + 1:]
            return index

        return [
            doQuery(Q)
            for Q in queries
        ]

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 23 ms Beats 30.23%
# NOTE: Memory 16.93 MB Beats 14.62%
