def summer_69(arr):
    add = 0
    skip = False

    for i in range(len(arr)):
        if arr[i] == 6:
            skip = True
        elif arr[i] == 9 and skip:
            skip = False
        elif not skip:
            add += arr[i]

    return add

# Check
print(summer_69([1, 3, 5]))       # Expected output: 9 (1 + 3 + 5)
print(summer_69([4, 5, 6, 7, 8, 9]))  # Expected output: 9 (4 + 5)
print(summer_69([2, 1, 6, 9, 11]))  # Expected output: 14 (2 + 1 + 11)
