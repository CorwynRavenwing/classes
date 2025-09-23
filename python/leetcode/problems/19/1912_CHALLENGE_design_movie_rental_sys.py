class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        print(f'init({n}):')
        self.movie_price_by_shop = {}
        self.available_price_and_shop_by_movie = {}
        self.rented_by_price_shop_and_movie = []
        for (shop, movie, price) in entries:
            # create movie-prices dict for MPS[shop]:
            self.movie_price_by_shop.setdefault(shop, {})
            # set movie price at that shop
            self.movie_price_by_shop[shop][movie] = price
            
            # add (price, shop) tuple, sorted, to APSM[movie]
            self.available_price_and_shop_by_movie.setdefault(movie, [])
            inventory = (price, shop)
            bisect.insort(
                self.available_price_and_shop_by_movie[movie],
                inventory
            )

            # don't add movie to rented list
        # print(f'  {self.movie_price_by_shop=}')
        # print(f'  {self.available_price_and_shop_by_movie=}')
        # print(f'  {self.rented_by_price_shop_and_movie=}')

        return

    def search(self, movie: int) -> List[int]:
        print(f'search({movie})')
        self.available_price_and_shop_by_movie.setdefault(movie, [])
        answer = [
            shop
            for (price, shop) in self.available_price_and_shop_by_movie[movie][:5]
        ]
        print(f'  {answer=}')
        return answer

    def rent(self, shop: int, movie: int) -> None:
        print(f'rent({shop},{movie})')
        price = self.movie_price_by_shop[shop][movie]
        print(f'  @{price=}')

        rental = (price, shop, movie)
        bisect.insort(
            self.rented_by_price_shop_and_movie,
            rental
        )

        inventory = (price, shop)
        index = bisect_left(
            self.available_price_and_shop_by_movie[movie],
            inventory
        )
        record = self.available_price_and_shop_by_movie[movie].pop(index)
        assert record == inventory

        # print(f'  {self.available_price_and_shop_by_movie=}')
        # print(f'  {self.rented_by_price_shop_and_movie=}')
        return

    def drop(self, shop: int, movie: int) -> None:
        print(f'drop({shop},{movie})')
        price = self.movie_price_by_shop[shop][movie]
        print(f'  @{price=}')

        rental = (price, shop, movie)
        index = bisect_left(
            self.rented_by_price_shop_and_movie,
            rental
        )
        record = self.rented_by_price_shop_and_movie.pop(index)
        assert record == rental

        inventory = (price, shop)
        bisect.insort(
            self.available_price_and_shop_by_movie[movie],
            inventory
        )

        # print(f'  {self.available_price_and_shop_by_movie=}')
        # print(f'  {self.rented_by_price_shop_and_movie=}')
        return

    def report(self) -> List[List[int]]:
        print(f'report()')
        answer = [
            (shop, movie)
            for (price, shop, movie) in self.rented_by_price_shop_and_movie[:5]
        ]
        print(f'  {answer=}')
        return answer

# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()

# NOTE: Acceptance Rate 36.9% (HARD)

# NOTE: Accepted on first Run
# NOTE: Accepted on third Submit (edge case; Output Exceeded)
# NOTE: Runtime 1600 ms Beats 8.34%
# NOTE: Memory 125.70 MB Beats 19.17%
