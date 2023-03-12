PI = 3.14159
age = 30
print(PI)
print("--------------------------------------")

math_operation = 1 + 3 * 4 / 2 - 2
print(math_operation)

float_division = 12 / 2
print(math_operation)

decimal_division = 13 // 5  # gives the whole part of the division
print(decimal_division)

remainder = 13 % 5
print(remainder)
print("--------------------------------------")

# Check if number is add or even

# x = input("print input number to check if it is odd or even: ")
x = 34
remainder = int(x) % 2
if remainder == 0:
    print("Even number")
else:
    print("Odd number")

print("-------------# Strings------------------")

# Strings
my_string = "Hello, World!"
string_with_quotes1 = 'He sad "You are amassing" yesterday!'
string_with_quotes2 = "He sad \"You are amassing\" yesterday!"  # \ before char is escaping
print(string_with_quotes1)
print(string_with_quotes2)
print("--------------------------------------")

multiline_string = """Hello, world.

My name is Arsen. Welcome, here is my program.
"""  # multiline string defines with """ (3 quotes), multiline comments are use case
print(multiline_string)

name = "Jose"
greeting = "Hello " + name
print(greeting)

print("------------# String formatting--------------")

# String formatting
# comment usually use fstring instead string.format

age = 34
age_as_str = str(age)
print("You are " + age_as_str)
print(f"You are {age}")

name = "Jose"
greeting = f"Hello {name}"
print(greeting)
# if we change name var and print greatting again name will not change
name = "Arsen"
print(greeting)
# Another way to do string formatting

sec_name = "John"
final_greeting = "How are you, {}?"
john_name_greeting = final_greeting.format(sec_name)  # takes sec_name and replace {} with sec_name value
print(john_name_greeting)

sec_name = "Bob"
bob_name_greeting = final_greeting.format(sec_name)  # takes sec_name and replace {} with sec_name value
print(bob_name_greeting)

sec_name = "Hakob"
__final_greeting = "How are you {sec_name}?"
jose_greeting = __final_greeting.format(sec_name="Jose")
# or
# jose_greeting = __final_greeting.format(sec_name=sec_name)
print(jose_greeting)

print("-------------# User Input--------------")

# User Input

my_name = "Arsen"
# your_name = input("Enter your name: ")
# print(f"Hello {your_name}. my name is {my_name}")
# age = int(input("Enter your age:"))
# print(f"You have lived for {age * 12} months.")

print("-------------# Boolean values ---------------")

# Boolean values

age = 20
is_over_age = age > 18
print(is_over_age)

my_number = 5
# user_number = int(input("Guess the number: "))
user_number = 8
print(my_number == user_number)

print("--------------------------------------")

# AND and OR

# age = int(input("Enter your age: "))
exp = 12
can_learn_programming = age > 0 and age < 150
print(f"You can learn programming: {can_learn_programming}")

# exp = int(input(f"Enter your experience: for checking Mid lvl: "))
exp = 12
is_mid_lvl = (exp > 2 and exp < 5) or exp == 4
print(f"You are matching for mid lvl: {is_mid_lvl}")

print(bool(5))  # Evaluate True
print(bool(0))  # Evaluate False
print(bool(""))  # Evaluate False
print(not -35)  # Evaluate False

print("--------------# List in Python --------------")

# List [] in Python

friend = ["Rolf", "Bob", "Anne"]
friend_age = [["Anna", 24], ["Bob", 35], ["Jack", 32]]

print(friend[0])
print(friend)
print(len(friend))
print(friend_age[0][1])

friend.append("Arsen")
print(friend)
friend.remove(friend[0])
print(friend)
friend_age.append(["Dave", 22])
print(friend_age)

print("-------------# Tuples ----------------")

# Tuples (): # Need more investigation use cases amd build in functions

short_tuple = "Rolf", "Bob"
a_bit_clearer_tuple = ("Rolf", "Bob", "Anne")
print(a_bit_clearer_tuple)

print("-------------# Sets ----------------")

# Sets: Don't contain duplicate elements, don't ordered

art_friends = {"Rolf", "Anne"}
science_friends = {"Jen", "Charlie"}

art_friends.add("Jen")
print(art_friends)
art_friends.remove("Anne")
print(art_friends)

print("-----------# Advanced Sets Functions------------------")

art_friends = {"Rolf", "Anne", "Jen"}
science_friends = {"Jen", "Charlie"}

art_but_not_science = art_friends.difference(science_friends)  # Items are in art and not in science
science_but_not_art = science_friends.difference(art_friends)  # Items are in science not in art
print(art_but_not_science)
print(science_but_not_art)

not_in_both = art_friends.symmetric_difference(science_friends)  # Items that are not in both sets
print(not_in_both)

art_and_science = art_friends.intersection(science_friends)  # Items which is common or both
print(art_and_science)

all_friends = art_friends.union(science_friends)  # Unite both sets
print(all_friends)

print("----------- # Dictionaries ---------------")

# Dictionaries: {"Key": val}, can't have duplicates, keep items order unlike sets

friend_age = {"Rolf": 24, "Anne": 27, "Adam": 30}
print(friend_age)
print(friend_age["Rolf"])

friend_age["Bob"] = 20
friend_age["Rolf"] = 25
print(friend_age)

friends = (  # Tuples of dictionaries
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},)

print(friends[0]["name"])
print(friends[1]["name"])
print(friends[2]["name"])

friends = {"Rolf": 24, "Anne": 27, "Adam": 30}
friend_ages = dict(friends)
print(friend_ages)

print("----------- # Length and sum ---------------")

# Length and sum

grades = [80, 75, 90, 100]
total = sum(grades)
length = len(grades)
print(f"total = {total} length = {length}")

average = total / length
print(average)

print("----------- # Joining List ---------------")

friend = ["Rolf", "Anne", "Charlie"]
print(f"My friends are {friends}")
comma_separated = ", ".join(friends)
print(f"My friends are {comma_separated}")



