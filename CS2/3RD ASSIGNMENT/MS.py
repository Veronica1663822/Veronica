from Utilities import file_reader
from Mer import merge_arrays
import os 


def merge_sort(a):
    if len(a) <= 1:
        return 0, a

    median = len(a) // 2
    left_count, left = merge_sort(a[:median])
    right_count, right = merge_sort(a[median:])
    combined_inv, combined = merge_arrays(left, right)
    return combined_inv + left_count + right_count, combined


if __name__ == "__main__":
    l = file_reader("rosalind_ms (1).txt")
    ls = list(map(int, l[1].split()))
    n, sorted_arr = merge_sort(ls)
    ans=" ".join(list(map(str, sorted_arr)))
    
    with open(os.path.expanduser("~/downloads/answer.txt"), "w") as file_: 
        file_.write(ans)
        
        
    
