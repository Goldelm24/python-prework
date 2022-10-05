#Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

import numbers


def hello_name(user_name):
    print("Hello, "+ user_name.title() + "!")
user_name = input("Enter USERNAME: ")
hello_name(user_name)

#Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    
    for i in range(1,101):
        if i % 2 == 1:
         print(i)
first_odds()

#Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    max_num = max(a_list)
    return max_num

num = [2, 4, 6, 8, 10]
print(max_num_in_list(num))

#Question 4 
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    leap = False
    if (a_year % 4 == 0) and (a_year % 100 != 0):
        leap = True
    elif (a_year % 100 == 0) and (a_year % 400 != 0):
        leap = False 
    elif (a_year % 400 == 0):
        leap = True
    else:
        leap = False
    return leap
print(is_leap_year(int(input("Enter a year: "))))

#Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
   """ Are all the numbers consecutive?  """
   return sorted(a_list) == list(range(min(a_list), max(a_list)+1))

numlist = [1, 2, 3, 4, 5]
numlist2 = [3, 9, 8, 12, 7]
numlist3 = [10, 1, 56, 25, 98]

print(is_consecutive(numlist))
print(is_consecutive(numlist2))
print(is_consecutive(numlist3))