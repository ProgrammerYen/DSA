def is_palindrome(x):
    list_x = list(str(x))
        
    list_x_copy = list_x.copy()
    list_x_copy.reverse()
    return list_x_copy == list_x