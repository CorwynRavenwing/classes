class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # print(f"{s=}")
        cleaned = list([
            ch.upper()
            for ch in s
            if ch != '-'
        ])
        # print(f"  {cleaned=}")
        answer = []
        while cleaned:
            group = cleaned[-k:]
            cleaned = cleaned[:-k]
            # print(f"    {cleaned} || {group}")
            answer.append(
                ''.join(group)
            )
        # print(f"  {list(reversed(answer))}")
        return '-'.join(reversed(answer))

