def binarySearch(l, x, low, high):
  if low>high:
    return -1
  mid=(low+high)//2
  if l[mid]==x:
    return mid
  elif l[mid]<x:
    return binarySearch(l,x,mid+1,high)
  else:
    return binarySearch(l,x,low,high-1)

def bSearchIterative(l,x):
  return binarySearch(l,x,0,len(l)-1)

n=int(input("Enter the number of elements: "))
l=list(map(int,input("\nEnter the numbers of the sorted list : ").strip().split()))[:n]
x=int(input("Enter the number to search: "))
result=bSearchIterative(l,x)
if result != -1:
    print(f"{x} is present in the list at index {result}")
else:
    print(f"{x} is not present in the list")