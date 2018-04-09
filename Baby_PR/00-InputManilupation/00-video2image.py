'''
Gustavo Zanoni Felipe
01/10/2017
Algoritmo feito com o intuito de extrair os frames de um video,
salvando-os como .jpg
'''

import os

input_dir = '/home/gustavozf/Documentos/UEM/Projetos/Baby/base_americana/Baby_cry/'
output_dir = '/home/gustavozf/Documentos/UEM/Projetos/Baby/base_americana/01-1_Testes_Frames/'
folders = ['Cry_No_Pain_5s', 'Cry_Pain_5s']


cont = 0
for pasta in folders:
	dir_atual = input_dir + pasta + '/'
	saida_atual = output_dir + pasta + '/'
	os.chdir(dir_atual)

	if not os.path.exists(saida_atual):
		os.makedirs(saida_atual)
		print "Novo diretorio criado!"
	for arquivo in os.listdir(dir_atual):
		if arquivo.endswith(".mp4"):
			print "Gerando imagens do video ", arquivo, " #",cont
			# arquivo%04d.jpg => dessa forma os nomes de saida ficam:
			# arquivo0001.jpg, arquivo0002.jpg, etc.
			arquivo_saida = saida_atual + arquivo[:-4]+"%04d.jpg"
			comando = 'ffmpeg -i '+arquivo+" " + arquivo_saida + " -hide_banner"
			os.system(comando)
		
			cont +=1
