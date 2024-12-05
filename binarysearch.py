def binary_search(arr,y):
    pos=-1
    first=0
    last=len(arr)-1
    while first<=last:
        mid=int(first+last)//2
        if arr[mid]==y:
            pos=mid
            print("Found element at",pos)
            break
        if arr[mid]>y:
            last=mid-1
        else:
            first=mid+1
    if pos<0:
        print("Search unsuccessful")
L=eval(input("enter a sorted list: "))
y=int(input("Entert he value to be searched: "))
binary_search(L,y)