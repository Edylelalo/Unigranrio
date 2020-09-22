# -*- coding: cp1252 -*-

import pygame
import math
import random
import time

#Iniciando o Jogo
pygame.init()

#Criando a tela do Jogo
screen = pygame.display.set_mode((800, 600))

#Nome e Ícone
pygame.display.set_caption("Survive Covid")
icon = pygame.image.load('Imagens/icon.png')
pygame.display.set_icon(icon)

#Background
background = pygame.image.load('Imagens/background.png')

#Primeiras Variáveis
current_time = 0
vida_value = 10
multiplicador = 1
combo_value = 0
score_value = 0
walkCount = 0
esquerda = False
direita = False
movendo = False
andar_direita = (pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'))
andar_esquerda = (pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'))

#Fonte
font = pygame.font.Font('PixelOperatorSC.ttf', 32)

#Posição da Interface
scoreX = 10
scoreY = 30
vidaX = 10
vidaY = 5
comboX = 10
comboY = 55

#Upload de Imagens e Movimentação
playerImg = pygame.image.load('PR.png')
playerImg = pygame.transform.scale(playerImg, (50, 50))
playerX = 400
playerY = 480
playerX_change = 0

feijaoImg = pygame.image.load('Imagens/feijao.png')
feijaoImg = pygame.transform.scale(feijaoImg, (50, 50))
feijaoX = random.randint(0, 700)
feijaoY = -60
feijaoY_change = 1.0

arrozImg = pygame.image.load('Imagens/arroz.png')
arrozImg = pygame.transform.scale(arrozImg, (50, 50))
arrozX = random.randint(0, 700)
arrozY = -3000
arrozY_change = 1.3

gelImg = pygame.image.load('Imagens/gel.png')
gelImg = pygame.transform.scale(gelImg, (50, 50))
gelX = random.randint(0, 700)
gelY = -6000
gelY_change = 1.6

virusImg = pygame.image.load('Imagens/covid.png')
virusImg = pygame.transform.scale(virusImg, (50, 50))
virusX = random.randint(0, 700)
virusY = -4000
virusY_change = 1.8

#Definindo como Visível
def show_score(x, y):
    score = font.render("Pontos: " + str(score_value), True, (0, 0, 0))
    screen.blit(score, (x, y))


def show_vida(x, y):
    vida = font.render("Vida: " + str(vida_value), True, (0, 0, 0))
    screen.blit(vida, (x, y))


def show_combo(x, y):
    combo = font.render("Combo: x" + str(multiplicador), True, (0, 0, 0))
    screen.blit(combo, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))


def feijao(x, y):
    screen.blit(feijaoImg, (x, y))


def arroz(x, y):
    screen.blit(arrozImg, (x, y))


def gel(x, y):
    screen.blit(gelImg, (x, y))


def virus(x, y):
    screen.blit(virusImg, (x, y))

#Colisões entre Itens
def isCollisionFeijao(playerX, playerY, feijaoX, feijaoY):
    distance = math.sqrt((math.pow(playerX - feijaoX, 2)) + (math.pow(playerY - feijaoY, 2)))
    if distance < 65:
        return True
    else:
        return False


def isCollisionArroz(playerX, playerY, arrozX, arrozY):
    distance = math.sqrt((math.pow(playerX - arrozX, 2)) + (math.pow(playerY - arrozY, 2)))
    if distance < 65:
        return True
    else:
        return False


def isCollisionGel(playerX, playerY, gelX, gelY):
    distance = math.sqrt((math.pow(playerX - gelX, 2)) + (math.pow(playerY - gelY, 2)))
    if distance < 65:
        return True
    else:
        return False


def isCollisionVirus(playerX, playerY, virusX, virusY):
    distance = math.sqrt((math.pow(playerX - virusX, 2)) + (math.pow(playerY - virusY, 2)))
    if distance < 65:
        return True
    else:
        return False

#Loop de Jogo
running = True
while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    current_time = pygame.time.get_ticks()

    feijaoY += feijaoY_change
    arrozY += arrozY_change
    gelY += gelY_change
    virusY += virusY_change
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 730:
        playerX = 730

    if combo_value >= 5:
        multiplicador = 2

    if combo_value >= 10:
        multiplicador = 4

    if combo_value >= 15:
        multiplicador = 6

    collision = isCollisionFeijao(playerX, playerY, feijaoX, feijaoY)
    if collision:
        soma_feijao = 5
        feijaoMultiplicado = multiplicador * soma_feijao
        feijaoX = random.randint(0, 770)
        feijaoY = -60
        feijaoY_change += 0.002
        score_value += feijaoMultiplicado
        combo_value += 1
        vida_value += 0

    collision = isCollisionArroz(playerX, playerY, arrozX, arrozY)
    if collision:
        soma_arroz = 10
        arrozMultiplicado = multiplicador * soma_arroz
        arrozX = random.randint(0, 700)
        arrozY = -60
        arrozY_change += 0.002
        score_value += arrozMultiplicado
        combo_value += 1
        vida_value += 0

    collision = isCollisionGel(playerX, playerY, gelX, gelY)
    if collision:
        soma_gel = 20
        gelMultiplicado = multiplicador * soma_gel
        gelX = random.randint(0, 700)
        gelY = -60
        gelY_change += 0.002
        score_value += gelMultiplicado
        combo_value += 1
        vida_value += 0

    collision = isCollisionVirus(playerX, playerY, virusX, virusY)
    if collision:
        soma_virus = 0
        virusX = random.randint(0, 700)
        virusY = -60
        virusY_change += 0.002
        combo_value = 1
        vida_value -= 1

    if feijaoY >= 600:
        feijaoX = random.randint(0, 700)
        feijaoY = -60
        feijaoY_change += 0.002
        combo_value = 0
        multiplicador = 1
        vida_value -= 0

    if arrozY >= 600:
        arrozX = random.randint(0, 770)
        arrozY = -60
        arrozY_change += 0.002
        combo_value = 0
        multiplicador = 1
        vida_value -= 0

    if gelY >= 600:
        gelX = random.randint(0, 770)
        gelY = -60
        gelY_change += 0.002
        combo_value = 0
        multiplicador = 1
        vida_value -= 0

    if virusY >= 600:
        virusX = random.randint(0, 770)
        virusY = -60
        virusY_change += 0.002
        combo_value = 0
        multiplicador = 1
        vida_value -= 0

    if current_time >= 10000:
        arroz(arrozX, arrozY)

    if current_time >= 25000:
        gel(gelX, gelY)

    if current_time >= 0:
        virus(virusX, virusY)

    if vida_value >= 10:
        vida_value = 10

    if vida_value <= 0:
        vida_value = 0

    player(playerX, playerY)
    show_score(scoreX, scoreY)
    show_combo(comboX, comboY)
    show_vida(vidaX, vidaY)
    pygame.display.update()