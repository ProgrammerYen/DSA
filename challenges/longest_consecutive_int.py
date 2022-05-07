def longest_consecutive_int(num, arr):
    """Finding the longest consecutive set of repeating integers in an array."""
    consecutive_int_length = {}
    count = 0
    count2 = 0
    g = 0
    repeating_ints = []
    lengths = []
    while count < len(arr):
        if arr[count] == num:
            repeating_ints.append([count,count])
            while arr[count] == num:
                repeating_ints[-1][-1] += 1  
                count += 1
                if count == len(arr):
                    g = 1
                    break
                
            length = repeating_ints[-1][-1] - repeating_ints[-1][0]
            consecutive_int_length[repeating_ints[-1][-1] - repeating_ints[-1][0]] = repeating_ints[-1]
            lengths.append(length)
            
            if g == 1:
                break
                
            count2 += 1 
            
        count += 1
        
    return consecutive_int_length[max(lengths)]
       
            
print(longest_consecutive_int(0, [0,1,0,0,1,2,3,4,0,0,0,0,0,1,2,0,0,0,2]))