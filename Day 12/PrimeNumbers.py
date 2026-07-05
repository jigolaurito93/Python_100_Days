def is_prime_number(num):
    if num == 2:
        return True
    if num == 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


print(is_prime_number(121))
print(is_prime_number(97))
print(is_prime_number(117))
print(is_prime_number(147))