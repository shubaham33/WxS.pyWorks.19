''' 
A program that prompts the user for two integers and then prints: 
• The sum
• The difference
• The product
• The average
• The distance (absolute value of the difference) 
• The maximum (the larger of the two)
• The minimum (the smaller of the two)
'''
num_A = int(input('Enter first number: '))
num_B = int(input('Enter second number: '))

print(f"Sum of {num_A} and {num_B} is {num_A + num_B}")
print(f"Diff of {num_A} and {num_B} is {num_A - num_B}")
print(f"Product of {num_A} and {num_B} is {num_A * num_B}")
print(f"Avg of {num_A} and {num_B} is {(num_A + num_B) / 2}")
print(f"Distance between {num_A} and {num_B} is {abs(num_A - num_B)}")
print(f"Maximum of {num_A} and {num_B} is {max(num_A , num_B)}")
print(f"Minimum of {num_A} and {num_B} is {min(num_A , num_B)}")
