import os, sys

entrada = "/home/gustavozf/Documentos/UEM/Projetos/Baby/Base_antiga/Baby_cry/"
saida = "/home/gustavozf/Documentos/UEM/Projetos/Baby/Base_antiga/audios/"

for fold in os.listdir(entrada):
	dir_atual = entrada + '/' + fold + '/'
	saida_atual = saida+'/' + fold + '/'
	print "Diretorio: " + dir_atual + '\n'

	if not os.path.exists(saida_atual):
		os.makedirs(saida_atual)

	for files in os.listdir(dir_atual):
		if files.endswith('.mp4'):
			print "Arquivo: "+ files + '\n'
			arquivo = dir_atual + files
			arquivo_new = saida_atual + files[:-3] + 'mp3'
			os.system("ffmpeg -i "+ arquivo+' '+arquivo_new)
