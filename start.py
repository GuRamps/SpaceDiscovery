from extençoes import*

pygame.init()

# Configurações
tamanho = (800, 500)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Space Discovery")
clock = pygame.time.Clock()

# Carregar imagens e músicas
try:
    fundo = pygame.image.load("fundo.jpg")
except pygame.error:
    fundo = pygame.Surface(tamanho)
    fundo.fill((0, 0, 0))

try:
    pygame.mixer.music.load("Space_Machine_Power.mp3")
    pygame.mixer.music.play(-1)
except pygame.error:
    print("Erro ao carregar o arquivo de áudio")

try:
    icone = pygame.image.load("space.png")
    pygame.display.set_icon(icone)
except pygame.error:
    print("Erro ao carregar o ícone")

# Inicializar variáveis
estrelas = []
fonte_letra = pygame.font.Font(None, 20)
tamanho_da_letra = 20

# Textos e posições
texto_opcoes = [
    ("Pressione F10 para Salvar os Pontos", (1, 1)),
    ("Pressione F11 para Carregar os Pontos", (1, 15)),
    ("Pressione F12 para Deletar os Pontos", (1, 30)),
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_F10:
                with open("pontos_estrelas.pkl", "wb") as arquivo:
                    pickle.dump(estrelas, arquivo)
                print("Pontos salvos!")
            elif event.key == pygame.K_F11:
                try:
                    with open("pontos_estrelas.pkl", "rb") as arquivo:
                        estrelas = pickle.load(arquivo)
                    print("Pontos carregados!")
                except FileNotFoundError:
                    print("Arquivo de pontos não encontrado.")
            elif event.key == pygame.K_F12:
                estrelas = []
                print("Pontos deletados.")
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            pos = pygame.mouse.get_pos()
            item = simpledialog.askstring("Space", "Nome da Estrela:")
            item = item if item else "desconhecidos"
            estrelas.append((pos, item))

    # Desenhar na tela
    tela.blit(fundo, (0, 0))

    # Renderizar textos
    for texto, posicao in texto_opcoes:
        texto_renderizado = fonte_letra.render(texto, True, (255, 255, 255))
        tela.blit(texto_renderizado, posicao)

    # Desenhar estrelas e calcular distâncias
    for i in range(len(estrelas) - 1):
        ponto_atual = estrelas[i][0]
        proximo_ponto = estrelas[i + 1][0]
        pygame.draw.line(tela, (255, 255, 255), ponto_atual, proximo_ponto)

        distancia_x = abs(proximo_ponto[0] - ponto_atual[0])
        distancia_y = abs(proximo_ponto[1] - ponto_atual[1])
        soma_distancias = distancia_x + distancia_y

        posicao_texto_distancias = (
            (ponto_atual[0] + proximo_ponto[0]) // 2,
            (ponto_atual[1] + proximo_ponto[1]) // 2 - 20,
        )
        texto_distancias = f"Distância: {soma_distancias}"
        texto_renderizado = fonte_letra.render(texto_distancias, True, (255, 255, 255))
        tela.blit(texto_renderizado, posicao_texto_distancias)

# Desenhar marcadores
    for pos, item in estrelas:
        pygame.draw.circle(tela, (95, 96, 97), pos, 5)


    pygame.display.update()
    clock.tick(60)

pygame.quit()
