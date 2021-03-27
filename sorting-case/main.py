import library


# case 1
unordered = [92, 31, 46]
print("Algoritma Bubble Sort")
# ascending
print(library.bubble_sort(unordered))
# descending
print(library.bubble_sort(unordered, desc=True))
print()

# case 2
unordered = [92, 31, 46]
print("Algoritma Selection Sort")
# ascending
print(library.selection_sort(unordered))
# descending
print(library.selection_sort(unordered, desc=True))
print()

# case 3
loop = True
while loop:
    unordered = library.insert_arr(unordered)
    print(unordered)
    loop = True if input("Tambah Lagi (y/n) : ") == "y" else False

# case 4
print()

# case 4.1
B = [15, 12, 20, 50 ,100]
condition = True if B[0] > B[-1] else False
B = library.selection_sort(B, desc=condition)
print(B)

# case 4.2
library.change_value(B, 0, 1000)
print(B)



