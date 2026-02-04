
#Docstring for 4th-SEM.Python.Practice.M02_Logic_Building_abd_Patterns.PS02_Number_Series
#1.print n natural no.
n = int(input())
for i in range(n):
    print(i)
#2. even numbers:
for i in range(2,n+1,2):
    print(i)
#3. print odd no:
for i in range(1,n+1,2):
    print(i)
#4.Fibonacci no.
a,b =0,1
for i in range(n):
    print(a)
    a,b = b,a+b
#5. mul table
for i in range(1,11):
    print(f"{n} x {i} = {n * i}")
#6.sq of first n no.
for i in range(1,n+1):
    print(i**2)
#7. 

