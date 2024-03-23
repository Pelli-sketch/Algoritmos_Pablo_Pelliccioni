# Bubble Sort
def bubble_sort_ultimo_primero(arr):
    n = len(arr)
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Insertion Sort
def insertion_sort_ultimo_primero(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# Selection Sort
def selection_sort_ultimo_primero(arr):
    for i in range(len(arr)-1, -1, -1):
        max_index = i
        for j in range(i + 1, len(arr)):
            if arr[max_index] < arr[j]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]

# Merge Sort
def merge_sort_max_a_min(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    merge_sort_max_a_min(left_half)
    merge_sort_max_a_min(right_half)

    i = j = k = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j] 
            j += 1
        k += 1

    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

    return arr

arr = [5, 3, 8, 4, 6]
bubble_sort_ultimo_primero(arr)
print(arr)

arr = [5, 3, 8, 4, 6]
insertion_sort_ultimo_primero(arr)
print(arr)

arr = [5, 3, 8, 4, 6]
selection_sort_ultimo_primero(arr)
print(arr)

arr = [5, 3, 8, 4, 6]
print(merge_sort_max_a_min(arr))