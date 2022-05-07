def two_sum(array, target):
    hash_table = {}
    for i in array:
        complement = target - i
        if complement in hash_table:
            return [i, complement]
        
        hash_table[i] = i
        
