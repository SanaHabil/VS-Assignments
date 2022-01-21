def first_plus_length(num_list):
    list_length = len(num_list)
    sum = num_list[0] + list_length
    return sum


# run the function for testing:
input_list = [0,2,3,4,5,3,4,5,5]
result = first_plus_length(input_list)
print(result)