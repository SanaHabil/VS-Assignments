new_list = []
def values_greater_than_second(num_list):
    if len(num_list) < 2:
        return False
    else:
        for i in range(0,len(num_list)):
            if num_list[i] > num_list[1]:
                new_list.append(num_list[i])
        return new_list  


# Run the function for testing:
input_list = [2]
result = values_greater_than_second(input_list)
print(result)        