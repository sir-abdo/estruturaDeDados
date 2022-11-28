#Dados ordenados em orden ascendente
#Vantagem: agiliza os tempos de pesquisa
#inserção
    #passos:
        # 1) pesquisa linear
                #média: N/2 elementos
                #pior caso: N (percorre todos os elementos)
        # 2) mover os elementos restantes (N/2 passos)
                #pior caso: N 
    #Big-O -> O(2n) = O(n)

#pesquisa linear
    #como o vetor está ordenado, a busca acaba qdo o primeiro item maior q o valor de pesquisa é atingido
    #pior caso: se elemento não estiver no vetor ou se estiver na última posição
    #Big O -> O(n)
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

    # O(n)
    def pesquisar(self, valor):
      for i in range(self.ultima_posicao + 1):
        if self.valores[i] > valor:
            return -1 #elemento não existe
        if self.valores[i] == valor:
            return i #retorna posicao

    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i+1]
            self.ultima_posicao -= 1

      
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

print(vetor.pesquisar(5)) #retorna 2 (posicao no vetor)

vetor.excluir(5)
vetor.imprime()