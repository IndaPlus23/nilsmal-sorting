import numpy as np

from modules.frontend import run_frontend_final
from modules.bogo_sort import bogo_sort
from modules.insertion_sort import insertion_sort
from modules.selection_sort import selection_sort
from modules.merge_sort import merge_sort
from modules.bubble_sort import bubble_sort
from modules.quick_sort import quick_sort



def main():
    arr = np.random.rand(100)
    sorted = bogo_sort(arr, True)
    print(sorted)
    run_frontend_final(sorted)

if __name__ == "__main__":
    main()