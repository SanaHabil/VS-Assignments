students = [
            {'first_name':  'Michael', 'last_name' : 'Jordan'},
            {'first_name' : 'John', 'last_name' : 'Rosales'},
            {'first_name' : 'Mark', 'last_name' : 'Guillen'},
            {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(students_dict):
    for i in range(0, len(students_dict)):
        output= ""
        for x, y in students_dict[i].items():
            output += f" {x} - {y}," 
        print(output)  

result = iterateDictionary(students)
print(result)