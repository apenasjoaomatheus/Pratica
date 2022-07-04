from itertools import count


palavra = "Teste Prático"
auxiliar = 1
palavraReversa = []

tamanho = len(palavra)

for i in range(0, len(palavra)):
    palavraReversa.append(palavra[len(palavra)-auxiliar])
    auxiliar += 1
    
print(''.join(palavraReversa))