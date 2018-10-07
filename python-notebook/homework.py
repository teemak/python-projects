import math
import string
import random


#V = (4/3) * pi * r**3
def vol(radius):
    return (4/3) * math.pi * radius**3

result = vol(4)



def check_range(num,low,high):
    if num in range(low,high + 1):
        return True
    else:
        return False

random_number = random.randint(1,100)
random_min = random.randint(1,100)
random_max = random.randint(100,1000)

result = check_range(random_number,random_min,random_max)

##str = 'The number is: {random_number} and the range is {random_min} to {random_max}: {result}'
##str = 'Hello Mr. Rogers, how are you this fine Tuesday?'

def up_low(str):
    lowercase = 0
    uppercase = 0

    for letter in str:
        ascii = ord(letter)
        if ascii < 123 and ascii > 96:
            lowercase += 1
        elif ascii > 64 and ascii < 91:
            uppercase += 1

    print(f'The uppercase letters are {uppercase}')
    print(f'The lowercase letters are {lowercase}')
    print(len(str))

#up_low(str)

numbers_list = [1,1,2,2,2,3,3,3,8,9,8,9,1,4,5,6,7]

#print(list(set(numbers_list)))

sample_list = [1,2,3,-4]

def mult(numbers):
    result = 1
    for x in numbers:
        result *= x
    return result

#print(mult(sample_list))

word = 'racecar'

def palindrome(word):
    print(f'word {word} and last {word[::-1]}')
    #compares abcde == edcba
    #word[::-1] = whole word backwards
    return word == word[::-1]
    #last = len(word)
    #count = -1
    #for i in range(last):
    #    print(f'first: {word[i]} -- last: {word[last + count]}')
    #    if word[i] == word[last + count]:
    #        count -= 1
    #    else:
    #        return False
    #return True

#print(palindrome(word))


