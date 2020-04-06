WEIGHT_LIMIT = 5
valor  = [3, 9, 12, 8]
peso = [1, 3, 4, 2]

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
	
	ans1 = knapsack(pos+1, selected+[pos])
	ans2 = knapsack(pos+1, list(selected))
	
	if ans1[0] > ans2[0]:
		return ans1
	else:
		return ans2
		
ans = knapsack(0, [])
print(ans)