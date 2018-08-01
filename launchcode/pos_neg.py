def pos_or_neg(num):
    if num > 0:
        print('positive')
    elif num < 0:
        print('negative')
    else:
        print('nothing')

pos_or_neg(24)
pos_or_neg(-24)
pos_or_neg(0)

def print_positives(the_ints):
    for num in the_ints:
        if num > 0:
            print(num)

from random import randint

my_numbers = [randint(-10,20) for x in range(10)]
print(my_numbers)
print_positives(my_numbers)

def print_signed_integers(the_ints, the_sign):

    if the_sign == 'positive':
        for i in the_ints:
            if i > 0:
                print(i)
    elif the_sign == 'negative':
        for i in the_ints:
            if i < 0:
                print(i)

numbers_list = [-1,2,3,-4,5,6,-7,8,9,-10, 0]
print_signed_integers(numbers_list, 'positive')
print_signed_integers(numbers_list, 'negative')
