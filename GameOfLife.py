# --------------------------- Conway's GameOfLife ---------------------------
# Autor: MatheusAlves - Github: https://github.com/MatheusAQueiroz/GameOfLife

# Variáveis de configuração
cor_ativa = (255,255,0)
cor_inativa = (100,100,100)
cor_grade = (150,150,150)
tamanho_grade = 75
tamanho_quadrado = 8
grossura_grade = 1
margem = 0
freq = 8
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
    geracao = 0
    matriz = np.full((tamanho_grade, tamanho_grade),False)
    # Método construtor
    def __init__(self):
        self.matriz = np.full((tamanho_grade, tamanho_grade),False)
        self.geracao = 0
    # Método para desenhar a matriz na tela
    def dTela(self, surface):
        surface.fill(cor_grade)
        for lin in range(np.size(self.matriz,0)):
            for col in range(np.size(self.matriz,1)):
                pg.draw.rect(surface,cor_inativa,pg.Rect(col*(tamanho_quadrado+grossura_grade)+margem,lin*(tamanho_quadrado+grossura_grade)+margem,tamanho_quadrado,tamanho_quadrado),0)
                if self.matriz.item((lin,col)):
                    pg.draw.rect(surface,cor_ativa,pg.Rect(col*(tamanho_quadrado+grossura_grade)+margem,lin*(tamanho_quadrado+grossura_grade)+margem,tamanho_quadrado,tamanho_quadrado),0)
        pg.display.update()
    # Método para calcular o quadro seguinte
    def calcQuadro(self):
        self.geracao += 1
        iniciado = False
        matrizTemp = self.matriz.copy()
        for lin in range(np.size(self.matriz,0)):
            for col in range(np.size(self.matriz,1)):
                # Contagem de vizinhos
                c = 0
                #if self.matriz.item((lin,col)) or iniciado:
                #    iniciado = True
                #    lin -= 1
                #    col -= 1
                for x in range(-1,2):
                    for y in range(-1,2):
                        if (0<=lin+x<np.size(self.matriz,0)) and (0<=col+y<np.size(self.matriz,1)) and not (x == 0 and y == 0 ) and self.matriz.item((lin+x,col+y)):
                            c += 1
                # Mata células por solidão ou superpopulação
                if self.matriz.item((lin,col)):
                    if (c > 3 or c < 2) or (lin == 0) or (col == 0) or (lin == np.size(self.matriz,0)-1) or (col == np.size(self.matriz,1)-1):
                        np.put(matrizTemp,col+(lin*tamanho_grade),False)
                # Revive células com exatamente 3 vizinhos
                elif c == 3:
                    np.put(matrizTemp,col+(lin*tamanho_grade),True)     
        self.matriz = matrizTemp.copy()
        jogo.dTela(tela)
               
# ---------------------------------------------------------------------------

# Definição da pygame.Surface (Janela do windows) e nome da janela
tela = pg.display.set_mode((largura,altura))
pg.display.set_caption('Conway\'s Game of Life')

# Evento de passagem do tempo
clk = pg.time.Clock()

# Instanciação
jogo = gameOfLife()

# Starter
np.put(jogo.matriz,[2+tamanho_grade*1,3+tamanho_grade*2,1+tamanho_grade*3,2+tamanho_grade*3,3+tamanho_grade*3],True)

# ---------------------------------------------------------------------------

# Mantém a janela aberta até o 'X' ser apertado
rodando = True
while rodando:
    for event in pg.event.get():
        # Evento de saída
        if event.type == pg.QUIT:
            rodando = False
        clk.tick()
        jogo.calcQuadro()
