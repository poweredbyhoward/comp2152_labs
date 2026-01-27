# Question 4 ----------------------------------------------
# Sets are unordered, unchangeable*, and unindexed.
# *Items can be added or removed BUT not altered
monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}

monday_class.add("Grace")
# re-running the script will have a different order to the list because this is a set!
print(f'Monday class: {monday_class}')
print(f'Wednesday class: {wednesday_class}')

# find the intersection of multiple sets using &
intersection_of_classes = monday_class & wednesday_class
print(f'Attended both classes: {intersection_of_classes}')

# find the union of multiple sets using |
all_classes = monday_class | wednesday_class
print(f'Attended either class: {all_classes}')

# Return a set containing the difference between multiple sets using -
# difference()
only_monday = monday_class - wednesday_class
print(f'Only Monday: {only_monday}')

# Return a set containing using exclusive-or, XOR, using ^
only_one = monday_class ^ wednesday_class
print(f'Only one class (not both: {only_one}')

# Return a boolean checking if a set is a subset of another set
print(f'Is Monday a subset of all students? {monday_class <= all_classes}')