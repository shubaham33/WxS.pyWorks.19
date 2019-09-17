''' 
Simulate a postage stamp vending machine
'''

# It is always a better choice to define CONSTANT variable instead of using a magic number
FIRST_CLASS_POSTAGE_STAMP = 44
PENNIES_IN_A_DOLLAR = 100

dollars = int(input('Enter amount in dollars'))

first_class_stamps = PENNIES_IN_A_DOLLAR * dollars // FIRST_CLASS_POSTAGE_STAMP
single_penny_stamps = PENNIES_IN_A_DOLLAR * dollars - \
    first_class_stamps * FIRST_CLASS_POSTAGE_STAMP

print('First class stamps: %d\nPenny stamps: %d' %
      (first_class_stamps, single_penny_stamps))
