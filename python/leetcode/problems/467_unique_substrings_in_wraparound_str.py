class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:

        def show(frag: str) -> str:
            N = 5
            L = len(frag)
            fixed = frag[:N] + '...' + frag[-N:] + f' ({L})'
            print
            if len(fixed) < L:
                return fixed
            else:
                return frag
        
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        mod = len(alphabet)
        seen = {
            char: 0
            for char in alphabet
        }
        i = 0 - 1   # we're about to add 1 here
        while i + 1 < len(s):
            i += 1
            char = s[i]
            first_char = char
            j = i
            fragment = char
            seen[first_char] = max(seen[first_char], 1)
            print(f'{i=}     "{char}" "{show(fragment)}"')
            index = alphabet.index(char)
            while j + 1 < len(s):
                j += 1
                prev_char = char
                char = s[j]
                expected_index = (index + 1) % mod
                index = alphabet.index(char)
                fragment += char
                character_is_next = (expected_index == index)
                # print(f'{i=} {j=} "{char}" "{show(fragment)}" {character_is_next}')
                # fragment = s[i:j+1]
                if character_is_next:
                    seen[first_char] = max(seen[first_char], (j - i + 1))
                else:
                    j -= 1
                    fragment = fragment[:-1]
                    break
            # print(f'- {i=} {j=} "{char}" "{show(fragment)}"')
            k = 0
            while i < j:
                i += 1
                k += 1
                char = fragment[k]
                if char in fragment[:k]:
                    # print(f': seen "{char}"')
                    pass
                else:
                    # print(f': {i=} {j=} "{char}" "{show(fragment[k:])}"')
                    seen[char] = max(seen[char], (j - i + 1))

        return sum([
            count
            for char, count in seen.items()
        ])

