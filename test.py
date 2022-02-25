def double_nums():
	results = []
	
	for i in range(1,51):
		if i % 2 == 0:
			results.append(i)
	
	return results

print(double_nums())