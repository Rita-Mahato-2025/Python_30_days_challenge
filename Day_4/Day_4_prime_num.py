#Check if a user entered number is prime.
n = int(input("Enter a number:"))
is_prime = True

for i in range(2, n):
    if n%i == 0:
        is_prime = False

if is_prime and n>1:
    print(f"{n} is a prime number.")
else:
        print(f"{n} is a not prime number.")