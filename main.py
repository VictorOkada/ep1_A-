import numpy as np
import random
import math
from random import randint

class Jogo:
  def __init__(self):
    self.estado = []

  def utilidade(self, posicao):   
    if posicao == "T":
        return 1
    elif posicao == "A":
        return 3
    elif posicao == "M":
        return 6
    else:
        return 0

  def sucesso(self, posicao, posicao_final):      
    if posicao == posicao_final:
      print("Você atingiu o objetivo!")
    else:
      print("Você ainda não atingiu o objetivo!")
    
  def Heuristica(self, p_xa, p_xb, p_ya, p_yb, opcao1, opcao2, opcao3):
    A = [opcao1, opcao2, opcao3]
    for index,x in enumerate(A):
      xa = x
      xb = p_xb
      ya = p_ya
      yb = p_yb
      distancia_euclidiana = math.sqrt(
          pow((xa - xb), 2) + pow((ya - yb), 2))
      distancia_manhattan = abs((xa - xb)) + abs((ya - yb))

      if index == 0:
        distE1 = distancia_euclidiana
        distM1 = distancia_manhattan
      elif index == 1:
        distE2 = distancia_euclidiana
        distM2 = distancia_manhattan
      elif index == 2:
        distE3 = distancia_euclidiana
        distM3 = distancia_manhattan

    if ((distE1 < distE2 and distM1 < distM2)):
      return opcao1
      
    elif ((distE2 < distE3 and distM2 < distM3)):
      return opcao2
      
    else:
      return opcao3
  
      # print("A distancia Euclidiana atual:", distancia_euclidiana)
      # print("A distancia de Manhattan atual:", distancia_manhattan)

  def fim_de_jogo(self, posicao_atual, posicao_final):
    if posicao_atual == posicao_final:
      print("Fim de jogo!")
      
  def jogar(self, estado = None):
    if (estado is None):
      m = randint(3, 10)
      n = randint(3, 10)
      print("linhas:", m) 
      print("colunas", n) 
      lista_valores = ["B","M","T","A"]
      
      matrizA = list()
      for c in range(1, m + 1):
        linha = list()
        for i in range(1, n + 1):
            while True:
              self.estado = random.choice(lista_valores)
              break
            linha.append(self.estado)
        matrizA.append(linha)
        
      matriz = np.array(matrizA)
      print(matriz)
      
      print("\n\n")
      total = n * m
      somaTotal = 0
      prox = 0
      for i in range(0, total):
        try:
          if i == m or i == n + m or i == n + m + n:
            i = prox
            p = [matriz.item(i - 1), matriz.item(i + n - 1), matriz.item(i + n)]
            cont = 0    
            contadorT = False
            for item in enumerate(p):
              if "T" in item:
                  cont = cont + 1
                  
              if (cont == 1 and p[0] == "T") or (cont == 1 and p[1] == "T") or (cont == 1 and p[2] == "T") or (cont == 2 and p[0] == "T") or (cont == 2 and p[1] == "T") or (cont == 2 and p[2] == "T") or (cont == 3 and p[0] == "T") or (cont == 3 and p[1] == "T") or (cont == 3 and p[2] == "T"):
                soma = 0
                ponto = j.utilidade('T')
                soma = ponto
                somaTotal = somaTotal + soma
                contadorT = True
                contadorA = True
                contadorM = True
                opcao1 = i - 1
                opcao2 = i + n - 1
                opcao3 = i + n
                posicao_xa = 0
                posicao_xb = total - 1
                posicao_ya = m
                posicao_yb = 0  
                distancia = j.Heuristica(posicao_xa, posicao_xb, posicao_ya, posicao_yb, opcao1, opcao2, opcao3)
                prox = distancia
                j.sucesso(prox, total - 1)
                
              else:
                  contadorT = False
      
              if contadorT == False:
                  contadorA = False
                  for item in enumerate(p):
                      if "A" in item:
                          cont = cont + 1
        
                  if (cont == 1 and p[0] == "A") or (cont == 1 and p[1] == "A") or (cont == 1 and p[2] == "A") or (cont == 2 and p[0] == "A") or (cont == 2 and p[1] == "A") or (cont == 2 and p[2] == "A") or (cont == 3 and p[0] == "A") or (cont == 3 and p[1] == "A") or (cont == 3 and p[2] == "A"):
                    soma = 0
                    ponto = j.utilidade("A")
                    soma = ponto
                    somaTotal = somaTotal + soma
                    contadorA = True
                    contadorM = True
                    opcao1 = i - 1
                    opcao2 = i + n - 1
                    opcao3 = i + n
                    #prox = i - 1
                    posicao_xa = 0
                    posicao_xb = total - 1
                    posicao_ya = m
                    posicao_yb = 0  
                    distancia = j.Heuristica(posicao_xa, posicao_xb, posicao_ya, posicao_yb, opcao1, opcao2, opcao3)
                    prox = distancia
                    j.sucesso(prox, total - 1)
                      
                  else:
                    contadorA = False
        
              if contadorA == False:
                  contadorM = False
                  for item in enumerate(p):
                    if "M" in item:
                        cont = cont + 1
        
                  if (cont == 1 and p[0] == "M") or (cont == 1 and p[1] == "M") or (cont == 1 and p[2] == "M") or (cont == 2 and p[0] == "M") or (cont == 2 and p[1] == "M") or (cont == 2 and p[2] == "M") or (cont == 3 and p[0] == "M") or (cont == 3 and p[1] == "M") or (cont == 3 and p[2] == "M"):
                    soma = 0
                    ponto = j.utilidade("M")
                    soma = ponto
                    somaTotal = somaTotal + soma
                    opcao1 = i - 1
                    opcao2 = i + n - 1
                    opcao3 = i + n
                    contadorM = True
                    posicao_xa = 0
                    posicao_xb = total - 1
                    posicao_ya = m
                    posicao_yb = 0  
                    distancia = j.Heuristica(posicao_xa, posicao_xb, posicao_ya, posicao_yb, opcao1, opcao2, opcao3)
                    prox = distancia
                    j.sucesso(prox, total - 1)
                
                  else:
                      contadorM = False
                    
              if contadorM == False:
                j.fim_de_jogo(prox, total-1)
                return 0
                
              print("Posição Tabuleiro:", prox)
              print("Pontuação total:", somaTotal)
            
          else:

            i = prox
            p = [matriz.item(i + 1), matriz.item(i + n), matriz.item(i + n + 1)]
            cont = 0    
            contadorT = False
            
            for item in enumerate(p):
                if "T" in item:
                    cont = cont + 1
                  
            if (cont == 1 and p[0] == "T") or (cont == 1 and p[1] == "T") or (cont == 1 and p[2] == "T") or (cont == 2 and p[0] == "T") or (cont == 2 and p[1] == "T") or (cont == 2 and p[2] == "T") or (cont == 3 and p[0] == "T") or (cont == 3 and p[1] == "T") or (cont == 3 and p[2] == "T"):

              soma = 0
              ponto = j.utilidade("T")
              soma = ponto
              somaTotal = somaTotal + soma
              contadorT = True
              contadorA = True
              contadorM = True
              opcao1 = i + 1
              opcao2 = i + n
              opcao3 = i + n + 1
              posicao_xa = 0
              posicao_xb = total - 1
              posicao_ya = m
              posicao_yb = 0                  
              distancia = j.Heuristica(posicao_xa, posicao_xb, posicao_ya, posicao_yb, opcao1, opcao2, opcao3)
              prox = distancia
              j.sucesso(prox, total - 1)
  
            else:
                contadorT = False
      
            if contadorT == False:
                contadorA = False
                for item in enumerate(p):
                    if "A" in item:
                        cont = cont + 1
      
                if (cont == 1 and p[0] == "A") or (cont == 1 and p[1] == "A") or (cont == 1 and p[2] == "A") or (cont == 2 and p[0] == "A") or (cont == 2 and p[1] == "A") or (cont == 2 and p[2] == "A") or (cont == 3 and p[0] == "A") or (cont == 3 and p[1] == "A") or (cont == 3 and p[2] == "A"):
                  
                  soma = 0
                  ponto = j.utilidade("A")
                  soma = ponto
                  somaTotal = somaTotal + soma
                  contadorA = True
                  contadorM = True
                  opcao1 = i + 1
                  opcao2 = i + n
                  opcao3 = i + n + 1
                  posicao_xa = 0
                  posicao_xb = total - 1
                  posicao_ya = m
                  posicao_yb = 0                  
                  distancia = j.Heuristica(posicao_xa, posicao_xb, posicao_ya, posicao_yb, opcao1, opcao2, opcao3)
                  prox = distancia
                  j.sucesso(prox, total - 1)

                else:
                  contadorA = False
      
            if contadorA == False:
                contadorM = False
                for item in enumerate(p):
                    if "M" in item:
                        cont = cont + 1
      
                
                    if (cont == 1 and p[0] == "M") or (cont == 1 and p[1] == "M") or (cont == 1 and p[2] == "M") or (cont == 2 and p[0] == "M") or (cont == 2 and p[1] == "M") or (cont == 2 and p[2] == "M") or (cont == 3 and p[0] == "M") or (cont == 3 and p[1] == "M") or (cont == 3 and p[2] == "M"):
                      soma = 0
                      ponto = j.utilidade("M")
                      soma = ponto
                      somaTotal = somaTotal + soma
                      opcao1 = i + 1
                      opcao2 = i + n
                      opcao3 = i + n + 1
                      posicao_xa = 0
                      posicao_xb = total - 1
                      posicao_ya = m
                      posicao_yb = 0                  
                      distancia = j.Heuristica(posicao_xa, posicao_xb, posicao_ya, posicao_yb, opcao1, opcao2, opcao3)
                      prox = distancia
                      j.sucesso(prox, total - 1)
               
                else:
                    contadorM = False
                  
            if contadorM == False:
              j.fim_de_jogo(prox, total-1)
              return 0
              
            print("Posição Tabuleiro:", prox)
            print("Pontuação total:", somaTotal)
            
        except:
          #print(inst)
          print("Você atingiu uma barreira!")
          j.fim_de_jogo(prox, total)
          return 0
          
j = Jogo()
j.jogar()