MAX_WEIGHT = 5
NUM_ITEMS = 4

valor  = [3, 9, 12, 8]
peso = [1, 3, 4, 2]

arr = [
	[0 for j in range(MAX_WEIGHT+1)]
	for i in range(NUM_ITEMS+1)
]

for i in range(NUM_ITEMS):
	val = valor[i]
	wt = peso[i]
	
	for j in range(MAX_WEIGHT+1):
		if peso[i] > j:
			arr[i+1][j] = arr[i][j]
			
		else:
			biggestPossibleWeight = j - wt
			if biggestPossibleWeight < 0:
				biggestPossibleWeight = 0
		
			switchOff = arr[i][j]
			switchOn = arr[i][biggestPossibleWeight] + val
			arr[i+1][j] = max((switchOff, switchOn))
			
for row in arr:
	print(("{:4}"*(MAX_WEIGHT+1)).format(*row))