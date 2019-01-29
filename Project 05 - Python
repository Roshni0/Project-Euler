import time

smallest_number = 2520

number_list = range(1,21)

def smallest_number_divisible(number):
    for counter in number_list:
        if number % counter:
            return 0       
    return number

num = smallest_number_divisible(smallest_number)

s = time.time()
while not num:
    smallest_number +=20
    num = smallest_number_divisible(smallest_number)
print 'TIME : ',time.time() - s,' seconds' #this prints the time it took to run the program
print smallest_number
