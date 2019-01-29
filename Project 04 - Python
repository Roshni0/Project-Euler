def isPalindrome(number):
    number_str = str(number)
    index_b = 0
    index_e = len(number_str)-1
    max_index = len(number_str) / 2 
   
    while index_b < max_index:
        if int(number_str[index_b]) != int(number_str[index_e]):
            return 0
        index_b += 1
        index_e -= 1
    return 1

def three_digit_product():
    biggest_product = 0

    for first in range(100,1000):
        for second in range(100,1000):
            temp = first*second
            if temp > biggest_product and isPalindrome(temp):
                biggest_product = temp
    return biggest_product

print three_digit_product()
