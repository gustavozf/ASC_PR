# -*- coding: utf-8 -*-

import cv2

# Local onde estão as imagens
img = '/home/gustavozf/Documentos/Projeto/Artigo/'

####################################################################
# nome da imagem, linha inicial, coluna inicial, coluna final, proporção
####################################################################
def mel(nome, li, ci, cf, p):

	# Função: imread ( nome da imagem, [1=cor, 0=grayscape, -1=alpha])
	imagem = cv2.imread(img + nome, 0)

	freq = [ 40, 161, 240, 404, 693, 867, 1000, 2022, 3000, 3393, 4109, 5526, 6500, 7743, 12000 ]

	# Qual a proporção para usar na imagem, aqui está 40%
	linhas = [x / 40 for x in freq]

	# Percorre cada pixel da imagem
	for l in linhas:
		# blue
		imagem[ lin_inicio-l: , ci:cf ][0] = 255
		# green
		#i[ l+lin_inicio: , col_inicio:col_fim ][1] = 255
		# red
		#i[ l+lin_inicio: , col_inicio:col_fim ][2] = 255

	# Mostrar imagem
	cv2.imshow('Mel',imagem)
	# Salvar imagem
	cv2.imwrite(img + 'spec_mel.png', imagem)

####################################################################
# zonas lineares
####################################################################
def linear(nome, li, lf, ci, cf, z):

	# Função: imread ( nome da imagem, [1=cor, 0=grayscape, -1=alpha])
	imagem = cv2.imread(img + nome, 0)

	# verificar a área da imagem
	espaco = lf - li
	# dividir o espaço disponível em zonas
	div = espaco / z
	# índice inicial pra pintar
	lin = li

	# 3 zonas, pintar 2 linhas
	for l in range(z):
		lin += div
		imagem[ lin: , ci:cf ][0] = 255

	# Mostrar imagem
	cv2.imshow('Linear',imagem)
	# Salvar imagem
	cv2.imwrite(img + 'spec_linear_' + str(z) + '.png', imagem)


####################################################################
# MAIN
####################################################################

# a imagem 0,0 começa no canto superior esquerdo
# Definir a altura que vai começar na frequência mais baixa
lin_inicio = 513

# linha final só para zonas lineares
lin_fim = 128
# quantidade de zonas
zonas = 4

# Início e fim das colunas da imagem a colorir
col_inicio = 0
col_fim = 800

# Chama a função mel
mel('exemplo.png', lin_inicio, col_inicio, col_fim, 40)
# Chama a função linear
linear('exemplo.png', lin_inicio, lin_fim, col_inicio, col_fim, 3)

# Funções mostrar as janelas com as imagens
cv2.waitKey(0)
cv2.destroyAllWindows()
