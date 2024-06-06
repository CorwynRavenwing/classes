class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        groups = []
        hand.sort()
        while hand:
            # print(f'{hand[:10]=}')
            group = []
            start = min(hand)
            # print(f'look for hand starting at {start}:')
            for i in range(groupSize):
                card = start + i
                if card in hand:
                    # print(f'  found {card=}')
                    group.append(card)
                    hand.remove(card)
                else:
                    print(f'  MISSING {card=}')
                    return False
            # print(f'found {group=}')
            groups.append(group)
        # print(f'{groups=}')
        return True

