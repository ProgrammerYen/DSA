from rotating_lists_tests import test_cases

def rotate_list(initial_arr, final_arr): # O(log n)
	"""Finds the number of times the values in a list are rotated - moved forward"""
	if initial_arr == final_arr:
		return 0
		
	first_val = initial_arr[0]

	# Searching for the value in the final array. The binary search algorithm is implemented to speed up this process
    # -> faster time complexity of O(log n) --> The binary search algorithm is reversed because the last value which is
    # larger would be moved to the very first position causing the search algorithm to work in an opposite manner
	# Lowest and highest indices
	low, high = 0, len(final_arr) - 1
	while low <= high:
		# Index of the middle value.
		mid = (low + high) // 2
		# Middle value
		mid_num = final_arr[mid]

		# Found the first value
		if mid_num == first_val:
			return mid
			
		# Searching the first half of the array		
		elif mid_num < first_val:
			high = mid - 1

		# Searching the second half of the array
		else:
			low = mid + 1

test_results = []
for i in range(len(test_cases["inputs 1"])):
    initial_input = test_cases["inputs 1"][i]
    final_input = test_cases["inputs 2"][i]
    output = test_cases["outputs"][i] 
    
    result = rotate_list(initial_input, final_input)
    print(result)
    test_results.append(result == output)
    
for test_result in test_results:
    print(test_result)
    
print()

if test_results.count(True) == len(test_results):
    print("Passed all tests including edge cases.")
    
else:
    print("Failed {} tests".format(test_results.count(False)))

	
	
	

