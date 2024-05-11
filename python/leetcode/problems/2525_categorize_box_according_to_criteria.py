class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:

        print(f"{length=} {width=} {height=} {mass=}")

        volume = length * width * height
        B = (
            (
                length >= 10**4
            ) or (
                width >= 10**4
            ) or (
                height >= 10**4
            ) or (
                volume >= 10**9
            )
        )
        
        H = (mass >= 100)

        print(f"{B=} {H=}")

        category = (
            "Both" if B and H
            else "Bulky" if B
            else "Heavy" if H
            else "Neither"
        )
        return category

