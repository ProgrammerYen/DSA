def binary_search(arr, query): # tc: O(log n)
    # the lowest and highest index in arr
    low, high = 0, len(arr) - 1
    # runs until query is found in arr
    while True:
        # finding the middle index in a list of values
        mid = (low + high) // 2
        # finding the middle value in a list of a values using mid_index as an index
        mid_value = arr[mid]
        
        if mid_value < query:
            low = mid + 1
        elif mid_value > query:
            high = mid - 1
        else:
            return mid
            
print(binary_search([1,4,8,20,45,46,47,47,47,47,48], 47
))


        
    