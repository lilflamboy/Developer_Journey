number = int(input("Enter a number to check if it's even or odd: "))
print("Even Numbers:") 
for i in range (1, number + 1):    
    
    if i % 2 == 0:
        print( i)
else:
    print("Odd Numbers:")
    for i in range (1, number + 1):
        if i % 2 != 0:
            print(i)    
