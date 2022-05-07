from binary_search_algorithm_iterative import test_repeating_values
from scripts.test_cases_search_algorithms import tests


def locate_card_recursive(cards, query, high, low):
    # Sort the list of cards
    cards = sorted(cards)
    
    # Index of the middle of the list of cards
    mid = (high + low) // 2
    
    if mid >= 0:
        mid_num = cards[mid]
        if mid_num == query:
            test_repeating_values(cards,mid,query)
            return mid
        
        elif mid_num > query:
            return locate_card_recursive(cards, query, mid-1, low)
    
        else:
            return locate_card_recursive(cards, query, high, mid+1)
        
list_test_results = []
for test in range(len(tests["inputs"])):
    input_value = tests["inputs"][test]
    query_value = tests["query"][test]
    output_value = tests["expected outputs"][test]
    
    new_result = locate_card_recursive(input_value, query_value, len(input_value) - 1, 0)
        
    list_test_results.append(new_result == output_value)
                                    
for test_result in list_test_results:
    print(test_result) 
    
if list_test_results.count(True) == len(list_test_results):           
    print("\nPassed all tests including edge cases.")
    
else:
    print(f"\nFailed {list_test_results.count(False)} tests")