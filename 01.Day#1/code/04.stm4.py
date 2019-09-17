''' 
A program that reads a number between 1,000 and 999,999 from the user 
and prints it with a comma separating the thousands
'''
num = input('Enter the number between 1000 and 999,999: ')
# Using string slicing
print(num[:-3] + ',' + num[-3:])
