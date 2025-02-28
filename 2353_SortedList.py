# 2353. 设计食物评分系统
from typing import List
from sortedcontainers import SortedList

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.n = len(foods)
        self.food_rating_cuisine = dict()
        self.cuisine_rating_food = dict()
        for i in range(self.n):
            self.food_rating_cuisine[foods[i]] = [ratings[i],cuisines[i]]

            if cuisines[i] not in self.cuisine_rating_food:
                self.cuisine_rating_food[cuisines[i]] = SortedList(key=lambda x : [-x[0],x[1]])
            self.cuisine_rating_food[cuisines[i]].add([ratings[i], foods[i]])
        
    def changeRating(self, food: str, newRating: int) -> None:
        oldRating,cuisine = self.food_rating_cuisine[food]
        self.food_rating_cuisine[food][0] = newRating
        
        # 使用 remove 不存在时，会报错
        # self.cuisine_rating_food[cuisine].remove([oldRating, food])
        # 使用 discard 更安全，更方便，不存在时，不会报错
        self.cuisine_rating_food[cuisine].discard([oldRating, food])
        self.cuisine_rating_food[cuisine].add([newRating, food])

    def highestRated(self, cuisine: str) -> str:
        return self.cuisine_rating_food[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
