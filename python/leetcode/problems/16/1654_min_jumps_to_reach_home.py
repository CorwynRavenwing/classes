class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:

        if x == 0:
            return 0
        
        forbidden_set = set(forbidden)  # make lookups faster
        forbidden_max = max(forbidden)

        MAX = 1_000_000

        seen = set()
        jumps = 0
        queue = {(0, False)}
        while queue:
            print(f'J={jumps}: L={len(queue)}  min={min(queue)[0]} max={max(queue)[0]}')
            newQ = set()
            for P in queue:
                # print(f'{jumps}: {P}')
                if P in seen:
                    # print(f'  (seen)')
                    continue
                else:
                    seen.add(P)
                (position, last_went_backwards) = P
                # print(f'{(position,last_went_backwards)}')
                if position == x:
                    # print(f'  FOUND')
                    return jumps
                for going_backwards in [False, True]:
                    direction = ("B" if going_backwards else "F")
                    if going_backwards and last_went_backwards:
                        # print(f'  {direction} (back twice)')
                        # don't do it twice
                        continue
                    new_position = (
                        position + (
                            -b
                            if going_backwards
                            else a
                        )
                    )
                    if new_position < 0:
                        # print(f'  {direction} below zero')
                        # don't go below zero
                        continue
                    if new_position in forbidden_set:
                        # print(f'  {direction} forbidden')
                        # don't hit a forbidden location
                        continue
                    if new_position > MAX:
                        # print(f'  {direction} too high')
                        # too high
                        continue
                    # print(f'  {direction} -> {new_position}')
                    newQ.add(
                        (new_position, going_backwards)
                    )
                
            queue = newQ
            jumps += 1

            if jumps > 10_000:
                break
            
        return -1

# NOTE: Runtime 8678 ms Beats 5.19%
# NOTE: Memory 301.36 MB Beats 5.11%
