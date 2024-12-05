l = eval(input("Enter the array: "))
ch = str(input("Ascending (a) or Descending (s): "))

if ch == "a":
   
    for i in range(len(l)):
        min_index = i
        for j in range(i + 1, len(l)):
            if l[j] < l[min_index]:
                min_index = j
        l[i], l[min_index] = l[min_index], l[i]
    print("Sorted list in ascending order:", l)

elif ch == "s":

    for i in range(len(l)):
        max_index = i
        for j in range(i + 1, len(l)):
            if l[j] > l[max_index]:
                max_index = j
        l[i], l[max_index] = l[max_index], l[i]
    print("Sorted list in descending order:", l)

else:
    print("Invalid choice. Please enter 'a' for ascending or 's' for descending.")
