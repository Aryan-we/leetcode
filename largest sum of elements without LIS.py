
def lis_length(arr):
    if not arr: 
        return 0
    dp=[1]*len(arr)
    for i in range(1,len(arr)):
        for j in range(i):
            if arr[i]>arr[j]:
                dp[i]=max(dp[i],dp[j]+1)
    print(dp)
    return max(dp)
arr=[3,2,6,4,5]
lis=lis_length(arr)
#max increasing subsequent in an array
total=sum(arr)
print(total)
maxs=total-sum(arr[i] for i in range(len(arr)) if lis_length(arr[:i]+arr[i+1:])==lis)
print(maxs)
        
    
