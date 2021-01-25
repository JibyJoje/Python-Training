# This program shows the simple example on Lists in Python

print('Program to show simple list example')

myList = ['This', 'is', 'a', 'Simple', 'Lists', 'Array'] #declaring and defining the list items

#printing the lists and the items at each index
print ('The items of the lists are: '+str(myList))
for items in range(len(myList)) :
	print(' The item at the index '+str(items)+' is :'+myList[items])

#Replacing items in a list
print('-------------------------------')
print('The current item at index 2 is '+myList[2])
print('Replacing the item at index 2')
myList[2] = 'new_value'
print('The new item at index 2 is '+myList[2])

#Slicing a list 
print('-------------------------------')
print('Slicing the list: '+str(myList[3:]))


#Deleting an item in a list
print('-------------------------------')
print('List before deleting '+str(myList))
del myList[2]
print('List after deleting '+str(myList))



