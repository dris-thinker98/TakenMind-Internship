import numpy as np

my_list1 = [1,2,3,4]
my_list2 = [5,6,7,8]

my_array = np.array(my_list1)

my_array = np.array([my_list1,my_list2])
print my_array

#usage of shape function
#print my_array.shape

#finding out the datatype of the members of the array
#print my_array.dtype

#zeros, ones, empty, eye, arange

#new_array1 = np.zeros(5) #creates a new numpy array with (1*5). All elements are zero
#new_array1 = np.ones([5,5]) #all elements as 1
#new_array1 = np.eye(5)
new_array1 = np.arange(5,50,3)
print new_array1
