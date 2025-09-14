def insertion_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0
    a = arr.copy()

    for i in range(1, n):
        key = a[i]
        assignments += 1  # присвоєння key
        j = i - 1
        assignments += 1  # присвоєння j

        while j >= 0 and a[j] > key:
            comparisons += 1  # порівняння у while
            a[j + 1] = a[j]
            assignments += 1  # зсув
            j -= 1
            assignments += 1  # зміна j

        # додаткове порівняння, коли while завершився (якщо j >= 0)
        if j >= 0:
            comparisons += 1

        a[j + 1] = key
        assignments += 1  # вставка key

    return a, comparisons, assignments


if __name__ == "__main__":
    data = [90, 10, 15, 80, 100, 6, 57, 5, 29]
    sorted_arr, comps, assigns = insertion_sort(data)
    print("Оригінальний список:", data)
    print("Відсортований список:", sorted_arr)
    print("Кількість порівнянь:", comps)
    print("Кількість присвоєнь:", assigns)
    print("Сума базових операцій:", comps + assigns)
