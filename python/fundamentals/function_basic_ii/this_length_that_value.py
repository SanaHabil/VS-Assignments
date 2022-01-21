new_list = []
def this_length_that_value(len,value):
    for i in range(0, len):
        new_list.append(value)
    return new_list  


# Run the function for testing:
input_list = this_length_that_value(10,2)
print(input_list)