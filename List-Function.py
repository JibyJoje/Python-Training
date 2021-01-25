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


