numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in numbers:
    for j in range(2,i):
        is_prime = bool(i % j)
        if is_prime == False:
            not_primes.append(i)
            break
    if i == 1:
        continue
    elif is_prime:
        primes.append(i)
print('Primes',primes)
print('Not_Prames',not_primes)