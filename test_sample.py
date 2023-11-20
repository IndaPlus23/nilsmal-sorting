import numpy as np

from modules.frontend import run_frontend_final
from modules.bogo_sort import bogo_sort
from modules.insertion_sort import insertion_sort
from modules.selection_sort import selection_sort
from modules.merge_sort import merge_sort

arr = np.array([0.3, 0.4, 0.5, 0.2, 0.1])
sorted_arr = np.array([0.1, 0.2, 0.3, 0.4, 0.5])


def test_bogo_sort():
    for a,b in zip(bogo_sort(arr), sorted_arr):
        assert a == b

def test_insertion_sort():
    for a,b in zip(insertion_sort(arr), sorted_arr):
        assert a == b

def test_selection_sort():
    for a,b in zip(selection_sort(arr), sorted_arr):
        assert a == b

def test_merge_sort():
    for a,b in zip(merge_sort(arr), sorted_arr):
        assert a == b
  
    