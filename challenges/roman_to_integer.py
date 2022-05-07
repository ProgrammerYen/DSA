def roman_to_integer(s):
    # If a roman numeral value is placed before a larger roman numeral value,
    # We subtract that value from the larger roman numeral value.
    # For example, IV = V - 1 = 10 - 1 = 9
    
    # Roman numeral symbol --> value
    roman_values = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    
    list_s = list(s)
    symbol_val = 0
    
    for i in range(len(s)):
        if i != len(s) - 1:
            if roman_values[list_s[i]] < roman_values[list_s[i + 1]]:
                symbol_val -= roman_values[list_s[i]]
                
            else:
                symbol_val += roman_values[list_s[i]]
            
        else:
            symbol_val += roman_values[list_s[i]]
            
    return symbol_val
    