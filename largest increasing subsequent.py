def lis_length(arr):
    if not arr: 
        return 0
    dp = [1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp), dp

def lis_elements_from_dp(arr, dp):
    max_len = max(dp)
    idx = dp.index(max_len)

    lis = [arr[idx]]
    curr_len = dp[idx] - 1
    for i in range(idx - 1, -1, -1):
        if dp[i] == curr_len and arr[i] < lis[-1]:
            lis.append(arr[i])
            curr_len -= 1

    return lis[::-1]

# Example
arr = [3, 1, 4, 9, 5, 7]
print(arr)
lis, b = lis_length(arr)
lis_seq = lis_elements_from_dp(arr, b)

print("DP array (b):", b)
print("LIS length:", lis)
print("LIS elements:", lis_seq)
