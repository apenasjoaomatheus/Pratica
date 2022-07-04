numero = int(input("Digite o numero: "))

numAnterior = 0
numProximo = 1
numSoma = 1
sequencia = []

for x in range(101):
    numSoma = numProximo + numAnterior
    numAnterior = numProximo
    numProximo = numSoma
    sequencia.append(numAnterior)
intSequencia = list(map(int, sequencia))

if numero in intSequencia:
    print(f"O numero {numero} está entre os 100 primeiros numeros da sequencia de fibonacci")
else:
    print(f"O numero {numero} não está entre os 100 primeiros numeros da sequencia de fibonacci")

