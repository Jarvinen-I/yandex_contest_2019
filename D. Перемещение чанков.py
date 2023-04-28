n, m, q = list(map(int, input().split())) # кол-во чанков, кол-во серверов, кол-во запросов
p = list(map(int, input().split())) # изначальное расположение чанков

for i in range(q):
	a, b, l, r = list(map(int, input().split())) # сервер a, сервер b, чанки с l по r
	flag = True
	for j in range(l, r + 1):
		if j != a:
			flag = False
	print(1 if flag else 0)
