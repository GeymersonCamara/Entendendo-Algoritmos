def buscaMenor(arr): #vai receber o arrey como parametro.
    menor = arr[0] #A variavel "menor" vai receber o item posicionado no indice 0.
    menor_indice = 0
    for i in range(1, len(arr)): #loop para percorrer os indices do arrey.
        if arr[i] < menor: #verifica se o item no indice [i] é menor que o atual.
            menor = arr[i] #se for, então vai ser atualizado na variavel menor.
            menor_indice = i
    return menor_indice #retorna toda a operação.

def ordenacaoPorSelecao(arr):
    novoArr = [] #arrey vazio.
    for i in range(len(arr)): #loop para percorrer o indice do arrey.
        menor = buscaMenor(arr) #essa variavel "menor" vai receber o valor encontrado na função "buscarMenor".
        novoArr.append(arr.pop(menor))
    return novoArr

print(ordenacaoPorSelecao([5, 3, 6, 2, 10, 1]))