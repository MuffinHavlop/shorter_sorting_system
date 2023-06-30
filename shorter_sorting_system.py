array = [23, 2, 3, 1, 5, 6, 4]

for i in range(len(array)):
    j = i
    for j in range(i):
        if array[j] > array[i]:
            array[j], array[i] = array[i], array[j]

print(array)