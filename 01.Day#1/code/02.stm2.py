''' 
A program that reads a number and displays the square, cube, and fourth power
'''
num = int(input('Enter the number: '))

# Using %s format
print("Square of %d is %d" % (num, num * num))

# Using str format()
print("Cube of {} is {}".format(num, num ** 3))

# Using str format()
print("Cube of {} is {}".format(num, num ** 3))

# Using f - string
print(f"Fourth power of {num} is {num**4}")
