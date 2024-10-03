import pygame
import sys

# Inicializa o Pygame
pygame.init()

# ConfiguraÃ§Ãµes da tela
largura, altura = 640, 480
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pong")

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# ConfiguraÃ§Ãµes das barras e da bola
largura_barra, altura_barra = 10, 100
largura_bola, altura_bola = 10, 10
velocidade_bola = [3, 3]

# PosiÃ§Ãµes iniciais
posicao_barra_esquerda = [10, (altura - altura_barra) // 2]
posicao_barra_direita = [largura - 20, (altura - altura_barra) // 2]
posicao_bola = [largura // 2, altura // 2]

# Velocidade das barras
velocidade_barra = 5
movimento_barra_esquerda = 0
movimento_barra_direita = 0

# PontuaÃ§Ã£o
pontuacao_esquerda = 0
pontuacao_direita = 0

# Fonte
fonte = pygame.font.SysFont(None, 55)


def desenha_elementos():
    tela.fill(preto)
    pygame.draw.rect(
        tela, branco, (*posicao_barra_esquerda, largura_barra, altura_barra)
    )
    pygame.draw.rect(
        tela, branco, (*posicao_barra_direita, largura_barra, altura_barra)
    )
    pygame.draw.ellipse(tela, branco, (*posicao_bola, largura_bola, altura_bola))
    pygame.draw.aaline(tela, branco, (largura // 2, 0), (largura // 2, altura))

    # Renderiza a pontuaÃ§Ã£o
    texto_esquerda = fonte.render(str(pontuacao_esquerda), True, branco)
    texto_direita = fonte.render(str(pontuacao_direita), True, branco)
    tela.blit(texto_esquerda, (largura // 4, 20))
    tela.blit(texto_direita, (3 * largura // 4, 20))


def atualiza_bola():
    global posicao_bola, velocidade_bola, pontuacao_esquerda, pontuacao_direita

    posicao_bola[0] += velocidade_bola[0]
    posicao_bola[1] += velocidade_bola[1]

    if posicao_bola[1] <= 0 or posicao_bola[1] >= altura - altura_bola:
        velocidade_bola[1] = -velocidade_bola[1]

    if posicao_bola[0] <= posicao_barra_esquerda[0] + largura_barra:
        if (
            posicao_barra_esquerda[1]
            < posicao_bola[1]
            < posicao_barra_esquerda[1] + altura_barra
        ):
            velocidade_bola[0] = -velocidade_bola[0]
        else:
            pontuacao_direita += 1
            reinicia_jogo()

    if posicao_bola[0] >= posicao_barra_direita[0] - largura_bola:
        if (
            posicao_barra_direita[1]
            < posicao_bola[1]
            < posicao_barra_direita[1] + altura_barra
        ):
            velocidade_bola[0] = -velocidade_bola[0]
        else:
            pontuacao_esquerda += 1
            reinicia_jogo()


def reinicia_jogo():
    global posicao_bola, velocidade_bola
    posicao_bola = [largura // 2, altura // 2]
    velocidade_bola = [3, 3]


# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_w:
                movimento_barra_esquerda = -velocidade_barra
            if evento.key == pygame.K_s:
                movimento_barra_esquerda = velocidade_barra
            if evento.key == pygame.K_UP:
                movimento_barra_direita = -velocidade_barra
            if evento.key == pygame.K_DOWN:
                movimento_barra_direita = velocidade_barra
        if evento.type == pygame.KEYUP:
            if evento.key in (pygame.K_w, pygame.K_s):
                movimento_barra_esquerda = 0
            if evento.key in (pygame.K_UP, pygame.K_DOWN):
                movimento_barra_direita = 0

    posicao_barra_esquerda[1] += movimento_barra_esquerda
    posicao_barra_direita[1] += movimento_barra_direita

    posicao_barra_esquerda[1] = max(
        0, min(posicao_barra_esquerda[1], altura - altura_barra)
    )
    posicao_barra_direita[1] = max(
        0, min(posicao_barra_direita[1], altura - altura_barra)
    )

    atualiza_bola()
    desenha_elementos()

    pygame.display.flip()
    pygame.time.Clock().tick(60)
