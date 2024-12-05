n = int(input("Enter the last term: "))
current_value = 4 
diff = 3  
sequence = []

while current_value <= n:
    sequence.append(current_value)
    current_value += diff
    diff = diff + (len(sequence) // 2) + 1  

print(sequence)
