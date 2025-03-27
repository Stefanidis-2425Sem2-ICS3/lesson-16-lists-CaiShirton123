# Name: Cai  
# Title: List of Numbers Averaged
# Date: March 27, 2025
# Description: Write a program that creates a list of 100 random numbers between 0 and 100. It should print out the numbers. Then your program should find the average of the 100 numbers. 

import random
#Program
# Create a list of 100 random numbers between 0 and 100
random_numbers = [random.randint(0, 100) for _ in range(100)]

# Print the list of random numbers
print("List of 100 random numbers:")
print(random_numbers)

# Calculate the average of the numbers
average = sum(random_numbers) / len(random_numbers)

print("\nAverage of the 100 random numbers:", average)