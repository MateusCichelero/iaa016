#Desenvolvido em Python por Mateus Cichelero da Silva


#Escreva a função triangular que receberá um parâmetro d indicando o tamanho da vizinha,
#a função deverá retornar um vetor com 2d+1 graus de pertinência para a vizinhança d.

def triangular_fuzzy(d):
    delta = 1/d #distancia entre graus de pertinencia dos vizinhos, considerando valor máximo de graus de pertinencia como =1 no centro do triangulo e minimo =0 nos vizinhos das extremidades
    metade = [round(0 + index_vizinho*delta,2) for index_vizinho in range(d)]
    lista_graus_pertinencia = metade + [1] + metade[::-1] #aproveita-se propriedade simétrica entre metades do triangulo
    return lista_graus_pertinencia

#exemplo de aplicação
triangular_fuzzy(5)
#[0.0, 0.2, 0.4, 0.6, 0.8, 1, 0.8, 0.6, 0.4, 0.2, 0.0]