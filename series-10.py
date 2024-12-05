n = int(input("Enter the last term: "))
current_value = 2
diff = 1 


while current_value <= n:
    print(current_value, end=" ")
    current_value += diff
    diff += 3  


