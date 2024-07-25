class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:

        def AliceWinsIfSheChooses(stone: int, stones: List[int]) -> bool:
            print(f'\nAlice attempts picking {stone=}:')

            def pick_correct_move(total: int) -> int:
                stone = (
                    1 if total == 1 else
                    2 if total == 2 else
                    0
                )
                return stone
            
            def pick_any_available_stone(counts: Counter) -> int:
                stone = (
                    0 if counts[0] else
                    1 if counts[1] else
                    2 if counts[2] else
                    None
                )
                return stone

            def show(counts: Counter) -> str:
                display = [
                    counts[i]
                    for i in range(3)
                ]
                return f'[{" ".join(map(str, display))}]'
            
            prior = (-1, -1)
            prior_count = 0

            # Alice chooses a stone (passed in)
            aliceStone = stone
            if aliceStone not in stones:
                print(f'  Cannot actually take {aliceStone=}, there are none')
                return None
            counts = Counter(stones)
            total = 0
            print(f'BEFORE stone=X {total=} counts={show(counts)}')
            while True:
                counts[aliceStone] -= 1
                total += aliceStone
                total %= 3
                print(f'ALICE  {aliceStone=} {total=} counts={show(counts)}')
                if total == 0:
                    print(f'  Total 0: Alice loses!')
                    return False
                # Bob chooses a stone
                bobStone = pick_correct_move(total)
                if counts[bobStone] == 0:
                    print(f'  Bob wants {bobStone=}, but there are none')
                    bobStone = pick_any_available_stone(counts)
                    if bobStone is None:
                        print(f'  Out of stones!  Bob wins!')
                        return False
                    else:
                        print(f'    -> {bobStone=} instead')
                counts[bobStone] -= 1
                total += bobStone
                total %= 3
                print(f'BOB      {bobStone=} {total=} counts={show(counts)}')
                if total == 0:
                    print(f'  Total 0: Bob loses!')
                    return True
                
                pair = (aliceStone, bobStone)
                if prior != pair:
                    prior = pair
                    prior_count = 1
                else:
                    prior_count += 1
                    if prior_count >= 3:
                        print(f'\nWe are in a repeating pattern ...\n')
                        jump_forward = min(
                            counts[aliceStone],
                            counts[bobStone],
                        )
                        jump_forward -= (jump_forward % 5)   # round to nearest 5
                        if aliceStone == bobStone:
                            # split the available stones between them
                            jump_forward //= 2
                        print(f'ALICE  {aliceStone=} X {jump_forward}')
                        print(f'BOB      {bobStone=} X {jump_forward}')
                        counts[aliceStone] -= jump_forward
                        counts[bobStone] -= jump_forward
                        total += (aliceStone * jump_forward)
                        total += (bobStone * jump_forward)
                        total %= 3
                        print(f'AFTERWARDS: {total=} counts={show(counts)}')
                        prior_count = -20   # don't repeat this jump
                        print(f'\n... end repetition\n')

                # Alice chooses a stone
                aliceStone = pick_correct_move(total)
                if counts[aliceStone] == 0:
                    print(f'  Alice wants {aliceStone=}, but there are none')
                    aliceStone = pick_any_available_stone(counts)
                    if aliceStone is None:
                        print(f'  Out of stones!  Bob wins!')
                        return False
                    else:
                        print(f'    -> {aliceStone=} instead')
                # Alice's stone is counted at top of loop

        print(f'stones={stones[:10]}{"..." if (len(stones) > 10) else ""}')
        stones = [
            S % 3
            for S in stones
        ]
        print(f'stones={stones[:10]}{"..." if (len(stones) > 10) else ""}')
        Play1 = AliceWinsIfSheChooses(1, stones)
        Play2 = AliceWinsIfSheChooses(2, stones)
        return (Play1 or Play2)
# NOTE: Runtime 996 ms Beats 51.76%
# NOTE: Memory 30.89 MB Beats 23.53%
