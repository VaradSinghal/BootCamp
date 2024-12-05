n = int(input("Enter the last term: "))
i = 1
diff = 3  


while i <= n:
    print(i)
    i+= diff
 
    diff = diff * 2 - 1 


