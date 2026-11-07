
# Sorting Algorithms in Data Structures
# Beginner Friendly Python Project

def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def selection_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def insertion_sort(arr):
    arr = arr.copy()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + equal + quick_sort(right)


def main():
    print("\n===== SORTING ALGORITHMS PROJECT =====")

    try:
        numbers = input(
            "\nEnter numbers separated by spaces: "
        )

        arr = [int(x) for x in numbers.split()]

        if not arr:
            print("Please enter at least one number.")
            return

    except ValueError:
        print("Invalid input! Please enter integers only.")
        return

    print("\nOriginal Array:", arr)

    print("\nChoose Sorting Algorithm:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Merge Sort")
    print("5. Quick Sort")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        result = bubble_sort(arr)
        name = "Bubble Sort"

    elif choice == "2":
        result = selection_sort(arr)
        name = "Selection Sort"

    elif choice == "3":
        result = insertion_sort(arr)
        name = "Insertion Sort"

    elif choice == "4":
        result = merge_sort(arr)
        name = "Merge Sort"

    elif choice == "5":
        result = quick_sort(arr)
        name = "Quick Sort"

    else:
        print("Invalid choice! Please choose between 1 and 5.")
        return

    print("\nAlgorithm:", name)
    print("Sorted Array:", result)


if __name__ == "__main__":
    main()
