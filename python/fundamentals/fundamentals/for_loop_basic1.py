#Basic
for i in range(0,151):
    print(i)

for x in range(5, 1001):
    if x%5 == 0:
        print(x)

#Multiples of Five 
for y in range(1, 101): 
    if(y % 5 == 0):
        print("Coding")
        if(y % 10 == 0):
            print("Coding Dojo")    
    else:
        print(y)
#Counting, the Dojo Way
total = 0
for n in range(1, 500001):
    if n % 2 == 1:
        total += n
print(total)

#Whoa. That Sucker's Huge
for g in range(2018, 0, -4):
    print(g)

#Flexible Counter 
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum, highNum+1):
    if i % mult == 0:
        print(i)



5+5        