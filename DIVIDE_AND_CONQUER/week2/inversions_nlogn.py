f,n=[],0
s = open("interger.txt")
for x in s:
    f.append(int(x))
    n = n+1
print(f)
print(n)
'''
def merges(arr,n):
    temp = []*n
    return mergesort(arr,temp,left,right)

def mergesort(arr,temp,left,right):
    count = 0
    if left>right:
        mid = (left+right)//2
        count += mergesort(arr,temp,left,mid)
        count += mergesort(arr,temp,mid+1,right)
        count += merge(arr,temp,left,right,mid)
    return count
def merge(arr,temp,left,right,mid):
    i = left
    j = right
    k = left
    count = 0
    while i<=mid and j<=right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k = k+1
            i = i+1
        else :
            temp[k] = arr[j]
            count = count + (mid -i + 1)
            k = k+1
            i = i+1
    while i<=mid:
        temp[k] = arr[i]
        k = k+1
        i = i+1
    while j<=right:
        temp[k] = arr[j]
        k = k+1
        i = i+1
    return count
