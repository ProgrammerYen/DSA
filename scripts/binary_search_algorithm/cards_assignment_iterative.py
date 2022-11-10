import sys

sys.path.append("C:/Users/dealw/OneDrive/SoftwareWork/Programming/PythonWork/DataStructuresAndAlgorithms/Scripts/test_cases/")
from test_cases_search_algorithms import tests

# Recursive function
def test_repeating_values(cards, ind, query): 
    """Checks for repeating values of the query value. Finds the first index of the query value and returns this."""
    card_val = cards[ind]
    if ind > 0:
        if cards[ind - 1] == card_val:
            ind -= 1
            return test_repeating_values(cards, ind, query)
        
    return ind
    
def locate_card(cards, query): # Time complexity: O(log(n))
    """Checks for a query card using divisions of 2 in a binary search algorithm"""
    # Sorting cards in descending order
    cards_decreasing = sorted(cards)
    cards_decreasing.reverse()
    
    # Lowest index, highest index
    low, high = 0, len(cards) - 1    
    
    while low <= high: 
        # The index of the middle value
        mid = (high + low) // 2
        mid_val = cards_decreasing[mid]
        
        # Searching the left half of the list
        if mid_val < query:
            high = mid - 1
        
        # Searching the right half of the list
        elif mid_val > query:
            low = mid + 1
        
        # Returns the index value of the query if the middle value is equal to the query    
        elif mid_val == query:
            repeating_vals = test_repeating_values(cards_decreasing, mid, query)
            return repeating_vals  


list_test_results = []
for test in range(len(tests["inputs"])):
    input_value = tests["inputs"][test]
    query_value = tests["query"][test]
    output_value = tests["expected outputs"][test]
    
    new_result = locate_card(input_value, query_value)
        
    list_test_results.append(new_result == output_value)
                                    
for test_result in list_test_results:
    print(test_result) 
    
if list_test_results.count(True) == len(list_test_results):           
    print("\nPassed all tests including edge cases.")
    
else:
    print(f"\nFailed {list_test_results.count(False)} tests")