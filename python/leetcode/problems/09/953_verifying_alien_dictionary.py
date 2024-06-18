class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        def by_alien_alphabet(word: str) -> List[int]:
            print(f"BAA '{word}'")
            answer = [
                order.index(ch)
                for ch in word
            ]
            print(f"  {answer}")
            return answer
        
        correct = sorted(
            words,
            key=by_alien_alphabet
        )
        print(f"in: {words}")
        print(f"out:{correct}")
        return (words == correct)

