#####################################################################################################################################################
# Name: CommonSortandSearch.py
# Description: This file will have all the common search and sorting algorithms.
# references: 
# Date: 10/2/2016
#####################################################################################################################################################

def insertion_sort(arr):
    '''
    This function will sort the given array using insertion sort algorithm.
    parameters: arr - Array to be sorted inplace
    return: -
    '''
    val = arr[0]
    for i in range(1, len(arr)):
        val = arr[i]
        for j in range(0, i):
            if val < arr[j]:
                while j < i:
                    temp = arr[j]
                    arr[j] = val
                    val = temp
                    j += 1
                arr[i] = val
                break

def merge(arr, i, m, j):
    '''
    This function will merge the two sorted parts of the array.
    parameters: arr - Array whose parts need to be merged properly.
                i - Starting index of the first part of the array
                j - End index of the second part of the array
                m - middle index of the two arrays. Usually end index of fist part and m+1 indicates start of second array
    return: -
    '''
    it1 = i
    it2 = m+1
    newarr1 = []
    newarr2 = []
    k = 0
    l = 0
    while it1 < it2:
        newarr1.append(arr[it1])
        it1 += 1
    while it2 <= j:
        newarr2.append(arr[it2])
        it2 += 1

    it = i

    while k < len(newarr1) and l < len(newarr2):
        if newarr1[k] < newarr2[l]:
            arr[it] = newarr1[k]
            k += 1
        else:
            arr[it] = newarr2[l]
            l += 1
        it += 1

    if k < len(newarr1):
        while k < len(newarr1):
            arr[it] = newarr1[k]
            k += 1
            it += 1

    if l < len(newarr2):
        while l < len(newarr2):
            arr[it] < newarr2[l]
            l += 1
            it += 1

def merge_sort_rec(arr, i, j):
    '''
    This is a recursive function which sorts the given array using merge sort.
    parameter: arr - Array to be sorted
               i - start index of the array to be sorted
               j - end index of the array to be sorted
    return: -
    '''
    if i < j:
        m = (i+j)/2
        merge_sort_rec(arr, i, m)
        merge_sort_rec(arr, m+1, j)
        merge(arr, i, m, j)

def merge_sort(arr):
    '''
    This function will sort the given array using merge sort. It intern uses merge_sort_rec
    parameters: arr - Array to be sorted
    return: - 
    '''
    merge_sort_rec(arr, 0, len(arr) - 1)


def selection_sort(arr):
    '''
    This function will sort the given array using selection sort. 
    parameters: arr - Array to be sorted
    return: -
    '''
    for i in range(0, len(arr) - 1):
        smallest = arr[i]
        index = i
        for j in range(i+1, len(arr)):
            if arr[j] < smallest:
                index = j
                smallest = arr[j]
        temp = arr[i]
        arr[i] = arr[index]
        arr[index] = temp

def binary_search(arr, item):
    '''
    This funciton will search a given item in the sorted array and returns the index of the item if found.
    parameters: arr - Sorted array where we need to find the item's position
                item - number which needs to be searched in the sorted array
    return: - index of the item if found. Else -1
    '''
    index = -1
    i = 0
    j = len(arr) - 1
    
    while i <= j:
        mid = (i+j)/2
        if arr[mid] == item:
            index = mid
            break
        else:
            if arr[mid] > item:
                j = mid - 1
            else:
                i = mid + 1

    return index

def heap_parent(i):
    '''
    In a heapified array this function return the parent index of a given index.
    parameter: i - index whose parents index needs to be found.
    return: parent index of the given index
    '''
    return i/2

def heap_leftchild(i):
    '''
    This function will return the left child index of a given index. Array should be heapified
    parameter: i - possibly a parent index, whose left child index needs to be found
    return: left child index
    '''
    return 2*i + 1

def heap_rightchild(i):
    '''
    This function will return the right child index of a given index. Array should be heapified
    parameter: i - possibly a parent index, whose right child index needs to be found.
    return: right child index
    '''
    return 2*i + 2

def max_heapify(arr, index, size):
    '''
    This function will make an array max heapify that is it make sure that root(index) node is having the highest value when compared
    to its children. 
    parameters: arr - Array whose values needs to be heapified from the index
                index - The parent node from where the heapification needs to be done.
                size - Size of the whole heap structure to be considered for heapification.
    returns: -
    '''
    nlargest = index

    if heap_leftchild(index) < size and arr[index] < arr[heap_leftchild(index)]:
        nlargest = heap_leftchild(index)
        if heap_rightchild(index) < size and arr[nlargest] < arr[heap_rightchild(index)]:
            nlargest = heap_rightchild(index)
    elif heap_rightchild(index) < size and arr[index] < arr[heap_rightchild(index)]:
        nlargest = heap_rightchild(index)
    else:
        nlargest = index

    if nlargest != index:
        temp = arr[nlargest]
        arr[nlargest] = arr[index]
        arr[index] = temp
        max_heapify(arr, nlargest, size)

    pass

def min_heapify(arr, index, size):
    '''
    This function will make an array min heapify that is it make sure that root(index) node is having the minimum or smallest value when
    compared to its children
    parameters: arr - Array whose values needs to be heapified from the index
                index - The parent node from where the heapification needs to be done.
                size - Size of the whole heap structure to be considered for heapification.
    returns: -
    '''
    nsmallest = index

    if heap_leftchild(index) < size and arr[index] > arr[heap_leftchild(index)]:
        nsmallest = heap_leftchild(index)
        if heap_rightchild(index) < size and arr[nsmallest] > arr[heap_rightchild(index)]:
            nsmallest = heap_rightchild(index)
    elif heap_rightchild(index) < size and arr[index] > arr[heap_rightchild(index)]:
        nsmallest = heap_rightchild(index)
    else:
        nsmallest = index

    if nsmallest != index:
        temp = arr[nsmallest]
        arr[nsmallest] = arr[index]
        arr[index] = temp
        min_heapify(arr, nsmallest, size)
    pass

def build_heap(arr, type=0):
    '''
    This function will construct a heap structure from the given array.
    parameters: arr - Array which needs to be converted to heap structure
                type - 0 indicates it needs to be max heapified that is root will have highest value.
                       1 indicates it needs to be min heapified that is root will have lowest value
    return: - 
    '''
    i = len(arr)/2
    while i >= 0:
        if type == 0:
            max_heapify(arr, i, len(arr))
        else:
            min_heapify(arr, i, len(arr))
        i -= 1

def heap_sort(arr):
    '''
    This function will sort the given array using heap sort algorithm
    parameters: arr - Array which needs to be sorted.
    return: - 
    '''
    build_heap(arr)
    i = 0
    while i < len(arr):
        temp = arr[0]
        arr[0] = arr[len(arr) - i - 1]
        arr[len(arr) - i - 1] = temp
        max_heapify(arr, 0, len(arr) - i - 1)
        i += 1

    
    pass

def partition(arr, lo, hi):
    '''
    This function finds the pivot index. That is finds the elements or position such that all the elements before that
    will be less than that element and all the elements which are present after this element will be greater than this element
    params: arr - Array whose elements to be sorted.
            lo - lowest index of the part of array which needs to be sorted.
            hi - highest index of the part of array which needs to be sorted.
    '''
    comp = arr[hi]
    i = lo
    for j in range(lo, hi):
        if arr[j] <= comp:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
    temp = arr[i]
    arr[i] = arr[hi]
    arr[hi] = temp
    return i

def quick_sort_rec(arr, lo, hi):
    '''
    This function is recursive part of the quick sort. It uses partition to get the pivot index.
    params: arr - Array whose elements needs to be sorted.
            lo - lowest index of the part of array to be considered.
            hi - highest index of the part of array to be considered.
    return: -
    '''
    if lo < hi:
        p = partition(arr, lo, hi)
        quick_sort_rec(arr, lo, p - 1)
        quick_sort_rec(arr, p+1, hi)

def quick_sort(arr):
    '''
    This function will sort a given list of numbers using quick sort algorithm
    params: arr - Array of numbers which needs to be sorted.
    return: -
    '''
    quick_sort_rec(arr, 0, len(arr) - 1)
    pass




