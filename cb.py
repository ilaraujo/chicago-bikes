import csv
import matplotlib.pyplot as plt

# Reading CSV
print('Reading the document...')
with open('files/chicago.csv') as chicago_file:
    reader = csv.reader(chicago_file)
    data_list = list(reader)
print('Done!')

# How many rows
print('The number of rows in the CSV file is ' + str(len(data_list)))

# Printing the first rows (head)
print('\nThe first row is: ')
print(data_list[0])

# Printing the second row (real data)
print('\nThe second row is: ')
print(data_list[1])

input('Press Enter to continue...')

# TASK 1
# TODO: Print the first 20 rows using a loop to identify the data.
print("\n\nTASK 1: Printing the first 20 samples")

# Remove header
data_list = data_list[1:]

i = 0
while i <= 20:
    print(data_list[i])
    i += 1

input("Press Enter to continue...")

# TASK 2
# TODO: Print the `gender` of the first 20 rows

print("\nTASK 2: Printing the genders of the first 20 samples")

i = 0
while i <= 20:
    if data_list[i][6]:
        print(data_list[i][6])
    else:
        print('Not declared')
    i += 1

input("Press Enter to continue...")

# TASK 3
# TODO: Create a function to add the columns(features) of a list in another list in the same order
def column_to_list(data, index):
    """
     Add the columns of a list in another list in the same order.
     Args:
         data: The entire list with all the data.
         index: Index of a certain item.
     Returns:
         List of items in a column.
     """
    column_list = []

    for item in data:
        column_list.append(item[index])

    return column_list

# Let's check with the genders if it's working (only the first 20)
print("\nTASK 3: Printing the list of genders of the first 20 samples")
print(column_to_list(data_list, -2)[:20])


# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(column_to_list(data_list, -2)) is list, "TASK 3: Wrong type returned. It should return a list."
assert len(column_to_list(data_list, -2)) == 1551505, "TASK 3: Wrong lenght returned."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TASK 3: The list doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we know how to access the features, let's count how many Males and Females the dataset have
# TASK 4
# TODO: Count each gender. You should not use a function to do that.
male = 0
female = 0

for line in data_list:
    if line[6] == 'Male':
        male += 1
    if line[6] == 'Female':
        female += 1

# Checking the result
print("\nTASK 4: Printing how many males and females we found")
print("Male: ", male, "\nFemale: ", female)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert male == 935854 and female == 298784, "TASK 4: Count doesn't match."
# -----------------------------------------------------


input("Press Enter to continue...")
# Why don't we creeate a function to do that?
# TASK 5
# TODO: Create a function to count the genders. Return a list
# Should return a list with [count_male, counf_female] (e.g., [10, 15] means 10 Males, 15 Females)
def count_gender(data_list):
    """
     Count how many Males and Females a list has.
     Args:
         data_list: The entire list with all the data.
     Returns:
         Number of men and women in the format [male, female]
     """
    male = 0
    female = 0

    for line in data_list:
        if line[6] == 'Male':
            male += 1
        if line[6] == 'Female':
            female += 1

    return [male, female]

print("\nTASK 5: Printing result of count_gender")
print(count_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(count_gender(data_list)) is list, "TASK 5: Wrong type returned. It should return a list."
assert len(count_gender(data_list)) == 2, "TASK 5: Wrong lenght returned."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TASK 5: Returning wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we can count the users, which gender use it the most?
# TASK 6
# TODO: Create a function to get the most popular gender and print the gender as string.
# We expect to see "Male", "Female" or "Equal" as answer.
def most_popular_gender(data_list):
    """
     Check which genre is most popular.
     Args:
         data_list: The entire list with all the data.
     Returns:
         The most popular gender.
     """
    male = 0
    female = 0
    not_declared = 0

    # Count the number of Male of Females
    for line in data_list:
        if line[6] == 'Male':
            male += 1
        elif line[6] == 'Female':
            female += 1
        else:
            not_declared += 1

    # Check the most popular gender
    if male > female:
        answer = "Male"
    elif male < female:
        answer = "Female"
    elif male == female:
        answer = "Equal"

    return answer


print("\nTASK 6: Which one is the most popular gender?")
print("Most popular gender is: ", most_popular_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(most_popular_gender(data_list)) is str, "TASK 6: Wrong type returned. It should return a string."
assert most_popular_gender(data_list) == "Male", "TASK 6: Returning wrong result!"
# -----------------------------------------------------

# If it's everything running as expected, check this graph!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('Gender')
plt.xticks(y_pos, types)
plt.title('Quantity by Gender')
plt.show(block=True)


input("Press Enter to continue...")
# TASK 7
# TODO: Plot a similar graph for user_types. Make sure the legend is correct.
print("\nTASK 7: Check the chart!")

# Counter for user_types
def count_user_type(data_list):
    """
     Count the types of users in a list
     Args:
         data_list: The entire list with all the data.
     Returns:
         The number of users for each type.
     """
    dependent = 0
    subscriber = 0
    customer = 0

    for line in data_list:
        if line[5] == "Dependent":
            dependent += 1
        if line[5] == "Subscriber":
            subscriber += 1
        if line[5] == "Customer":
            customer += 1

    return [dependent, subscriber, customer]

user_types = column_to_list(data_list, -3)
types = ['Dependent', 'Subscriber', 'Customer']
quantity = count_user_type(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('Gender')
plt.xticks(y_pos, types)
plt.title('Quantity by User Type')
plt.show(block=True)

input("Press Enter to continue...")
# TASK 8
# TODO: Answer the following question
male, female = count_gender(data_list)
print("\nTASK 8: Why the following condition is False?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Because there are some empty records in line[6] as predicted in the function most_popular_gender()."
print("Answer:", answer)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert answer != "Because there are some empty records in line[6] as predicted in the function most_popular_gender(). diff", "TASK 8: Write your own answer!"
# -----------------------------------------------------

input("Press Enter to continue...")

# Let's work with the trip_duration now. We cant get some values from it.
# TASK 9
# TODO: Find the Minimum, Maximum, Mean and Median trip duration.
# You should not use ready functions to do that, like max() or min().
trip_duration_list = column_to_list(data_list, 2)

# Calculating min_trip and max_trip
int_values = [ int(x) for x in trip_duration_list ]
int_values.sort()

min_trip = int_values[0]
max_trip = int_values[-1]

# Calculating mean_trip
def sum_all(data):
    """
     Sum all integers in a column of a list.
     Args:
         data: List of integers.
     Returns:
         The sum of all integers in a list.
     """
    sum = 0
    for x in data:
        sum += x
    return sum

def list_length(data):
    """
     The number of lines in a column or entire list.
     Args:
         data: A list.
     Returns:
         Number of lines in a column or a list.
     """
    length = 0
    for item in data:
        length += 1

    return length

mean_trip = round(sum_all(int_values)/list_length(int_values))

# Calculating median_trip
def median(data):
    """
     Calculates the median of a list of integers.
     Args:
         data: List of integers.
     Returns:
         The median of a list of integers.
     """
    l = list_length(data)

    if l < 1:
        return None
    elif l % 2 == 1:
        return sorted(data)[l//2]
    else:
        return sum_all(sorted(data)[l//2-1:l//2+1])/2

median_trip = median(int_values)

print("\nTASK 9: Printing the min, max, mean and median")
print("Min: ", min_trip, "Max: ", max_trip, "Mean: ", mean_trip, "Median: ", median_trip)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert round(min_trip) == 60, "TASK 9: min_trip with wrong result!"
assert round(max_trip) == 86338, "TASK 9: max_trip with wrong result!"
assert round(mean_trip) == 940, "TASK 9: mean_trip with wrong result!"
assert round(median_trip) == 670, "TASK 9: median_trip with wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")


# TASK 10
# Gender is easy because usually only have a few options. How about start_stations? How many options does it have?
# TODO: Check types how many start_stations do we have using set()
user_types = list(set(column_to_list(data_list, 3)))

print("\nTASK 10: Printing start stations:")
print(len(user_types))
print(user_types)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert len(user_types) == 582, "TASK 10: Wrong len of start stations."
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 11
# Go back and make sure you documented your functions. Explain the input, output and what it do. Example:
# def new_function(param1: int, param2: str) -> list:
#     """
#      Example function with annotations.
#      Args:
#          param1: The first parameter.
#          param2: The second parameter.
#      Returns:
#          List of X values
#
#      """
input("Press Enter to continue...")

# TASK 12 - Challenge! (Optional)
# TODO: Create a function to count user types without hardcoding the types
# so we can use this function with a different kind of data.
print("Will you face it?")
answer = "yes"
def count_items(column_list):
    """
     Count types of data with undefined number of types.
     Args:
         column_list: The entire column values.
     Returns:
         Item types and how many items for each type.
     """
    item_types = []
    count_items = []

    group = list(set(column_list))

    for item_type in group:
        item_types.append(item_type)

    for item in item_types:
        occur = column_list.count(item)
        count_items.append(occur)

    return item_types, count_items

count_items(column_to_list(data_list, -2))
if answer == "yes":
    # ------------ DO NOT CHANGE ANY CODE HERE ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTASK 11: Printing results for count_items()")
    print("Types:", types, "Counts:", counts)
    assert len(types) == 3, "TASK 11: There are 3 types of gender!"
    assert sum(counts) == 1551505, "TASK 11: Returning wrong result!"
    # -----------------------------------------------------
