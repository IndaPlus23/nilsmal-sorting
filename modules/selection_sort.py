from .frontend import run_frontend

def selection_sort(arr, display=False):
    i = 0
    while i < len(arr) - 1:
        if display: run_frontend(arr)
        min_index = i
        j = i + 1

        while j < len(arr):
            if arr[j] < arr[min_index]:
                min_index = j
            j += 1

        if min_index != i:
            # Swap A[i] and A[min_index]
            arr[i], arr[min_index] = arr[min_index], arr[i]

        i += 1

    return arr