def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0
    a = arr.copy()

    for i in range(n - 1):
        min_index = i
        assignments += 1
        for j in range(i + 1, n):
            comparisons += 1
            if a[j] < a[min_index]:
                min_index = j
                assignments += 1
        comparisons += 1
        if min_index != i:
            tmp = a[i]
            a[i] = a[min_index]
            a[min_index] = tmp
            assignments += 3

    return a, comparisons, assignments


if __name__ == "__main__":
    data = [90, 10, 15, 80, 100, 6, 57, 5, 29]
    sorted_arr, comps, assigns = selection_sort(data)
    print("Оригінальний список:", data)
    print("Відсортований список:", sorted_arr)
    print("Кількість порівнянь:", comps)
    print("Кількість присвоєнь:", assigns)
