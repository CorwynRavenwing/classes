
        def all_substrings(s: str) -> List[str]:
            for i in range(len(s)):
                for j in range(i + 1, len(s) + 1):
                    yield s[i:j]

        def all_prefixes(s: str) -> List[str]:
            for i in [0]:
                for j in range(i + 1, len(s) + 1):
                    yield s[i:j]


