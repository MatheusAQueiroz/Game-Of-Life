# --------------------------- Conway's GameOfLife ---------------------------
# Autor: MatheusAlves - Github: https://github.com/MatheusAQueiroz/GameOfLife

# Variáveis de configuração
cor_ativa = (255,255,255)
cor_inativa = (0,0,0)
tamanho_grade = 10
tamanho_quadrado = 15
grossura_grade = 2
margem = 3
# Definição automática do tamanho da janela
t = (tamanho_quadrado+grossura_grade)*tamanho_grade+2*margem
(largura, altura) = t,t

# ---------------------------------------------------------------------------

# Bibliotecas
import pygame as pg
import numpy as np

# Classe com propriedades e métodos relacionados ao jogo
class gameOfLife:
    # Propriedades
    matriz = np.full((tamanho_grade, tamanho_grade),False)
    # Método construtor
    def __init__(self):
        self.matriz = np.full((tamanho_grade, tamanho_grade),True)
    # Método para desenhar a matriz na tela
    def dTela(self, surface):
        surface.fill(cor_inativa)
        for lin in range(np.size(self.matriz,0)):
            for col in range(np.size(self.matriz,1)):
                if self.matriz.item((lin,col)):
                    pg.draw.rect(surface,cor_ativa,pg.Rect(col*(tamanho_quadrado+grossura_grade)+margem,lin*(tamanho_quadrado+grossura_grade)+margem,tamanho_quadrado,tamanho_quadrado),0)
        pg.display.update()
    # Método para calcular o quadro seguinte
    def calcQuadro(self):
        matrizTemp = self.matriz.copy()
        for lin in range(np.size(self.matriz,0)):
            for col in range(np.size(self.matriz,1)):
                # Contagem de vizinhos
                c = 0
                for x in range(-1,2):
                    for y in range(-1,2):
                        if (0<=lin+x<np.size(self.matriz,0)) and (0<=col+y<np.size(self.matriz,1)) and (not (x,y) == (0,0)) and self.matriz.item((lin+x,col+y)):
                            c += 1
                if self.matriz.item((lin,col)):
                    if (c > 3 or c < 2):
                        np.put(matrizTemp,col+(lin*tamanho_grade),False,mode='clip')
                elif (c == 3):
                    np.put(matrizTemp,matrizTemp,col+(lin*tamanho_grade),True)     
        self.matriz = matrizTemp.copy()
               
# ---------------------------------------------------------------------------

# Definição da pygame.Surface (Janela do windows)
tela = pg.display.set_mode((largura,altura))

# ---------------------------------------------------------------------------

# Instanciação
jogo = gameOfLife()
jogo.dTela(tela)

jogo.calcQuadro()
jogo.dTela(tela)

# ---------------------------------------------------------------------------

# Mantém a janela aberta até o 'X' ser apertado
rodando = True
while rodando:
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            rodando = False