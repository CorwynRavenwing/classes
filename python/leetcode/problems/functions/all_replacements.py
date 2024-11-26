
        # replaces each single char in "s" with one char in "replace"
        def all_replacements(s: str, replace: str) -> List[str]:
            for i in range(len(s)):
                left = s[:i]
                right = s[i + 1:]
                for c in replace:
                    yield left + c + right

