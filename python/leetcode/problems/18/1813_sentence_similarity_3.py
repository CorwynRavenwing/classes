class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:

        tokens1 = sentence1.split(' ')
        tokens2 = sentence2.split(' ')
        if tokens1 == tokens2:
            print(f'YES: Already identical')
            return True

        if len(tokens1) == len(tokens2):
            print(f'NO: Already same length')
            return False

        if len(tokens1) < len(tokens2):
            (tokens1, tokens2) = (tokens2, tokens1)
            # now tokens1 is the longer one
        
        print(f'{len(tokens1)}, {len(tokens2)}')
        # remove identical tokens from the front
        while tokens1 and tokens2 and tokens1[0] == tokens2[0]:
            del tokens1[0]
            del tokens2[0]
            print(f'FRONT: {len(tokens1)}, {len(tokens2)}')
        
        # remove identical tokens from the back
        while tokens1 and tokens2 and tokens1[-1] == tokens2[-1]:
            del tokens1[-1]
            del tokens2[-1]
            print(f'BACK: {len(tokens1)}, {len(tokens2)}')
        
        return (tokens2 == [])

