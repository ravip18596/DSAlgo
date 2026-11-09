# Matrix

## Spiral Matrix

```python
def spiral_order(matrix):
    result = []
    if not matrix:
        return result

    i, m = 0, len(matrix) - 1
    j, n = 0, len(matrix[0]) - 1

    while i <= m and j <= n:
        for x in range(j, n + 1):
            result.append(matrix[i][x])
        i += 1

        for x in range(i, m + 1):
            result.append(matrix[x][n])
        n -= 1

        if i <= m:
            for x in range(n, j - 1, -1):
                result.append(matrix[m][x])
            m -= 1

        if j <= n:
            for x in range(m, i - 1, -1):
                result.append(matrix[x][j])
            j += 1

    return result

# Example usage:
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(spiral_order(matrix))  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
```

- Another Solution
```python
def spiral_matrix(mat, r, c):
    i, j = 0, 0
    while i<r and j<c:
        for k in range(j,c):
            print(mat[i][k])
        i+=1
        for k in range(i, r):
            print(mat[k][c-1])
        c-=1

        if j<c:
            for k in range(c-1, j-1, -1):
                print(mat[r-1][k])
            r-=1
        if i<r:
            for k in range(r-1, i-1, -1):
                print(mat[k][j])
            j+=1

    return mat

if __name__ == '__main__':
    r,c = 4, 4
    mat = [
        [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7],
    ]

    print(spiral_matrix(mat, r, c))
```