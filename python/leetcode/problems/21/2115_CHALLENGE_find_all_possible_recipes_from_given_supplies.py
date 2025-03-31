class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        recipes_w_ingredients = {
            recipe: set(ingredients_list)
            for recipe, ingredients_list in zip(recipes, ingredients)
        }
        # print(f'{recipes_w_ingredients=}')

        ingredient_usage = {}
        for recipe, ingredients_list in recipes_w_ingredients.items():
            for ingredient in ingredients_list:
                ingredient_usage.setdefault(ingredient, set())
                ingredient_usage[ingredient].add(recipe)
        # print(f'{ingredient_usage=}')

        queue = set(supplies)
        answer = set()
        while queue:
            ingredient = queue.pop()
            print(f'\nChecking "{ingredient}"')
            if ingredient not in ingredient_usage:
                print(f'  NOT USED')
                continue
            for recipe in ingredient_usage[ingredient]:
                # print(f'  Remove from "{recipe}"')
                recipes_w_ingredients[recipe].remove(ingredient)
                if len(recipes_w_ingredients[recipe]) == 0:
                    print(f'    No missing ingredients!')
                    answer.add(recipe)
                    queue.add(recipe)
                    del recipes_w_ingredients[recipe]
            # print(f'DEBUG: {recipes_w_ingredients=}')

        # print(f'(done): {recipes_w_ingredients=}')

        return tuple(answer)

# NOTE: Acceptance Rate 50.6% (MEDIUM)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 150 ms Beats 21.77%
# NOTE: Memory 21.17 MB Beats 19.64%

# NOTE: re-ran for challenge:
# NOTE: Runtime 153 ms Beats 95.44%
# NOTE: Memory 21.08 MB Beats 20.53%
