#!/usr/bin/python
# -*- coding: utf-8 -*-
#######################################
# Le o arquivo e as linhas sao armazenadas em um vetor
# Autor: Rafael Henrique D. Zottesso
# Versao: 1.0 - 19/11/2015
#######################################

import numpy as np
import sys

# Verifica se é Windows ou Linux
is_win = (sys.platform == 'win32')
# Se n for windows...
if not is_win:
	dir_origem_tipo1 = '/home/gustavozf/Documentos/BabyStuff/05_Predicts/x1500/audios/'
	dir_original_svm = '/home/gustavozf/Documentos/BabyStuff/04_Features/x1500/audios/'
# Se n for Linux...
else:
    dir_origem_tipo1 = 'D:/'

#####################################################################

# Quantidade de folds
qtde_folds = 5

# Diretório e tipo de origem
tipo1 = 'lbp'
frequencia = "32000"
amplitude = "90"
# Se a imagem não foi "zoneada" deixe o parâmetro como vazio = ""
# Se foi 'zoneada', defina como: "-n", onde n é o número da zona
zona = ''
# Defina o nome da escala (que está no arquivo)
# Sempre com um menos, ex: -mel ou -bark ou -nome
escala = 'zl'
# Foi feita a fusão de vetores? (early fusion): 1 = sim, 0 = não
early_fusion = 0
# Este conteúdo será adicionado ao nome do arquivo
if early_fusion:
	early = 'early-'
else:
	early = ''
# Nome da pasta com o conteúdo a ser analisado
#dir_origem_tipo1 += "mel_lbp_3z_1s/Spectrograms2/predicts/"
extra_path = str(qtde_folds) + "_folds/"+frequencia+"Hz_"+amplitude+"dB/"+tipo1+"_"+escala+"_1z_1s/Right_Channel/"
dir_origem_tipo1 += extra_path
dir_original_svm+=  extra_path
#####################################################################

print 'Origem: ', dir_origem_tipo1

# Define as regras usadas
regras = [tipo1]
# Para armazenar o conteúdo das regras
qtde_regras = len(regras)
fold_results = [''] * qtde_regras
arq_fold_fusao = [''] * qtde_regras
conteudo_fold_fusao = [''] * qtde_regras
acertos = [''] * qtde_regras
fusao = [''] * qtde_regras

# Criação dos cálculos
matriz_confusao = [''] * qtde_regras
total_geral_acerto = 0
total_geral_amostras = 0
recall = [''] * qtde_regras
recall_medio = [''] * qtde_regras
precision = [''] * qtde_regras
precision_medio = [''] * qtde_regras
fmeasure = [''] * qtde_regras
macrof = [''] * qtde_regras

# Total de classes
total_classes = 0

# Faz o cálculo pra cada um dos folds
for f in range(1, qtde_folds+1):

	# Abrir predict original e os outros predicts para cada fold
	fold_original = dir_original_svm + 'test/fold' + str(f) + "-" + escala + '-0-0-' + early + tipo1 + '.svm'
	fold_results[0] = dir_origem_tipo1 + 'fold' + str(f)  + "/" + 'fold' + str(f)  + "-" + escala + '-0-0-' + early + tipo1 + '.svm.predict'
	#fold_results[0] = dir_origem_tipo1 + 'fold'  + "-" + str(f)  + '-fusao-maximo-lbp-lbp.svm.predict'

	# Abre o original para saber as classes corretas
	arq_fold_original = open(fold_original, 'r')
	conteudo_fold_original = arq_fold_original.readlines()
	arq_fold_original.close()

	# Conta quantas classes tem, mas só uma vez, contando as colunas de alguma linha -1
	if total_classes == 0:

		# Abre o predict pra contar as classes
		file_predict = open(fold_results[0], 'r')
		conteudo_file_predict = file_predict.readlines()
		file_predict.close()

		# Conta as colunas, -1 porque tem o texto "label" ou "9999" na primeira coluna do predict
		total_classes = len(conteudo_file_predict[0].split(' '))-1

		# Cria uma matriz para todos os folds, e armazena o total geral
		for r in range( qtde_regras ):
			# Criar a matriz de confusão, como um array numpy para poder fazer operações por linha inteira e colunas
			# é uma matriz "classe x classe"
			matriz_confusao[r] = np.array( [ [0 for x in range(total_classes)] for x in range(total_classes) ], dtype=np.int )


	# Conta quantas amostras tem neste fold
	total_amostras = len(conteudo_fold_original)

	# Abre os arquivos da fusão
	for r in range( qtde_regras ):
		arq_fold_fusao[r] = open(fold_results[r], 'r')
		conteudo_fold_fusao[r] = arq_fold_fusao[r].readlines()
		arq_fold_fusao[r].close()

		# Contar os acertos de cada regra
		acertos[r] = 0

	# Compara a classe encontrada no arquivo de fusão com a classe do fold original
	# Como todos tem o mesmo tanto de classe e amostra, qualquer um é usado
	# A primeira LINHA só possui os rótulos, por isso começa em 1
	# Para cada linha dos arquivos...
	for i in range (1, len(conteudo_fold_fusao[0]) ):

		# Quebra a linha nos espaços pra pegar a primeira coluna
		# O original não tem a primeira linha de rótulos
		original = conteudo_fold_original[i-1].split(' ')

		# Faz a mesma coisa com cada um dos arquivos de fusão
		for r in range( qtde_regras ):
			fusao[r] = conteudo_fold_fusao[r][i].split(' ')

			if original[0] == fusao[r][0]:
				acertos[r] += 1

			# Matriz de confusão, soma 1 na linha correta e na coluna da classe que achou que é
			matriz_confusao[r] [ int(original[0]) ] [ int(fusao[r][0]) ] += 1

	# Mostrando os resultados
	for r in range( qtde_regras ):
		print '========== FOLD %02d ==========' % f
		#print 'Regra:', regras[r].upper()
		#print 'Total:', total_amostras
		print 'Acertos: %d/%d' % (acertos[r], total_amostras)
		print 'Acurácia: %.2f%%' % (float( acertos[r] ) * 100 / float( total_amostras ))

	# Só pra separar as linhas entre folds
	#print ''

print '\n******** Fim da contagem ********\n'

# Depois que terminou os 10 folds, precisa contar a matriz de confusão
# para cada uma das regras
for r in range( qtde_regras ):

	# Cria as dimensões para calcular cada medida
	recall[r] = np.array( [0] * total_classes, dtype=np.float )
	precision[r] = np.array( [0] * total_classes, dtype=np.float )
	fmeasure[r] = np.array( [0] * total_classes, dtype=np.float )
	macrof[r] = np.array( [0] * total_classes, dtype=np.float )

	# Calculando o recall e o precision para cada classe
	for x in range(total_classes):
		# Verifica se não é zero
		correto = float(matriz_confusao[r][x][x])
		sum_linha = float( matriz_confusao[r][x,:].sum() )
		sum_coluna = float( matriz_confusao[r][:,x].sum() )

		total_geral_acerto += correto
		total_geral_amostras += sum_linha

		# Se a soma é maior que zero faz a conta
		if sum_linha > 0.0 and correto > 0.0:
			# Recall = Total certo da classe / total da linha
			recall[r][x] = correto / sum_linha
		else:
			# Recall = Total certo da classe / total da linha
			recall[r][x] = 0

		# Se a soma é maior que zero faz a conta
		if sum_coluna > 0.0 and correto > 0.0:
			# Precision = Total certo da classe / total da coluna
			precision[r][x] = correto / sum_coluna
		else:
			# Precision = Total certo da classe / total da coluna
			precision[r][x] = 0

	# Calculando o recall e o precision médio para todos os folds
	# Para a regra r, soma todas as colunas: [r,:]
	recall_medio[r] = ( recall[r].sum() ) / float(total_classes)
	precision_medio[r] = ( precision[r].sum() ) / float(total_classes)


	# Usar o try porque pode ser zero
	try:
		# F-Measure = (2 * rec * prec) / (rec + prec)
		fmeasure[r] = float( (recall_medio[r] * precision_medio[r] * 2) ) / float( (recall_medio[r] + precision_medio[r]) )
	except:
		fmeasure[r] = 0.0

	acuracia = (float(total_geral_acerto) / float(total_geral_amostras)) * 100

	print '========== Resultado: %s ==========' % regras[r].upper()
	print 'Acertos: %d/%d' % (total_geral_acerto, total_geral_amostras)
	print 'Acurácia: %.2f' % acuracia
	print 'Recall: %.2f' % (recall_medio[r] * 100)
	print 'Precision: %.2f' % (precision_medio[r] * 100)
	print 'F-Measure: %.2f' % (fmeasure[r] * 100)
	print '===================================\n'
	print 'X dB & %.2f & %.2f & %.2f & %.2f \\\\\n' % (acuracia, recall_medio[r] * 100, precision_medio[r] * 100, fmeasure[r] * 100)
	print '===================================\n\n'

print(matriz_confusao)