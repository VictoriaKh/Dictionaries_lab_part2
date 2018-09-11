"""Restaurant rating lister."""



def loadRatings(file):
    """ goes through a file and loads restaurant names and their ratings into 
    a restaurant_ratings dictionary, where the keys are the restaurant names.
    Returns the dictionary. 
    """
    restaurant_ratings = {}
    for line in file:
        restaurant, rating = line.rstrip().split(":")

        restaurant_ratings[restaurant] = rating
    return restaurant_ratings

def printRatings(restaurant_ratings):
    """ prints each restaurant and its rating, sorted in alphabetic order
    by restaurant name
    """
    for (restaurant, rating) in sorted(restaurant_ratings.items()):
        print (f"{restaurant} is rated at {rating}.")



def add_user_rating(restaurant_ratings):
  
    restaurant = input("\nPlease, enter restaurant name: ")
    while True:
        rating = input("Please enter restaurant score: ")
       
        try:
            rating = int(rating)
        except ValueError:
            print ("\nBad score. Please enter a number.")
            continue

        if 1 <= rating <= 5:
            print('good score')
            restaurant_ratings[restaurant.title()] = rating
            break;
        else:
            print("\nBad score. Please enter a score between 1 and 5 inclusive.")
            


def get_user_choice():
    print("\n\nWhat do you want to do?")
    print("Enter 1 to see all ratings")
    print("Enter 2 to review a restaurant")
    print("Enter 3 or q to quit")
    while True:
        choice = input("Enter your choice: ").lower()
        if choice not in ('1', '2', '3', 'q'):
            print("\nInvalid choice. Try again.")
            continue

        if choice == 'q': 
            return 3
        else:
            return choice


# put your code here
file = open('scores.txt')

rest_ratings_dict = loadRatings(file)

while True:
    choice = get_user_choice()
    if choice == '1':
        printRatings(rest_ratings_dict)
    elif choice == '2':
        add_user_rating(rest_ratings_dict)
    else:
        break

print("Quitting...")


