# # Write a multi-line comment with your name, favorite food, and dream job on 3 different lines.
'''
My name is Blake,
my favorite food is pasta,
and my dream job is NBA player
'''
# assign 5 different data types to 5 different variables. At least one datatype must be a string.
a = "Dog"
b = int(15)
c = float(1.432)
d = True
e = [1,2,3,4,5]
# print the length of your string.
print(len(a))


# # create a new variable called savvy, and assign it the string with this phrase "Learning Data Analytics and Python is Awesome!"
# savvy = "Learning Data Analytics and Python is Awesome!"

# # return a range of characters that slices the above string from the beginning of "ing" up to before "and"
# print(savvy[5:23])

# # Replace "Awesome" with "great" in the string
# new_savvy = savvy.replace("Awesome", "great")
# print(new_savvy)
# # Test and print the savvy string to see it contains "Python"
# print(savvy)




# # Create and assign 3 more variables called name, age and length using the multi-variable naming method.
# name, age, length = "Blake", 34, 6

# # Format a new string called 'miniBio' using variables in curly brackets to complete this phrase... "Hi my name is (name), I am (tall) and (so) old today."
# print(f"Hi my name is {name}, I am {length} feet tall, and {age} years old.")
# # print 'miniBio'
# # cast and print the age variable to a float.
# print(float(age))

# Create a list of at least 5 elements of mixed data types
# replace a part of it with something else
# append or insert several more items to the list
# find and print the length of the list
# slice a sub-section of the 1st list, and save it to a different 2nd list
# print the 2nd list
# extend your original list with the 2nd list sliced above
# Create a new list called "simList" containing at least 5 elements of the same data type, either string, integer, float, or Boolean.
# sort "simList", and print the list
# copy the "simList" list to another 3rd list
# add the 2nd and 3rd lists together into a 4th list


my_list = ["basketball", "football", "baseball", "soccer", "tennis"]
my_list[2] = "pickleball"
my_list.append("hockey")
print(my_list)


# print(len(my_list))

middle_index = 3
first_list = my_list[:middle_index]
print(first_list)
second_list = my_list[middle_index:]
print(second_list)
new_list = first_list + second_list
print(new_list)


simList = [4,3,15,5]
simList.sort()
print(simList)
simList3 = simList.copy()
final_list = simList + simList3
print(final_list)