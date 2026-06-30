def bubble_sort(arr: list) -> None:
    """Sort the array using bubble sort (in-place).

    Args:
        arr: list to be sorted (modified in-place)
    """
    if len(arr) <= 1:
        return arr
    
    for i in range (len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                value = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = value
    return arr

def insertion_sort(arr: list) -> None:
    """Sort the array using insertion sort (in-place).

    Args:
        arr: list to be sorted (modified in-place)
    """
    # Replace the code below with your implementation
    raise NotImplementedError


def merge_sort(arr: list) -> list:
    """Sort the array using merge sort (out-of-place).

    Args:
        arr: list to be sorted (not modified)

    Returns:
        New sorted list
    """
    # Replace the code below with your implementation
    raise NotImplementedError


def quick_sort(arr: list) -> list:
    """Sort the array using quick sort (out-of-place).

    Args:
        arr: list to be sorted (not modified)

    Returns:
        New sorted list
    """
    # Replace the code below with your implementation
    raise NotImplementedError
