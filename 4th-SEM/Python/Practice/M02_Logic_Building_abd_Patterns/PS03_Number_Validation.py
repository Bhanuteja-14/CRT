'''
1) write a python code for the factorial of a number?

n = int(input("enter n"))
fact = 1
for i in range(1, n+1):
    fact = fact * i
print(fact)

2) write a python code to check whether the given number is Armstrong or not?
ex: 153 = 1^3 + 5^3 + 3^3
n = int(input("enter n"))
temp = n
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if sum == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
'''
'''
3) write a python code to check whether the given number is prime or not?

n = int(input("enter n: "))
if n > 1:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
'''
'''
4) print the prime numbers in a given range?
lower = int(input("Enter lower bound: "))
upper = int(input("Enter upper bound: "))
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)
'''
'''5)reverse of number
n = int(input("enter n: "))
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10
print("Reverse of the number is:", reverse)
'''
'''
6  ''' 