

    # Ask the user to input a list of integers separated by spaces
input_string = input("Enter list of integer separated by spaces: ")

 # Split the input string into a list 
input_list = input_string.split()

    # Convert the list of strings into a list of integers
integer_list = [int(x) for x in input_list]

    # Print  list of integers
print("List of integers:", integer_list)
   # calculate the sum of integer
Total_sum = sum(integer_list)
    # print total sum of integer
print("The sum of numbers entered is :", Total_sum)
