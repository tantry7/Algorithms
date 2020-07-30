print("enter number of ele")
t = int(input())
s = list(map(int,input().split()))
k,a,b =[],[],[]
mid = len(s)//2
a = s[:mid]
b = s[mid:]
i,j = 1,2
for t in range(len(s)):
    if a[i]>b[j]:
        k[t]=a[i]
        i = i+1
    else :
        k[t]=b[j]
        j = j+1

print("Sorted array using merge sort")
print(k)
