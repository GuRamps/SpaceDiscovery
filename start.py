from extençoes import*

pygame.init()
tamanho = (683,384)
branco = (255,255,255)
preto = (0,0,0)
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
fundo = pygame.image.load('fundo.jpg')
pygame.display.set_caption('Space Discovery')

rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_F10:
                with open("Pontos 1", "wb") as arquivo:
                    pickle.dump(estrelas, arquivo)
            elif event.key == pygame.K_F11:
                try:
                    with open("Pontos 1", "wb") as arquivo:
                        estrelas = pickle.load(arquivo)
                    print("Estrela Armazenada")
                except FileNotFoundError:
                    print("Estrela não encontrada")
            elif event.key == pygame.K_F12:
                estrelas = []
                print("Estrela Deletada")
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            item = simpledialog.askstring("Space", "Nome da Estrela:")
            print(item)
            if item == None:
                item = "desconhecido"+str(pos)
            estrelas[item] = pos
    tela.blit(fundo, (0,0))
    pygame.display.update()
    clock.tick(60)