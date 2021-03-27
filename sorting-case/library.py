def bubble_sort(array, desc=False):
    n = len(array) # jumlah list
    # perulangan pertama
    for i in range(n): 
        # perulangan kedua
        for j in range(n - i - 1):
            # bandingkan masing" elemen
            if desc:
                if array[j] < array[j + 1]:
                    # jika lebih kecil, tukar.
                    array[j], array[j + 1] = array[j + 1], array[j]
            else:
                if array[j] > array[j + 1]:
                    # jika lebih besar, tukar.
                    array[j], array[j + 1] = array[j + 1], array[j]
    return array


def selection_sort(arr, desc=False):  
    n = len(arr)
    # perulangan list elemen
    for i in range(n):
        # cari nilai elemen terendah
        # yang masih tersedia
        min_idx = i
        for j in range(i+1, n):
            if desc:
                if arr[min_idx] < arr[j]:
                    min_idx = j
            else:
                if arr[min_idx] > arr[j]:
                    min_idx = j
        # tukar dengan nilai elemen ke-i
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insert_arr(arr):
    newInt = int(input("Add Number : "))
    arr.append(newInt)
    arr = selection_sort(arr)
    return arr

def change_value(arr, idx, value):
    arr[idx] = value
    arr = selection_sort(arr)
    return arr
