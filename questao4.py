import json
dados_JSON = '''[
	{
		"estado": "SP",
		"valor": 6783643
	},
	{
		"estado": "RJ",
		"valor": 3667866
	},
	{
		"estado": "MG",
		"valor": 2922988
	},
 	{
		"estado": "ES",
		"valor": 2716548
	},
  	{
		"estado": "Outros",
		"valor": 1984953
	}]'''

valores = []
nomes = []
dados = json.loads(dados_JSON)

for i in dados:
    valores.append(i['valor'])
    nomes.append(i['valor'])
soma = sum(valores)

print(f'SP com {valores[0]:.2f} que equivale a {(valores[0]*100)/soma:.1f}% do total')
print(f'RJ com {valores[1]:.2f} que equivale a {(valores[1]*100)/soma:.1f}% do total')
print(f'MG com {valores[2]:.2f} que equivale a {(valores[2]*100)/soma:.1f}% do total')
print(f'ES com {valores[3]:.2f} que equivale a {(valores[3]*100)/soma:.1f}% do total')
print(f'OUTROS com {valores[4]:.2f} que equivale a {(valores[4]*100)/soma:.1f}% do total')

