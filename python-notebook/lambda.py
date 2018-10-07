def square(num):
    return num**2

nums = [x for x in range(10)]

result = list(map(square,nums))

#COERCE to FLOAT
#print(3.6 + 5.4)

def splicer(string):
    if len(string) %  2 == 0:
        return 'EVEN'
    else:
        return string

words = ['Tee', 'ERZA', 'Crystal']

result = list(map(splicer,words))

result = list(map(lambda x:x[::-1], words))
result = list(map(lambda num:num ** 2, nums))

print(result)
