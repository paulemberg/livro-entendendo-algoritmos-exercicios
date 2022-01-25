import math

def pesquisa_binaria(lista, item):
    
    baixo = 0
    alto = len(lista) - 1
    
    while baixo <= alto:
        meio = math.trunc((baixo + alto) / 2)
        chute = lista[meio]
        if chute == item:
            return meio        
        if chute > item:
            alto = meio - 1 
        else:
            baixo = meio + 1
    return None


def quantidade_etapas_de_pesquisa(items):
    divisor = 2
    etapa_fininal = 0
    contador = -1
    valor_divido = items
    while  valor_divido > etapa_fininal:
        valor_divido = math.trunc(items / divisor)
        contador += 1        
        if valor_divido == etapa_fininal:
            return contador
        else:
            items = valor_divido



minha_lista = [1,3,5,7,9]

print('O valor está no indíce: ' + str(pesquisa_binaria(minha_lista, 3)))
print('O valor está no indíce: ' + str(pesquisa_binaria(minha_lista, -1)))

print('Iterações necessárias: ' +  str(quantidade_etapas_de_pesquisa(256)))

