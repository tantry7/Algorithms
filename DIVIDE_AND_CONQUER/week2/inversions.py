#for N^2
f=[]
s = open("interger.txt")
for x in s:
    f.append(int(x))



def getInvCount(arr, n):

    inv_count = 0
    for i in range(len(arr)):
        for j in range(i + 1,len(arr)):
            if (arr[i] > arr[j]):
                inv_count += 1

    return inv_count
n = 1000000
S = getInvCount(f,n)
print(S)
