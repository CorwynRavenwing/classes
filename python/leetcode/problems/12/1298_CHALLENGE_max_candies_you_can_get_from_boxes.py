class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        
        # SHORTCUT: there's no functional difference between a box whose status
        # is "open", and a box to which we have already found the key.
        # Therefore I'm going to initialize my keys-i-have array to the list
        # of boxes whose status is "open".

        keys_found = {
            key
            for key, value in enumerate(status)
            if value == 1
        }
        # print(f'{keys_found=}')

        boxes_found = set(initialBoxes)
        # print(f'{boxes_found=}')

        queue = set()
        candies_found = 0

        while True:
            boxes_to_open = keys_found & boxes_found
            boxes_found -= boxes_to_open
            print(f'Loop:\n\tkeys: {keys_found}\n\tboxs: {boxes_found}\n\topen: {boxes_to_open}')
            if not boxes_to_open:
                print(f'  Nothing in queue: quitting')
                break
            for box in boxes_to_open:
                print(f'  {box=}')
                candies_found += candies[box]
                print(f'    +candy:{candies[box]}')
                keys_found |= set(keys[box])
                print(f'    +keys: {keys[box]}')
                boxes_found |= set(containedBoxes[box])
                print(f'    +boxs: {containedBoxes[box]}')

        return candies_found

# NOTE: Acceptance Rate 66.1% (HARD)

# NOTE: Accepted on third Run (binary operator typo, var-name typo)
# NOTE: Accepted on first Submit
# NOTE: Runtime 86 ms Beats 5.36%
# NOTE: Memory 28.20 MB Beats 65.13%
