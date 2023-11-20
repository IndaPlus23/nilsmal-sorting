from .frontend import run_frontend

def bogo_sort(arr, display=False):
    import random
    while not all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)):
        if display: run_frontend(arr)
        random.shuffle(arr)
    return arr