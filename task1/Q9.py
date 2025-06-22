# 9. Given a list of integers,
#    write a function to return a new list containing only the prime numbers from the original list.

def is_prime(n):
    if n<=1 :
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 :
            return False
    return True

li = [1,3,4,6,5,8,9,19,37,121,127]
prime_list = [n for n in li if is_prime(n)]
print(prime_list)