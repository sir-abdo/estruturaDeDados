#inserção
#   basta um único passo, insiro o novo dado na primeira célula vaga do vetor
#   a célula vaga será a o tamanho do vetor + 1 (ou seja, insere no final do vetor)
#   big-O constante -> O(1)

#pesquisa lienar
#   percorre cada posição do vetor, do item 0 ao último
#   melhor caso: ser o primeiro elemento do vetor
#   pior caso: ser o último elemento do vetor
#   em média: metade dos itens devem ser examinados (N/2)
#   big-O linear -> O(n)

#exclusão
    #exclui o elemento, remaneja os valores que estavam atrás dele para ocupar sua posição
    #passos
        #pesquisar uma média de N/2 elementos (pesquisa linear)
            #pior caso: N
        #mover elementos restantes (N/2 passos)
            #pior caso: N
    #Big-o -> O(2n) = O(n)

import numpy as np

class VetorNaoOrdenado:
    def __init__(self, capacidade): #capacidade é a quantidade maxima de elementos suportados pelo vetor, mas pode ser preenchido com menos elementos
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int) #valores é inicializado vazio e é definido que só receberá valores inteiros 
    
    # big O =  O(n) -> pois percorre todo o vetor
    def imprime(self):
        if self.ultima_posicao == -1:
            print('Vetor vazio')
        else:
            for i in range(self.ultima_posicao + 1): 
                print(i, '->', self.valores[i])

    #big O = O(1) -> executa apenas 1 passo, é um função constante, independe do valor passado no parametro
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima foi atingida')
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor

    #Big(0) = O(0)
    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i
        return -1

    # big O =  O(n) -> pois percorre todo o vetor
    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1: #posicao não existe
            return -1
        for i in range(posicao, self.ultima_posicao):
            self.valores[i] = self.valores[i+1] #faz o remanejamento dos elementos que estava atrás do que foi excluido (sobrescreve ele)

        self.ultima_posicao -=  1


vetor = VetorNaoOrdenado(5)
vetor.insere(2)
vetor.insere(3)
vetor.insere(5)
vetor.insere(8)
vetor.insere(1)

vetor.imprime()

print(vetor.pesquisar(8))

vetor.excluir(5)

vetor.imprime()
