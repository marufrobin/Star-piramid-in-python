rows = int(input("Enter the rows value: "))

# printing diamons of star
for i in range(rows,0, - 1):
    for space in range(rows - i):
        print(' ',end='')
    for j in range(2*i-1):
        print('*',end='')
    print()
    
