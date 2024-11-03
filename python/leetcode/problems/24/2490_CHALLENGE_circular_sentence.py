class Solution:
    def isCircularSentence(self, sentence: str) -> bool:

        words = sentence.split(' ')
        print(f'{words=}')
        
        words.append(words[0])
        # duplicate the first word onto the end
        # this takes care of circularity requirement

        links = [
            (A[-1], B[0])
            for A, B in pairwise(words)
        ]
        print(f'{links=}')

        same = [
            A == B
            for A, B in links
        ]
        print(f'{same=}')

        return all(same)

# NOTE: Accepted on second Run (first was punctuation typo)
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 16.48 MB Beats 80.88%
