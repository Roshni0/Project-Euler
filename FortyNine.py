from math import sqrt

def prime_checker(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, int(sqrt(num))+1):
            if num % i == 0:
                return False
        return True

def check_if_permutation(str1, str2):
    str1 = sorted(str1)
    str2 = sorted(str2)
    if str1 == str2:
        return True
    return False



def prime_permutations():
    nums = []
    for i in range(1000,3340):
        if prime_checker(i) and prime_checker(i+3330) and prime_checker(i+6660):
            nums.append(i)
    
    for k in nums:
        if (check_if_permutation(str(k), str(k+3330))) and (check_if_permutation(str(k), str(k+6660))):
            if k != 1487:
                print(str(k) + str(k+3330) + str(k+6660))
                break

prime_permutations()