class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        
        ID = lambda R: R[0]
        RATING = lambda R: R[1]
        VEGAN = lambda R: R[2]
        PRICE = lambda R: R[3]
        DISTANCE = lambda R: R[4]

        print(f'init: count={len(restaurants)}')
        if veganFriendly:
            restaurants = tuple(filter(
                lambda R: VEGAN(R),
                restaurants
            ))
            print(f'vegan: count={len(restaurants)}')
        restaurants = tuple(filter(
            lambda R: PRICE(R) <= maxPrice,
            restaurants
        ))
        print(f'price: count={len(restaurants)}')
        restaurants = tuple(filter(
            lambda R: DISTANCE(R) <= maxDistance,
            restaurants
        ))
        print(f'distance: count={len(restaurants)}')
        BY_RATING_DESC_THEN_ID_DESC = lambda R: (-RATING(R), -ID(R))

        restaurants = sorted(
            restaurants,
            key=BY_RATING_DESC_THEN_ID_DESC
        )

        answer = [
            ID(R)
            for R in restaurants
        ]
        return answer

# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 24.08 MB Beats 82.69%
