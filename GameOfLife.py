import pygame

# Definição das coordenadas da tela
(largura, altura) = 600, 600
tela = pygame.display.set_mode((largura,altura))

# Mantém a janela aberta
rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False           

