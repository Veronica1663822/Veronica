def insertion_sort(l):
    swaps = 0
    for i in range(1, len(l)):
        j = i
        while j > 0 and l[j-1] > l[j]:
            l[j], l[j-1] = l[j-1], l[j]
            j -= 1
            swaps += 1
    return swaps