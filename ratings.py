"""Restaurant rating lister."""

restaurant_ratings = {}
# put your code here
file = open('scores.txt')

for line in file:
    restaurant, rating = line.rstrip().split(":")

    restaurant_ratings[restaurant] = rating

for (restaurant, rating) in sorted(restaurant_ratings.items()):
    print (f"{restaurant} is rated at {rating}.")

