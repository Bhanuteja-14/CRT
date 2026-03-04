'''
li = [1, 2, 3, 4, 5]
#output : [2,4,6,8,10]
res = []
for ele in li:
    res.append(ele * 2)
print(res)
print([ele * 2 for ele in li])

li = [1, 2, 3, 4, 5]
res = []
for i in li:
    if i % 2 == 0:
        res.append(i)
print(res)
print([i for i in li if i % 2 == 0])
print((i for i in li if i % 2 == 0))
print({i: i**2 for i in li if i % 2 == 0})
'''
'''1. Pyramid
n = 4
output:
      *
    *   *
  *   *   *
*   *   *   * 
'''
n = 4
for i in range(n,0, - 1):
    print(" " * (n-i) + "* " * i)