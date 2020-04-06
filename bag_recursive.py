WEIGHT_LIMIT = 30
valor  = [15, 7, 10, 5, 8, 17]
peso = [15, 3, 2, 5, 9, 20]

def knapsack(pos, selected):

	# calcula o total
	totalValue = 0 
	totalWeight = 0
	
	for i in selected:
		totalValue += valor[i]
		totalWeight += peso[i]

	if totalWeight > WEIGHT_LIMIT:
		return (0,0)
		
	if pos >= len(peso):
		return (totalValue, totalWeight)
	
	answer1 = knapsack(pos+1, selected+[pos])
	answer2 = knapsack(pos+1, list(selected))
	
	if answer1[0] > answer2[0]:
		return answer1
	else:
		return answer2
		
bestAnswer = knapsack(0, [])
print(bestAnswer)