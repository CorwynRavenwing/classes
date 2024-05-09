class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        def count_bits(N: int) -> int:
            if not N:
                return 0
            return (N % 2) + count_bits(N // 2)
        
        def by_number_of_bits(N: int) -> Tuple[int,int]:
            return (count_bits(N), N)
        
        return sorted(
            arr,
            key=by_number_of_bits
        )

