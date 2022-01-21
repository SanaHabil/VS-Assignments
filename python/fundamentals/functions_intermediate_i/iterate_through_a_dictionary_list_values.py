dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for x, y in some_dict.items():
        print( f"{len(y)} {x} ")
        for i in range(0, len(y)):
            print(some_dict[x][i])


result = printInfo(dojo)
print(result)