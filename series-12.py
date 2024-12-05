n = int(input("Enter the last term: "))
num = 1  
sign = 1 

while abs(num) <= n:
    print(num, end=" ")
    num += 4  
    sign *= -1 
