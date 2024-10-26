numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for num in numbers:
    if num < 2:
        not_primes.append(num)
        continue

    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)
not_primes.remove(1)

print(f'Простые числа: {primes}')
print(f'Непростые числа: {not_primes}')
