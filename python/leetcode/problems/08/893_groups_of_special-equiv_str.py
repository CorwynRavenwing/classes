class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        
        def getEquivalence(word: str) -> Tuple[str,str]:
            letters_polarized = sorted([
                (index % 2, letter)
                for (index, letter) in enumerate(word)
            ])
            evens = [
                letter
                for (polarity, letter) in letters_polarized
                if polarity == 0
            ]
            odds = [
                letter
                for (polarity, letter) in letters_polarized
                if polarity == 1
            ]
            return (''.join(evens), ''.join(odds))
        
        equivalence_groups = {}
        for word in words:
            equiv = getEquivalence(word)
            print(f'{word}: {equiv}')
            equivalence_groups.setdefault(equiv, set())
            equivalence_groups[equiv].add(word)

        print(f'equivalence_groups:')
        for equiv, words in equivalence_groups.items():
            print(f'  {equiv}: {words}')
        return len(equivalence_groups)

# NOTE: Accepted on first Submit
# NOTE: Runtime 19 ms Beats 99.52%
# NOTE: Memory 17.41 MB Beats 5.81%
