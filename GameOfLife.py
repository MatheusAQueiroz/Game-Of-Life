# --------------------------- Conway's GameOfLife ---------------------------
# Autor: MatheusAlves - Github: https://github.com/MatheusAQueiroz/GameOfLife
# Variáveis de configuração

cor_ativa = (255,255,255,255)
tamanho_grade = 100
tamanho_quadrado = 5
grossura_grade = 1
margem = 3

t = (tamanho_quadrado+grossura_grade)*tamanho_grade+2*margem
(largura, altura) = t,t

# ---------------------------------------------------------------------------

# Bibliotecas
import pygame as pg
import numpy  as np

# Classe com propriedades e métodos relacionados ao jogo
class gameOfLife:
    # Propriedades
    matriz = np.full((tamanho_grade, tamanho_grade),False)
    # Método construtor
    def __init__(self):
        self.matriz = np.full((tamanho_grade, tamanho_grade),True)
    # Método de desenhar a matriz na tela
    def dTela(self, surface):
        for lin in range(np.size(self.matriz,0)):
            for col in range(np.size(self.matriz,1)):
                if self.matriz.item((lin,col)):
                    pg.draw.rect(surface,cor_ativa,pg.Rect(margem+lin*(tamanho_quadrado+grossura_grade),margem+col*(tamanho_quadrado+grossura_grade),tamanho_quadrado,tamanho_quadrado),0)
        pg.display.update()
        
# ---------------------------------------------------------------------------

# Definição da pygame.Surface (Janela do windows)
tela = pg.display.set_mode((largura,altura))

# ---------------------------------------------------------------------------

# Instanciação
jogo = gameOfLife()

jogo.dTela(tela)

# ---------------------------------------------------------------------------

# Mantém a janela aberta até o 'X' ser apertado
rodando = True
while rodando:
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            rodando = False