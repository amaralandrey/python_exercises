"""
1) Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C.
"""

values = [] # os índices representam a ordem alfabética.
labels = ["A", "B", "C"]

def less_than_c(array):
    """ Esta função avalia se a soma de A + B é menor que C """
    if array[0] + array[1] < array[2]:
        return True
    else:
        return False

i = 0
while i < 3:
    try:
        valor = int(input(f"Informe o valor de {labels[i]}: "))
        values.append(valor)
        i += 1
    except ValueError:
        print("Valor inválido!")
    
if less_than_c(values) == True:
    print(f"A + B ({values[0]} + {values[1]}) é menor que C ({values[2]}).")
else:
    print(f"A + B ({values[0]} + {values[1]}) não é menor que C ({values[2]}).")