class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        S = list(senate)
        while True:
            print(f'{"".join(S)}')
            for i, party in enumerate(S):
                print(f'  S[{i}]={party}:')
                if party == 'X':
                    continue
                otherparty = ('R' if party == 'D' else 'D')
                if otherparty not in S:
                    print(f'    No {otherparty} in senate!')
                    return (
                        'Dire'
                        if party == 'D'
                        else 'Radiant'
                    )
                try:
                    indexForward = S.index(otherparty, i)
                except ValueError:
                    indexForward = None
                    
                if indexForward is not None:
                    print(f'    found {otherparty} forward at {indexForward=}')
                    S[indexForward] = 'X'
                    continue
                else:
                    index = S.index(otherparty)
                    print(f'    found {otherparty} backward at {index=}')
                    S[index] = 'X'
                    continue

