def find_peak(list_of_integers):
    # Length of the list
    n = len(list_of_integers)
    
    # Edge case: empty list
    if n == 0:
        return None
    
    # Binary search-like approach
    left, right = 0, n - 1
    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid
    
    return list_of_integers[left]

# Testing the function
# print(find_peak([1, 3, 5, 4, 2]))  # Example usage
