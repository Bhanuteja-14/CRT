'''1) Find Largest NUmber(Using max()) -->largest value in a list'''
numbers = [10, 25, 5, 30, 15]
print(max(numbers))
'''2)check palindrome(Using reversed()) & join()-->reverse the string'''
word = "level"
if word == ''.join(reversed(word)):
    print("Palindrome")
else:
    print("Not Palindrome")
'''3)Count Even Numbers(Using filter())-->filter elements based on a condition'''
arr=[1,2,3,4,5,6,7,8,9,10]
res=list(filter(lambda x:x%2==0,arr))
print(res)
'''4)Find common elements (using set())-->find common elements between two lists'''
list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
common_elements=set(list1).intersection(set(list2))
print(common_elements)
'''5)Index with value using enumerate() function-->get index and value of elements in a list'''
arr=['a','b','c','d']
for index, value in enumerate(arr):
    print(f"Index: {index}, Value: {value}")
'''6)Pair two lists using zip() function-->combine two lists into a list of tuples'''
list1=['a','b','c']
list2=[1,2,3]
zipped_list=list(zip(list1,list2))
print(zipped_list)
'''7)find second largest number using sorted() function-->sort the list and get the second last element
numbers=[10,25,5,30,15]
sorted_numbers=sorted(numbers)
second_largest=sorted_numbers[-2]
print(second_largest)
'''
#find the maximium ele in list
'''numbers=[10,25,5,30,15]
max_number=numbers[0]
for a in numbers:
    if a>max_number:
        max_number=a
print(max_number)'''
