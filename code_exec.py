arr = [10, 4, 3, 50, 23, 90]

first, second, third = arr[0], None, None
n = len(arr)

for i in range(1, n):
    if arr[i] > first:
        third = second
        second = first
        first = arr[i]
    elif second != None and arr[i] > second and first != arr[i]:
        third = second
        second = arr[i]
    elif third !=None and arr[i] > third and second != arr[i]:
        third = arr[i]

print(f'first:{first}, second:{second}, third:{third}')
