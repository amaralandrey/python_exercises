"""
1) Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C.
"""

values = []
labels = ["A", "B", "C"]

for i in range(3):
    valor = int(input(f"Informe o valor de {labels[i]}: "))
    values.append(valor)

def greater_than_c(array):
    if array[0] + array[1] < array[2]:
        return True
    else:
        return False
    
if greater_than_c(values) == True:
    print(f"A + B ({values[0]})+({values[1]})) é menor que C ({values[2]})")
else:
    print(f"A + B ({values[0]})+({values[1]})) é maior que C ({values[2]})")