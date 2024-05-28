#user to enter first set of integers separated by spaces
list_of_set_0 = input('Enter sets of integer separated by spaces : ' )

#user to enter second set of integers separated by spaces
list_of_set_1 = input('Enter sets of integer separated by spaces : ')

#Split the first input string into  string elements and print output
elements1 = list_of_set_0.split()
result_set1 = set(map(int, elements1))
print(result_set1)

#Split the second input string into  string elements and print output
elements2 = list_of_set_1.split()
result_set2 = set(map(int, elements2))
print(result_set2)

# Create a new set that contains only the elements that are common to both sets and print output
common_elements = result_set1  &  result_set2
print("'\nCommon elements:", common_elements)
