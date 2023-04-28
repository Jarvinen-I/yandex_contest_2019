t = int(input()) # кол-во тестов

for test in range(t):
	n = int(input()) # кол-во лежаков
	a = [int(num) for num in input().split()] # идентификаторы лежаков
	similar = 10 ** 9 # непохожесть

	for i in a:
		for j in a:
			if i != j and i ^ j < similar: # i ^ j - XOR
				similar = i ^ j

	print(similar)
