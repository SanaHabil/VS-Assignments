students = [
            {'first_name':  'Michael', 'last_name' : 'Jordan'},
            {'first_name' : 'John', 'last_name' : 'Rosales'},
            {'first_name' : 'Mark', 'last_name' : 'Guillen'},
            {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


def iterateDictionary2(key_name, students):
    for i in range(0, len(students)):
        print(students[i][key_name])


iterateDictionary2('last_name', students)
iterateDictionary2('first_name', students)





