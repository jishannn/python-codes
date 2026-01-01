# bicycles = ['trek', 'cannodlae', 'redline', 'specialized']
# print(bicycles)
# print(bicycles[0])                 # Output trek
# print(bicycles[0].title())         # Produces trek in capitalized which is Trek #

# message = f"My first bicycle was a {bicycles[0].title()}."
# print(message);

# motorcycles = ['honda', 'yamaha', 'suzuki']
<<<<<<< HEAD
# print(motorcycles);
=======
# print(motorcocles);
>>>>>>> 0ab4417 (hash table folder added.)

# motorcycles[0] = 'ducati'
# print(motorcycles);




# Adding elements to a list

# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles);

# motorcycles.append('ducati')
# print(motorcycles);


# motorcycles = [];

# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')

# print(motorcycles);

# motorcycles.insert(0, 'ducati')          # Inserting Elements into a List
# print(motorcycles);



# motorcycles = ['honda', 'yamaha', 'suzuki'];
# print(motorcycles)

# del motorcycles[0]             # Removing an item using the del statement
# print(motorcycles)

# del motorcycles[1]
# print(motorcycles);


# Removing an item using  the pop() method

# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles);

# popped_motorcycle = motorcycles.pop()
# print(motorcycles);
# print(popped_motorcycle);


# motorcycles = ['honda', 'yamaha', 'suzuki']

# last_owned = motorcycles.pop()
# last_owned = motorcycles.pop(0)
# print(f"The last motorcycles I owned was a {last_owned.title()}.");


# Removing an Item by Value:

# Example:1

# motorcycles =['honda', 'yamaha', 'suzuki', 'ducati']
# print(motorcycles)

# motorcycles.remove('ducati')
# print(motorcycles);

# Example:2

# motorcycles =['honda', 'yamaha', 'suzuki', 'ducati']

# too_expensive = 'ducati'
# motorcycles.remove(too_expensive)
# print(motorcycles)
# print(f"\nA {too_expensive.title()} is too expensive for me.");

# Orgnaizing a List:
# Sorting a List Permanently with the sort() Method

# Ex:1
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# print(cars)

# Ex:2 - Reverse order or reverse sort() Method
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()        
# print(cars)           # alphabetical order
# cars.sort(reverse=True)
# print(cars)           # reverse alphabetical order


# Sorting a List Temporarily with the sorted() Function:

# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print('Here is the original list:')
# print(cars)

# print('\nHere is the sorted list:')
# print(sorted(cars))

# print('\nHere is the original list again:')
# print(cars)

# Printing a List in Reverse Order:

# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print(cars)

# cars.reverse()
# print(cars)

# Finding length of a list using len() function:

# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print(len(cars))

# Avoiding Index Errors When Working with Lists

# Error Ex-1:

# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles[3])           # this will give a index error

# Ex:1
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles[-1])        # returns the last item in a list


# Looping through an entire list:

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     # print(magician)
#     print(f"{magician.title()}, that was a great trick!")
#     print(f"I can't wait to see your next trick, {magician.title()}.\n")

# print("Thank you, everyone. That was a great magic show!")



# Forgetting to Indent

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
# print(magician)          # it will give error because of indentation...


# Ex-2:
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
# print(f"I can't wait to see your next trick, {magician.title()}.\n")


# Making Numerical Lists

# range() function
# for value in range(1, 5):
#     print(value)

# range() function to make a List of Numbers
# numbers = list(range(1, 6))
# print(numbers)

# even_numbers = list(range(2, 11, 2))
# print(even_numbers)

# squares = []
# for value in range(1, 11):
#     square = value ** 2
#     squares.append(square)

# print(squares)

# # or

# squares = []
# for value in range(1, 11):
#     squares.append(value**2)

# print(squares)


# Simple Statistics with a List of Numbers
# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(min(digits))
# print(max(digits))
# print(sum(digits))


# List Comprehension
# squares = [value**2 for value in range(1, 11)]
# print(squares)


# Working with Part of a List
# Slicing a List
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[0:3])
# print(players[1:4])
# print(players[:4])
# print(players[2:])

# print(players[-3:])


# Looping Through a List
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print('Here are the first three players on my team:')
# for player in players[:3]:
#     print(player.title())


# Copying a List
# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]

# print('My favorite foods are:')
# print(my_foods)

# print("\nMy friend's favorite foods are:")
# print(friend_foods)


# my_foods.append('cannoli')
# friend_foods.append('ice cream')

# print("\nMy favorite foods are:")
# print(my_foods)

# print("\nMy friend's favorite foods are:")
# print(friend_foods)


# Tuple
# dimension = (200, 50)
# print(dimension[0])
# print(dimension[1])

# dimension[0] = 300
# print(dimension[0])         # will show error because Tuples are constant in Python.



# Looping Through All Values in a Tuple
# dimensions = (200, 50)
# for dimension in dimensions:
#     print(dimension)

# Writing over a Tuple
# dimensions = (200, 50)
# print('Original dimensions:')
# for dimension in dimensions:
#     print(dimensions)


# dimensions = (400, 100)
# print("\nModified dimensions:")
# for dimension in dimensions:
#     print(dimensions)



# If Statement
# cars = ['audi', 'bmw', 'subaru', 'toyota']

# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())


# --- Conditional Tests
# Checking for Equality

# car = 'bmw'

# if car == 'bmw':
#     print(True)

# Checking for Inequality
# requested_topping = 'mushrooms'

# if requested_topping != 'anchovies':
#     print('Hold the anchovies!')


# Numerical Comparisons
# age = 18
# if age == 18:
#     print(True)


# answer = 17

# if answer != 42:
#     print('That is not the correct answer. Please try again!')

# age = 19

# if age < 21:
#     print(True)

# if age <= 21:
#     print(True)

# if age > 21:
#     print(False)

# if age >= 21:
#     print(False)




# Using 'and' to Check Multiple Conditions
# age_0 = 22
# age_1 = 18

# checking_age_0 = (age_0 >= 21) and (age_1 >= 21)      # Parentheses are not required i.e. (age_0 >= 21) and anything like this, just for improving readability.
# print(checking_age_0)

# age_1 = 22
# checking_age_1 = (age_0 >= 21) and (age_1 >= 21)
# print(checking_age_1)


# Using 'or' to Check Multiple Conditions
# age_0 = 22
# age_1 = 18

# checking_age_0 = age_0 >= 21 or age_1 >= 21
# print(checking_age_0)

# age_0 = 18
# checking_age_1 = age_0 >= 21 or age_1 >= 21
# print(checking_age_1)


# Checking Whether a Value is Not in a List.
# banned_users = ['andrew', 'carolina', 'david']
# user = 'marie'

# if user not in banned_users:
#     print(f"{user.title()}, you can post a response if you wish.")


# If-else Statement
# age = 17
# if age >= 18:
#     print('You are old enough to vote!')
#     print('Have you registered to vote yet!')

# else:
#     print('Sorry, you are too young to vote.')
#     print('Please register to vote as soon as you turn 18!')


# ## if-elif-else chain

# instruction:
#     Admission for anyone under age 4 is free.
#     Admission for anyone between the ages of 4 and 18 is $25.
#     Admission for anyone age 18 or older is $40.

# age = 12

# if age < 4:
#     print('Your admission cost is $0.')
# elif age < 18:
#     print('Your admission cost is $25')
# else:
#     print('Your admission cost is $40.')


# # Another approach is by setting the price directly to have a simple print.

# age = 12

# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# else:
#     price = 40

# print(f"You admission cost is ${price}.")


# Using Multiple elif Block
# age = 12

# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# elif age < 65:           
#     price = 40
# else:
#     price = 20             # anyone 65 or older will pay 20.

# print(f"Your admission cost is ${price}.")

# --- Note: You can use a final elif block and omit the else block. i.e. not having else block but finalizing in elif.




# Testing Multiple Conditions

# requested_toppings = ['mushrooms', 'extra cheese']

# if 'mushrooms' in requested_toppings:
#     print('Adding mushrooms.')
# if 'pepperoni' in requested_toppings:
#     print('Adding pepperoni')
# if 'extra cheese' in requested_toppings:
#     print('Adding extra cheese.')

# print("\nFinished making your pizza!")    



# Using if Statement with Lists

# Checking for Special Items
# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print('Sorry, we are out of green peppers right now.')
#     else:
#         print(f"Adding {requested_topping}.")

# print("\nFinished making your pizza!")



# Checking That a List is Not Empty

# requested_toppings = []

# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f"Adding {requested_topping}.")
#     print("\nFinished making your pizza!")
# else:
#         print("Are you sure you want a plain pizza?")


# Using Multiple Lists
# available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print(f'Adding {requested_topping}')
#     else:
#         print(f"Sorry, we don't have {requested_topping}.")

# print("\nFinished making your pizza!")






# --- Date: 1/10/2024 ---

# ## Dictionary

# alien_0 = {'color': 'green', 'points': 5}

# print(alien_0['color'])
# print(alien_0['points'])


# alien_0 = {'color': 'green', 'points': 5}

# new_points = alien_0['points']
# print(f"You just earned {new_points} points!")



# # Adding New Key-Value Pairs

# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)

# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)


# # Starting with an Empty Dictionary

# alien_0 = {}

# alien_0['color'] = 'green'
# alien_0['points'] = 5

# print(alien_0)


# # Modifying Values in a Dictionary

# alien_0 = {'color': 'green'}
# print(f"The alien is {alien_0['color']}.")

# alien_0['color'] = 'yellow'
# print(f"The alien is now {alien_0['color']}.")


# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print(f"Original position: {alien_0['x_position']}")

# # Move the alien to the right.
# # Determine how far to move the alien based on its current speed.
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# elif alien_0['speed'] == 'fast':
#     x_increment = 3 
# else:
#     x_increment = 4

# # The new position is the old position plus the increment.
# alien_0['x_position'] = alien_0['x_position'] + x_increment

# print(f"New position: {alien_0['x_position']}")


# # Removing Key-Value Pairs

# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)

# del alien_0['points']          # Be aware that the deleted key-value pair is removed permanently. 
# print(alien_0)


# # A Dictionary of Similar Objects

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }

# language = favorite_languages['sarah'].title()    # To see which language Sarah chose.
# print(f"Sarah's favorite language is {language}")


# # Using get() to Access Values

# problem with retrieving value using key in square
# alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])          # This results in a trackback, showing a keyError


# the get() method to set a default value that will be returned if the requested key doesn’t exist.
# alien_0 = {'color': 'green', 'speed': 'slow'}
# point_value = alien_0.get('points', 'No point value assigned.')
# print(point_value)


# # Looping Through a Dictionary

# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'fermi',
# }

# for key, value in user_0.items():
#     print(f"\nKey: {key}")
#     print(f"Value: {value}")


 
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }

# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")


# # Looping Through All the Keys in a Dictionary

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }

# for name in favorite_languages.keys():
#     print(name.title())

# or

# for name in favorite_languages:     # This code will have exactly the same output, Looping through the keys is actually the default behavior when looping through a dictionary
#     print(name.title()


# favorite_languages = {
#      'jen': 'python',
#      'sarah': 'c',
#      'edward': 'ruby',
#      'phil': 'python',
# }

# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(name.title())

#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}!")


# favorite_languages = {
#      'jen': 'python',
#      'sarah': 'c',
#      'edward': 'ruby',
#      'phil': 'python',
# }

# if 'erin' not in favorite_languages.keys():
#     print("Erin, please take our poll!")


# # Looping Through a Dictionary's Keys in a Particular Order.

# favorite_languages = {
#      'jen': 'python',
#      'sarah': 'c',
#      'edward': 'ruby',
#      'phil': 'python',
# }

# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")



# # Looping Through All Values in a Dictionary

# favorite_languages = {
#      'jen': 'python',
#      'sarah': 'c',
#      'edward': 'ruby',
#      'phil': 'python',
# }

# print("The following languages have been mentioned:")
# for language in favorite_languages.values():
#     print(language.title())


# # set() Method

# favorite_languages = {
#      'jen': 'python',
#      'sarah': 'c',
#      'edward': 'ruby',
#      'phil': 'python',
# }

# print(f"The following languages have been mentioned:")
# for language in set(favorite_languages.values()):
#     print(language.title())

# Note:  # To see each language chosen without repetition, we can use a set. 
#          A set is a collection in which each item must be unique:


# You can build a set directly using braces and separating the elements with commas
# languages = {'python','ruby', 'python', 'c'}
# print(languages)


# # Nesting

# A List of Dictionaries

# alien_0 = {'color': 'green', 'point': 5}
# alien_1 = {'color': 'yellow', 'point': 10}
# alien_2 = {'color': 'red', 'point': 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)


# # Make an empty list for storing aliens.
# aliens = []

# # Make 30 green aliens.
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)

# for alien in aliens[:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'       
#         alien['speed'] = 'medium'       
#         alien['points'] = 10     

#     elif alien['color'] == 'yellow':
#         alien['color'] = 'red'
#         alien['speed'] = 'fast'
#         alien['points'] = 15
  

# # Show the first 5 aliens.
# for alien in aliens[:5]:
#     print(alien)
# print("...")

# # Show how many aliens have been created.
# print(f"Total number of aliens: {len(aliens)}")



# # A List in a Dictionary

# Store information about a pizza being ordered
# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese'],
# }

# # Summarize the order
# print(f"You ordered a {pizza['crust']}-crust pizza " "with the following toppings:")

# for topping in pizza['toppings']:
#     print("\t" + topping)


# favorite_languages = {
#     'jen': ['python', 'ruby'],
#     'sarah': ['c'],
#     'edward': ['ruby', 'go'],
#     'phil': ['python', 'haskell'],
# }


# for name, languages in favorite_languages.items():
#     print(f"\n{name.title()}'s favorite languages are:")
#     for language in languages:
#         print(f"\t{language.title()}")



# A Dictionary in Dictionary
# users = {
#     'aeinstein': {
#         'first': 'albert',
#         'last': 'einstein',
#         'location': 'princeton'
#     },
#     'mcurie': {
#         'first': 'marie',
#         'last': 'curie',
#         'location': 'paris'
#     },
# }

# for username, user_info in users.items():
#     print(f"\nUsername: {username}")
#     full_name = f"{user_info['first']} {user_info['last']}"
#     location = user_info['location']


#     print(f"\tFull name: {full_name.title()}")
#     print(f"\tLocation: {location.title()}")



# ## User Input and While Loops



# # How the input() Function Works

# message = input("Tell me something, and I will repeat it back on you: ")
# print(message)


# # Writing Clear Prompts

# name = input("Please enter your name: ")
# print(f"\nHello, {name}!")

# prompt = "If you tell us who you are, we can personalize the message you see."
# prompt += "\nWhat is your first name? "

# name = input(prompt)
# print(f"\nHello, {name}!")


# # Using int() to Accept Numerical Input

# age = input("How old are you? ")
# print(age)
# age = int(age)
# age_0 = age >= 18
# print(age_0)


# height = input("How tall are you, in inches? ")
# height = int(height)

# if height >= 48:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")



# # The Modulo Operator

# modulo_optr_0 = 4 % 3
# print(modulo_optr_0)

# modulo_optr_1 = 5 % 3
# print(modulo_optr_1)

# modulo_optr_2 = 6 % 3
# print(modulo_optr_2)

# modulo_optr_3 = 7 % 3
# print(modulo_optr_3)


# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number = int(number)

# if number % 2 == 0:
#     print(f"\nThe number {number} is even.")
# else:
#     print(f"\nThe number {number} is odd.")


# ## Introducing While Loops

# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1


# # Letting the User Choose When to Quit
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program."

# message = ""
# while message != 'quit':
#     message = input(prompt)

#     if message != 'quit':
#         print(message)



# # Using a Flag
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program."

# active = True
# while active:
#     message = input(prompt)

#     if message == 'quit':
#         active = False
#     else:
#         print(message)



# # Using break to Exit a Loop
# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.)"

# while True:
#     city = input(prompt)

#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")


# # Using continue in a Loop
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue

#     print(current_number)



# # Avoiding Infinite Loops
# x = 1
# while x <= 5:
#     print(x)
#     x += 1

# # This loop runs forever!
# x = 1
# while x <= 5:
#     print(x)


# # Using a while Loop with Lists and Dictionaries
# # Moving Items from One List to Another

# Start with users that need to be verified, and an empty list to hold confirmed users.

# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []

# # Verify each user until there are no more unconfirmed users.
# # Move each verified user into the list of confirmed users.
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()

#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)


# # Display all confirmed users.
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())


# # Removing All Instances of Specific Vales from a List
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')

# print(pets)



# # Filling a Dictionary with User Input
# responses = {}

# # Set a flag to indicate tht polling is active
# polling_active = True

# while polling_active:
#     # Prompt for the person's name and response.
#     name = input("\nWhat is your name?")
#     response = input("Which mountain would you like to climb someday? ")

#     # Store the response in the dictionary
#     responses[name] = response

#     # Find out if anyone else is going to take the poll.
#     repeat = input("Would you like to let another person respond? (yes/ no) ")
#     if repeat == 'no':
#         polling_active = False

    
# # Polling is complete. Show the results.
# print("\n--- Poll Results ---")
# for name, response in responses.items():
#     print(f"{name} would like to climb {response}.")



# ## Function

# def greet_user():
#     """Display a simple greeting."""
#     print("Hello!")

# greet_user()


# # Passing Information to a Function

# def greet_user(username):
#     print(f"Hello, {username.title()}!")

# greet_user('Jesse')


# # Passing Arguments

# # Positional Arguments
# def describe_pet(animal_type, pet_name):
#     """display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")


# describe_pet('hamster', 'harry')


# # Keywords Arguments

# def describe_pet(animal_type, pet_name):
#     """display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")


# describe_pet(animal_type='hamster', pet_name='harry')
# describe_pet(pet_name='harry', animal_type='hamster')


# # Defualt Value

# def describe_pet(pet_name, animal_type='dog'):
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")


# describe_pet('willie')
# describe_pet(pet_name='harry', animal_type='hamster')


# # Equivalent Function Calls

# A dog named Willie.
# describe_pet('willie')
# describe_pet(pet_name='willie')

# A hamster named Harry
# describe_pet('harry', 'hamster')
# describe_pet(pet_name='harry', animal_type='hamster')
# describe_pet(animal_type='hamster', pet_name='harry')


# # Returning a Simple Value
# def get_formatted_name(first_name, last_name):
#     """ Return a full name, neatly formatted."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# """This might seem like a lot of work to get a neatly formatted name when 
# we could have just written:
# But when you consider working with a large program that needs to 
# store many first and last names separately, functions like get_formatted_name()
# become very useful. You store first and last names separately and then call 
# this function whenever you want to display a full name."""


# # Making an Argument Optional
# def get_formatted_name(first_name, last_name, middle_name=''):
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()

# musician = get_formatted_name('jimi','hendrix')
# print(musician)

# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)


# def build_person(first_name, last_name):
#     person = {'first': first_name, 'last': last_name}
#     return person

# musician = build_person('jimi', 'hendrix')
# print(musician)

# def build_person(first_name, last_name, age=None):
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person

# musician = build_person('jimi', 'hendrix', age=27)
# print(musician)


# # Using a Function with a while loop

# def get_formatted_name(first_name, last_name):
#  """Return a full name, neatly formatted."""
#  full_name = f"{first_name} {last_name}"
#  return full_name.title()

# This is an infinite loop!
# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")

#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
    
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break

#     formatted_name = get_formatted_name(f_name, l_name) 
#     print(f"\nHello, {formatted_name}!")


# Passing a List
# def greet_users(names):
#     """Print a simple greeting to each user in the list."""
#     for name in names:
#         msg = f"Hello, {name.title()}!"
#         print(msg)

# usernames =  ['hannah', 'ty', 'margot']
# greet_users(usernames)


# Modifying a List in a Function

# Start with some designs that need to be printed
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# Simulate printing each design, until none are left.
# Move each design to complete_models after printing
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)

# # Display all completed models.
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)


# def print_models(unprinted_designs, completed_models):
#     """ 
#       Simulate printing each design, until none are left.
#       Move each design to completed_models after printing.  
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)

# def show_completed_models(completed_models):
#     """Show all the models that were printed"""
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)

# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# print_models(unprinted_designs[:], completed_models)
# show_completed_models(completed_models)


# Passing an Arbitrary Number of Arguments
# def make_pizza(*toppings):
#     """The asterisk in the parameter name *toppings tells Python to make an 
#         empty tuple called toppings and pack whatever values it receives into this 
#         tuple."""

#     """Print the list of toppings that have been requested"""

#     """Summarize the pizza we are about to make."""
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')   # no matter how many arguments the function receives, this syntax will work.



# Mixing Positional and Arbitrary Arguments   (args)
# def make_pizza(size,*toppings):
#     print(f"\nMaking a {size}-inch pizza with the following toppings: ")
#     for topping in toppings:
#         print(f"- {topping}")

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# # Using Arbitrary Keyword Arguments  (kwargs)
# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user."""
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info

# user_profile = build_profile('albert', 'einstein', location='prineton', field='physics')
# print(user_profile)



# # Creating the Dog Class
# class Dog:
#     """A simple attempt to model a dog"""

#     def __init__(self, name, age):
#         """Initialize name and age attributes."""
#         self.name = name
#         self.age = age

#     def sit(self):
#         """Simulate a dog sitting in response to a command."""
#         print(f"{self.name} is now sittings.")
    
#     def roll_over(self):
#         """Simulate rolling over in response to a command."""
#         print(f"{self.name} rolled over!")


# my_dog = Dog('Willie', 6)


# print(f"My dog's name is {my_dog.name}")
# print(f"My dog is {my_dog.age} years old.")

# # Calling Methods
# my_dog.sit()
# my_dog.roll_over()


# # Creating Multiple Instances
# class Dog:
#     """A simple attempt to model a dog"""

#     def __init__(self, name, age):
#         """Initialize name and age attributes."""
#         self.name = name
#         self.age = age

#     def sit(self):
#         """Simulate a dog sitting in response to a command."""
#         print(f"{self.name} is now sittings.")
    
#     def roll_over(self):
#         """Simulate rolling over in response to a command."""
#         print(f"{self.name} rolled over!")


# my_dog = Dog('Willie', 6)
# your_dog = Dog('Lucy', 3)

# print(f"My dog's name is {my_dog.name}")
# print(f"My dog is {my_dog.age} years old.")
# my_dog.sit()

# print(f"\nYour dog's name is {your_dog.name}")
# print(f"Your dog is {your_dog.age} year old.")
# your_dog.sit()


# # Working with Classes and Instances
# class Car:
#     """A simple attempt to represent a car."""
#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0   # Setting a Default Value for an Attribute
    
#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()

#     def read_odometer(self):
#         """Print a statement showing the car's mileage."""
#         print(f"This car has {self.odometer_reading} miles on it.")

# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())

# my_new_car.odometer_reading = 23   # Modifying an Attribute’s Value Directly

# my_new_car.read_odometer()


# # Modifying an Attribute’s Value Through a Method
# class Car:
#     """A simple attempt to represent a car."""
    
#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0  # Setting a default value for an attribute

#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()

#     def read_odometer(self):
#         """Print a statement showing the car's mileage."""
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def update_odometer(self, mileage):
#         """
#         Set the odometer reading to the given value.
#         Reject the change if it attempts to roll the odometer back.
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")

#     def increment_odometer(self, miles):
#         """Add the given amount to the odometer reading."""
#         self.odometer_reading += miles


# # Using the Car class
# my_used_car = Car('subaru', 'outback', 2015)
# print(my_used_car.get_descriptive_name())  # Expected: 2015 Subaru Outback

# my_used_car.update_odometer(23_500)  # Set initial mileage
# my_used_car.read_odometer()  # Expected: This car has 23500 miles on it.

# my_used_car.increment_odometer(100)  # Increment mileage
# my_used_car.read_odometer()  # Expected: This car has 23600 miles on it.


# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())  # Expected: 2019 Audi A4

# my_new_car.update_odometer(23)  # Set initial mileage
# my_new_car.read_odometer()  # Expected: This car has 23 miles on it.


# # Inheritance
# class Car:
#     """A simple attempt to represent a car."""
#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0   # Setting a Default Value for an Attribute
    
#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()

#     def read_odometer(self):
#         """Print a statement showing the car's mileage."""
#         print(f"This car has {self.odometer_reading} miles on it.")

# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())

# my_new_car.odometer_reading = 23   # Modifying an Attribute’s Value Directly

# my_new_car.read_odometer()


# # Modifying an Attribute’s Value Through a Method
# class Car:
#     """A simple attempt to represent a car."""
    
#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0  # Setting a default value for an attribute

#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()

#     def read_odometer(self):
#         """Print a statement showing the car's mileage."""
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def update_odometer(self, mileage):
#         """
#         Set the odometer reading to the given value.
#         Reject the change if it attempts to roll the odometer back.
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")

#     def increment_odometer(self, miles):
#         """Add the given amount to the odometer reading."""
#         self.odometer_reading += miles


# class Battery:
#     """A simple attempt to model a battery for an electric car."""

#     def __init__(self, battery_size=75):
#         """Initialize the battery's attributes."""
#         self.battery_size = battery_size

#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print(f"This car has a {self.battery_size}-kWh battery.")

#     def get_range(self):
#         """Print a statement about the range this battery provides."""
#         if self.battery_size == 75:
#             range = 260
#         elif self.battery_size == 100:
#             range = 315

#         print(f"This car can go about {range} miles on a full charge.")

# class ElectricCar(Car):
#     """Represent aspects of a car, specific to an electric vehicles."""

#     def __init__(self, make, model, year):
#         """Initialize attributes of the parent class."""
#         super().__init__(make, model, year)
#         self.battery = Battery()


#     # Overriding Methods from the Parent Class
#     def fill_gas_tank(self):
#         """Electric cars don't have gas tanks."""
#         print("This car doesn't need a gas tank!")


# my_tesla = ElectricCar('tesla', 'model s', 2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()

# # Using the Car class
# # my_used_car = Car('subaru', 'outback', 2015)
# # print(my_used_car.get_descriptive_name())  # Expected: 2015 Subaru Outback

# # my_used_car.update_odometer(23_500)  # Set initial mileage
# # my_used_car.read_odometer()  # Expected: This car has 23500 miles on it.

# # my_used_car.increment_odometer(100)  # Increment mileage
# # my_used_car.read_odometer()  # Expected: This car has 23600 miles on it.


# # my_new_car = Car('audi', 'a4', 2019)
# # print(my_new_car.get_descriptive_name())  # Expected: 2019 Audi A4

# # my_new_car.update_odometer(23)  # Set initial mileage
# # my_new_car.read_odometer()  # Expected: This car has 23 miles on it.



<<<<<<< HEAD
=======
    
>>>>>>> 0ab4417 (hash table folder added.)
