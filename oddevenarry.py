l=eval(input("Enter the array: "))
odd=0
even=0
for i in l:
    if i%2==0:
        even+=1
    else:
        odd+=1
print(f"Number of even elements is {even} and Number of odd elements is {odd}")