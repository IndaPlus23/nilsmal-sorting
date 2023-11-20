import numpy as np

def merge_sort(arr, display=False):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(a, b):
    c = []

    while len(a) > 0 and len(b) > 0:
        if a[0] > b[0]:
            c.append(b[0])
            b = b[1:]
        else:
            c.append(a[0])
            a = a[1:]

    # Extend the remaining elements from a and b
    c.extend(a.tolist())  # Convert NumPy array to a list before extending
    c.extend(b.tolist())

    return np.array(c)