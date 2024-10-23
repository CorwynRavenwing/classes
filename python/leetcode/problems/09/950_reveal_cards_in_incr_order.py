class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        
        deck.sort()

        answer = [None] * len(deck)
        indexes = list(range(len(deck)))

        while deck and indexes:
            index = indexes.pop(0)
            number = deck.pop(0)
            print(f'[{index}]={number}')
            assert answer[index] is None
            answer[index] = number
            if indexes:
                index = indexes.pop(0)
                print(f'\t\t[{index}]=back')
                indexes.append(index)
            
        if deck or indexes:
            raise Exception(f'ERROR: {deck=} but {indexes=}')
        
        assert None not in answer
        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 7 ms Beats 97.29%
# NOTE: Memory 16.93 MB Beats 24.76%
