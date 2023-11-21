import pygame
pygame.init
tamanho = (509,360)
branco = (255,255,255)
preto = (0,0,0)
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
fundo = pygame.image.load('fundo.jpg')
pygame.display.set_caption('Space Discovery')
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    tela.blit(fundo, (0,0))
    pygame.display.update()
    clock.tick(60)