        def replaceMultipleTimes(haystack: str, needle: str, replacement: str) -> str:
            prior = haystack + 'guaranteed not to match'
            while prior != haystack:
                prior = haystack
                haystack = haystack.replace(needle, replacement)
            return haystack

        # --- OR ---

        def replaceMultipleTimes(haystack: str, needle: str, replacement: str) -> str:
            while needle in haystack:
                haystack = haystack.replace(needle, replacement)
            return haystack

