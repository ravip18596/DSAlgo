def sqrt_rec(n, low, high, ans=0):
    if low>high:
        return ans
    mid = (low+high)>>1
    sq = mid*mid

    if sq == n:
        return mid
    if sq < n:
        return sqrt_rec(n, mid+1, high, mid)
    else:
        return sqrt_rec(n, low, mid-1, ans)


def sqrt(n):
    if n<2:
        return n

    low, high = 1, n//2
    return sqrt_rec(n, low, high)

if __name__ == '__main__':
    print(sqrt(10))