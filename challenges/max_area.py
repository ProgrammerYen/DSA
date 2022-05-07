def max_area(height):
    # O(n^2)
    # Brute force solution
    
    height_diffs = []
    
    for index, item in enumerate(height):
        for index2, item2 in enumerate(height):
            if index != index2:
                height_diffs.append(abs(index2-index) * min([item, item2]))
                
    return max(height_diffs)


print(max_area([2,4,2,4,2,5,9,3,6,1]))