l = []
def countdown(n):
    while n>= 0:
        l.append(n)
        n = n-1
    return l 

#call the function for testing
result = countdown(10)
print(result)