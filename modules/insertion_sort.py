from .frontend import run_frontend

def insertion_sort(arr, display=False):
    for i in range(1, len(arr)):
        if display: run_frontend(arr)
        x = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > x:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = x

    return arr