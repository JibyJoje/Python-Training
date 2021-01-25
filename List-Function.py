# Sample program to demonstrate some commonly used functions with Lists

print('Program to demonstrate commonly used functions with Lists:')

myList = []
print("Enter the item in the list: ") 
myList.append(input())
print(myList)

while True:
	print("Do you want to add more items to the list (y/n):")
	if (input()== 'y'):
		print("Enter the new item in the list: ")
		myList.append(input())
		print(myList)
	else:
		break

print("There are now total of "+str(len(myList))+ " in your list")

print("Using Index Function")
print('Enter the item from the list whose index you want to find: ')
myValue = input()
print('The index of '+myValue+' is '+str(myList.index(myValue)))

print("Using Insert Function")
print('Enter at which index you want to enter the new item: ')
newIndex = input()
print('Enter the new item you want to add at '+newIndex+' :')
newItem = input()
myList.insert(int(newIndex), newItem)
print(myList)

print('Using the Sort function')
myList.sort()
print('Sorted List :'+str(myList))
myList.sort(reverse=True)
print('Reverse Sorted List: '+str(myList))		










