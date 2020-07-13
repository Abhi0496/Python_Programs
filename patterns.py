# first for loop is for rows
# second for loop is for column
# for adding spaces before, second for loop is used and in that case third for loop is used for printing

for x in range(5,0,-1):
    for y in range(0,x,1):
        print("*", end="")
    print()
print("-------------------------------")

for x in range(1,6):
    for y in range(5,x,-1):
        print(" ", end="")
    for z in range(1,x+1):
        print(z, end = "")
    print()
print("-------------------------------")

for x in range(1,6):
    for y in range(5,x,-1):
        print(" ", end="")
    for z in range(1,x+1):
        print("*", end = "")
    print()
print("-------------------------------")

for x in range(1,6):
    for y in range(5,x,-1):
        print(" ", end = "")
    for z in range(x):
        print("*", end=" ")
    print()
print("-------------------------------")