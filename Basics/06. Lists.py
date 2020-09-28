#List is a data structure in Python that is a mutable, or changeable, ordered sequence of elements which allows duplicate members. Lists are defined by having 
#values between square brackets [ ].

myList = [9.5,'Ayve',12]           #This is  a List
names = ['Ayve','Arman','Atoshe']  #Another List
nums = [5,8,12,15,20,24,27,30,35]  #Another List

print(nums[0])                     #will print the value of first index
print(nums[-1])                    #will print the value of last index
print(nums[2:5])                   #will print the value from index 2 to 4
nums.append(45)                    #45 will be added at the end of the list
print(nums)

#Another way to print the list
for x in nums:
    print(x)
    
#Checking an item is in the list or not
if 'Ayve' in names:
    print("Yes, 'Ayve' is in the name list.")
    
#List length
print("Length of nums :",len(nums))
print("Length of names :",len(names))
print("Length of myList :",len(myList))

nums.insert(2,10)                  #list.insert(index,value). Indexing starts from 0.
print(nums)
nums.remove(15)                    #list.remove(value)
print(nums)
nums.pop()                         #remove the last element
print(nums)
nums.pop(1)                        #list.pop(index)
print(nums)
del nums[5:7]                      #remove values from index 5 to 7
print(nums)
#del nums will delete the list completely
#nums.clear()  will make the list empty.

#Making a copy of a list
newList = myList.copy()
print(newList)
#Another way
newList1 = list(myList)
print(newList1)

#Joining two lists
list1 = ["a","b","c"]
list2 = [1,2,3]
list3 = list1+list2
print(list3)
#Another way
list3 = ["d","e","f"]
list4 = [4,5,6]
for x in list4:
  list3.append(x)
print(list3)
#Another way
list3.extend(list4)
print(list3)

print(nums)
nums.extend([29,38,52,14,43,13])     #will be added at the end of the list
print(nums)
print(min(nums))                   #will return the minimum number of the list
print(min(names))
print(max(nums))                   #will return the maximum number of the list
print(sum(nums))                   #summation of all elements. Only when the elements are integer values.
nums.sort()                        #will sort the list
print(nums)
#print(sum(names))                 #Error
#print(sum(myList))                #Error

#List constructor
Latest_list = list(("apple", "banana", "cherry"))  #note the double round-brackets
print(Latest_list)

#Happy Coding! ^_^
