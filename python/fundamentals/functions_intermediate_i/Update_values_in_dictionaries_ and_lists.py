x = [ [5,2,3], [10,8,9] ] 
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#################################################################

#1 Function to Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
def list_update(x):
    x[1][0]=15
    return x    

result = list_update(x)
print(result)   

#2 Change the last_name of the first student from 'Jordan' to 'Bryant' 
def change_last_name(students):
    students[0]['last_name'] = "Bryant"
    return students

result = change_last_name(students)
print(result)    

#3 In the sports_directory, change 'Messi' to 'Andres'
def sports_dictionary_change(sports_directory):
    sports_directory['soccer'][0] = "Andres"
    return sports_directory
result = sports_dictionary_change(sports_directory)
print(result)      


#4 Change the value 20 in z to 30
def change_value_z(z):
    z[0]['y'] = 30
    return z

result = change_value_z(z)
print(result)     