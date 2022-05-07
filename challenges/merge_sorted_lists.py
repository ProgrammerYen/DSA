def merge_sorted_lists(list1, list2):
	if list1 == [] and list2 == []:
		return []
	
	elif list1 == [] and list2 != []:
		return list2
	
	elif list1 != [] and list2 == []:
		return list1        
	
	merged_list = []
	min_len_list = min([len(list1), len(list2)])
	
	for i in range(min_len_list):
		merged_list.append(list1[i])
		merged_list.append(list2[i])
		
	if len(list1) > len(list2):
		for j in range(len(list2), len(list1)):
			merged_list.append(list1[i])
			
	if len(list1) < len(list2):
		for j in range(len(list1), len(list2)):
			merged_list.append(list2[i])
		
	return merged_list        

result = merge_sorted_lists([1, 3, 5, 6, 7], [1, 6, 7, 9, 10, 15])
print(result)
        