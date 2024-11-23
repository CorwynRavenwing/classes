class Solution:
    def entityParser(self, text: str) -> str:
        tags = {
            "&quot;": '"',
            "&apos;": "'",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/",
            "&amp;": "&",       # do ampersands last, so we don't double-decrypt
        }
        print(f'{text=}')
        for entity, value in tags.items():
            if entity in text:
                text = text.replace(entity, value)
                print(f'{text=}')
        return text

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 47 ms Beats 48.41%
# NOTE: Memory 17.22 MB Beats 74.23%
