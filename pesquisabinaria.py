# para qdo se tem vetores ordenados, pois utiliza a pesquisa linear (percorre elemento por elemento)
#faz um divisão do vetor por 2 a cada vez que faz uma busca

#algoritmo:
#numeros de 1 a 100
#pesquisar numero 47

#1 ate 100/2 = 50
# 50 é o numero pesquisado? Não
# 47 é menor ou maior que 50? Menor

#1 ate 49/2 = 25
# 25 é o numero pesquisado? Não
# 47 é menor ou maior que 25? Maior

#26 ate 49/2 = 38
# 26 é o numero pesquisado? Não
# 47 é menor ou maior que 38? Maior

#39 ate 49/2 = 44
# 44 é o numero pesquisado? Não
# 47 é menor ou maior que 44? Maior

#45 ate 49/2 = 47
# 25 é o numero pesquisado? Sim


import numpy as np

class VetorOrdenado:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    # O(n)
    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i]) #mostra a posição e o respectivo valor
    # O(n)
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return

        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i+1

        x = self.ultima_posicao
        while x >= posicao: #remaneja os valores no array para uma posicação a frente, uma vez que o novo valor vai ser inserido
            self.valores[x+1] = self.valores[x]
            x -= 1

        self.valores[posicao] = valor
        self.ultima_posicao += 1
    
    #O (log n)
    def pesquisa_binaria(self, valor):
        limite_inferior = 0
        limite_superior = self.ultima_posicao

        while True:
            posicao_atual = int((limite_inferior + limite_superior) / 2)
            #se achou na primeira tentativa
            if self.valores[posicao_atual] == valor:
                return posicao_atual
            #se não achou
            elif limite_inferior > limite_superior:
                return -1
            #divide os limites
            else:
                if self.valores[posicao_atual] < valor:
                    limite_inferior = posicao_atual + 1
                else:
                    limite_superior = posicao_atual - 1


vetor = VetorOrdenado(10)
#vetor.imprime()

vetor.insere(6)
#vetor.imprime()

vetor.insere(4)
#vetor.imprime()
 
vetor.insere(3)
#vetor.imprime()

vetor.insere(5)
vetor.imprime()

print(vetor.pesquisa_binaria(5)) #retorna 2 (posicao no vetor)

#vetor.excluir(5)
#vetor.imprime()