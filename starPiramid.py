rows = int(input("Enter the rows value: "))
k = 0

# printing diamons of star
for i in range(1, rows + 1):
    for space in range(1, (rows - i) + 1):
        print(end="  ")
    while k != (2*i-1):
        print("*",end=" ")
        k+=1
    k=0
    print()