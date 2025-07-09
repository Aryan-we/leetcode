import itertools
arr="abc"
superset=[]
for i in range(len(arr)+1):
    data=itertools.combinations(arr,i)
    superset.extend(data)
superset=[list(a) for a in superset]   
print(superset)
b=[]
n=len(arr)
for i in range(1<<n):
    a=''
    for j in range(len(arr)):
        if i & 1<<j:
            a+=arr[j]
    b.append(a)
print(b)
    

    
    
