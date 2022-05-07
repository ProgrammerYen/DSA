def longestCommonPrefix(strs):
    # Find the string of lowest length
    # Using a for loop and range with an input of the length of the string, we will stores slice values that are found in this string. The slice values will begin from the start of the string to the index value in the loop. 
    # We will store the slice values in an array.
    # Next, we will find the slice value of greatest length which is common in all strings.
    # If there is no common prefix, we will return an empty string.
    lengths_strs = [len(string) for string in strs]
    lowest_length_str = strs[lengths_strs.index(min(lengths_strs))]
    prefixes = []
    
    for i in range(len(lowest_length_str)):
        prefixes.append(lowest_length_str[:i+1])

    common_prefixes = {prefix: 0 for prefix in prefixes}
    
    for j in range(len(strs)):
        for prefix in prefixes:
            if prefix == strs[j][:len(prefix)]:
                common_prefixes[prefix] += 1
    
    common_all_prefixes = []
    for common_prefix, prefix_count in common_prefixes.items():
        if prefix_count == len(strs):
            common_all_prefixes.append(common_prefix)
            
            
    lengths_prefixes = [len(common_prefix) for common_prefix in common_all_prefixes]
    
    if lengths_prefixes == []:
        return ""
        
    return common_all_prefixes[lengths_prefixes.index(max(lengths_prefixes))]

print(longestCommonPrefix(["flow", "flower", "flight"]))
            
                    
                    
            
            
        
        
        
                    