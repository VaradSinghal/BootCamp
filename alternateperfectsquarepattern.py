n = int(input("Enter the number of rows: "))
num = 1  
sign = 1  

for i in range(1, n + 1):
    for j in range(i):
        square = num * num  
        print(sign * square, end=" ") 
        num += 1 
        sign *= -1  
    print()  
