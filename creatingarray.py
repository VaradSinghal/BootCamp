n = int(input("Enter the number of elements: "))
array = []
for i in range(n):
    element = input(f"Enter element {i + 1}: ")
    array.append(element)
print("The elements in the array are:", array)
