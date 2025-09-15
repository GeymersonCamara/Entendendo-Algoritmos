#Exemplo para situação da vida real
#Algoritmo para encontrar uma chave
#Nesse algoritmo eu encontro uma caixa com outras caixas dentro e preciso encontrar uma chave que vai abrir uma maleta

def procure_pela_chave(caixa_principal):
    pilha = main_box.crie_uma_pilha_para_busca()
    while pilha is not vazia:
        caixa = pilha.pegue_caixa()
        for item in caixa:
            if item.e_uma_caixa():
                pilha.append(item)
            elif item.e_uma_chave():
                print("achei a chave")