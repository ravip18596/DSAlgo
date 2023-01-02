def minJumps(arr):
    n = len(arr)
    dp = [[0]*(n+1) for i in range(n+1)]

    dp[n][n] = arr[n-1]

    j = n-1
    for i in range(n, 0, -1):
        for j in range(n, 0, -1):
            dp[i][j] = min(dp[i][j])


if __name__ == '__main__':
    res = minJumps([65,-3,31,-61])
    print(res)

