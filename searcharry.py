l=eval(input("Enter the array: "))
element=int(input("Enter term to be searched"))
for i in l:
    if i==element:
        print("Element found at position",i)
    else:
        print("There is no",element,"in the array")