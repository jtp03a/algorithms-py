# Big O is a method for comparing code mathmathically about how efficient they run
# time complexity - measure how long it takes code to run, measured in the number of operations that it takes to complete
# space complexity - preserving memory space

# 3 greek letters 
# Omega - Best case scenario for running some code 
# Theta - Average case
# Omicron - Worse case

# List iteration - build for loop to iterate and find a number
# [1, 2, 3, 4, 5, 6, 7] - 1 is best case, 7 is worst case, 4 is avg case

# Big O is the worst case

# Big O is graphed on time as the x axis and number of operations as the y axis

# example of O(n) - n was the number of operations

# def print_items(n):
#     for i in range(n):
#         print(i)

# print_items(10)

# Drop constants - this ran n+n times, could be 0(2n) but we can simplify by dropping constantants, still wright 0(n)

# def print_items2(n):
#     for i in range(n):
#         print(i)

#     for j in range(n):
#         print(j)

# print_items2(10)

# O(n^2) - below would be O(n^3) but simplify as O(n^2), doesnt matter if its to the 3, 4, 5, 6 etc. - its is alot less efficient from a time complexity standpoint, if you graph the line of O(n^2) it is much steeper 

# def print_items(n):
#     for i in range(n):
#         for j in range(n):
#             for k in range(n):
#                 print(i, j, k)

# print_items(10)

# Drop Non-Dominants - nested for loop ran O(n^2) times, single for lop ran O(n) times - so total number of items was O(n^2 + n), but we are concerned in big O with what happens when n gets very large, the plus n is insignificant compared to total operations so n^2 is the dominate and we drop the non dominate

# def print_items(n):
#     for i in range(n):
#         for j in range(n):
#             print(i, j)

#     for k in range(n):
#         print(k)

# print_items(10)

# O(1) - in this case the number of operations does not increase no matter how big n gets, even if we have 3 operations (n + n + n) we are stil going to call it O(1) (also called constant time) as n increases the number of operations remains constant. on the graph O(1) is a flat line across bottom, the most efficient big O

# def add_items(n):
#     return n + n

# O (logn) log2 8 = 3, 2^3 = 8, 2 to the what power = 8, if you have very large lists, i.e. a list of a billion items and you iterate through it linearily you will have 10 billion operations, but if you do process of iterating through it by cutting it in half, you will have many less operations
#  the graph of this is very flat and efficient.
# O(nlog n ) is the most efficient you can make a sorting algorithm that sorts different types of data i.e. strings

# Different Terms for Inputs - inclination in the below is to say that this is O(n) + O(n) = O(2n) = O(n), but when a function has different parameters, you cant say that O(a) = O(b), so you get O(a) + O(b) -> O(a + b)

# def print_items(a, b):
#     for i in range(a):


#     for k in range(b):
#         print(k)

# O(a * b)

# def print_items(a, b):
#     for i in range(a):
#         for k in range(b):
#             print(i, k)

# Lists - [11, 3, 23, 7]
          # 0, 1,  2, 3
# my_list.append(17) - simple operations because no reindexing occurs
# my_list.pop() - still simple, no reindexing
#  these are O(1)

# my_list.pop(0) - reindexing occurs for every item in the list , same issue for my_list.insert(0,11) - O(n) with n being the number of items in the list
# my_list.insert(1, 'Hi') - insert in the middle, O(n), still  O(n) because 1) drop constants, 2) Big O measures worst case (every item has to be reindexed)
# looking for items in list - if we are going to iterate through a list until we ge the item we are looking for its O(n) (worse case the item is in the very last position)
# if you look for an item based on the index its O(1) (only 1 operation, you go straight there)

# n = 100
# O(1) = 1, O(logn) = 7, O(n) = 100, O(n^2) = 10000

# as n grows the gap grows in efficiency  

# O(n^2) - Loop within a Loop
# O(n) - proportional
# O(log n ) - divide and conquer
# O(1) - constant time

# https://www.bigocheatsheet.com/








