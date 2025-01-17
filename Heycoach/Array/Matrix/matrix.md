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
