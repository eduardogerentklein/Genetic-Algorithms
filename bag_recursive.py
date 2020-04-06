maxWeight = 30
value  = [15, 7, 10, 5, 8, 17]
weight = [15, 3, 2, 5, 9, 20]

def bag(pos, selected):
	# calcula o total
	totalValue = 0 
	pesoTotal = 0

	for i in selected:
		totalValue += value[i]
		pesoTotal += weight[i]

	if pesoTotal > maxWeight:
		return (0,0)
		
	if pos >= len(weight):
		return (totalValue, pesoTotal)
	
	answer1 = bag(pos + 1, selected + [pos])
	answer2 = bag(pos + 1, list(selected))
	
	if answer1[0] > answer2[0]:
		return answer1
	else:
		return answer2
		
bestAnswer = bag(0, [])
print(bestAnswer)