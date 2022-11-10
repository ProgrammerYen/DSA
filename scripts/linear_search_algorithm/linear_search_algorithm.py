from scripts.test_cases_search_algorithms import tests


def locate_card(cards, query):
    """Locating a random card, which has been chosen, in a list of cards which are arranged in descending order.
    Uses the linear search algorithm."""   
    
    # Sort cards in descending order.
    decreasing_cards = cards.copy()
    decreasing_cards.sort()
    decreasing_cards.reverse()

    # Checking if the query is in the list of cards.
    for card in decreasing_cards:
        if card == query:
            return decreasing_cards.index(card)

    # If the query is not found within the list of cards, we do not return a result, we return None


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