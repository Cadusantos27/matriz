n_linhas = int(input('Digite o número de linhas:'))
n_colunas = int(input('Digite o número de colunas:'))
matriz = []
for i in range(n_linhas):
	linha = []
	for j in range(n_colunas):
		if i == j:
			linha.append('1')
		else:
		     linha.append('0')
	matriz.append(linha)
for i in range(n_linhas):
	print (matriz[i])
