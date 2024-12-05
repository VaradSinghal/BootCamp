n = int(input("Enter the last term: "))
num = 2  

while abs(num) <= n:
    print(num, end=" ")
    num = -num - 2 
