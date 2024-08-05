class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.Cuisine = {}
        self.Rating = {}
        self.CuisineRatings = {}
        for Food, Cuisine, Rating in zip(foods, cuisines, ratings):
            self.Cuisine[Food] = Cuisine
            self.Rating[Food] = Rating
            self.CuisineRatings.setdefault(Cuisine, [])
            bisect.insort(self.CuisineRatings[Cuisine], (-Rating, Food))
            # ratings are negative so we can sort ASC by rating and then food
            # and get "biggest number" first followed by "first alphabetic food"

        # print(f'{self.Cuisine=}')
        # print(f'{self.Rating=}')
        # print(f'{self.CuisineRatings=}')
        return

    def changeRating(self, food: str, newRating: int) -> None:
        oldRating = self.Rating[food]
        Cuisine = self.Cuisine[food]
        self.Rating[food] = newRating
        # print(f'changeRating(): {food} ({Cuisine}) {oldRating} -> {newRating}')
        # print(f'  before: {self.CuisineRatings[Cuisine]}')
        self.CuisineRatings[Cuisine].remove((-oldRating, food))
        bisect.insort(self.CuisineRatings[Cuisine], (-newRating, food))
        # print(f'  after : {self.CuisineRatings[Cuisine]}')
        return

    def highestRated(self, cuisine: str) -> str:
        ratedFoods = self.CuisineRatings[cuisine]
        (rating, food) = ratedFoods[0]     # highest
        return food

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)

# NOTE: Runtime 8100 ms Beats 5.20%
# NOTE: Memory 44.68 MB Beats 98.70%
