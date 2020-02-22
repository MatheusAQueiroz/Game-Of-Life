# --------------------------- Conway's GameOfLife ---------------------------
# Autor: MatheusAlves - Github: https://github.com/MatheusAQueiroz/GameOfLife
# Variáveis de configuração
(largura, altura) = 600, 600
cor_ativa = (255,255,255)

# ---------------------------------------------------------------------------

# Bibliotecas
import pygame  
import numpy   

# Classe com métodos relacionados ao jogo em si
class gameOfLife:
    # Método construtor
    def __init__(self,tamanho_grade):
        matriz = numpy.fill((self.tamanho_grade, self.tamanho_grade),True)
    # 


# Definição das coordenadas da tela
tela = pygame.display.set_mode((largura,altura))

# Mantém a janela aberta até o X ser apertado
rodando = True
while rodando:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False


