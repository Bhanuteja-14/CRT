'''
Docstring for 4th-SEM.Python.Practice.M02_Logic_Building_abd_Patterns.PS01_Digits_Problems
n = int(input())
temp = n
count = 0
while n>0:
    count += 1
    n//=10
print(count)
print(len(str(temp)))
print()
'''
n = int(input())
while n > 10:
    n = sum(list(map(int,str(n))))
print(n)
