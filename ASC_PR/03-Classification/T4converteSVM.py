# -*- coding: utf-8 -*-
"""
@author: Rafael Zottesso
@descprition: Com base nos arquivos de características criados pelo LBP dentro do diretório das classes,
monta um arquivo só no formato SVM para cada um dos folds. ("Varre" as pastas montando o .svm)
ADAPTADO POR GUSTAVO ZANONI
@Date: 03/03/2017
"""
import os, sys

# Lê o arquivo com os índices
# fidIndice = open('indices.txt', 'r')
# conteudo = fidIndice.readline()
# fidIndice.close()

#####################################################################
def converterSVM(dir_origem, folds_qtde, tipo, zona, escala, early_fusion, early, segmento):

        # Lista as classes da pasta
        indices = os.listdir(dir_origem + 'fold1/')
        indices.sort()
        total_indices = len(indices)

        # Para cada um dos folds, cria o arquivo txt
        for f in range(1, folds_qtde+1):
            arq = open(dir_origem + "fold" + str(f) + '-' + escala + zona + segmento + '-' + early + tipo + '.svm', 'w') # fold-01-lbp.svm, fold-02-lbp.svm, ...
            arq.close()

        # Copia as características de uma classe para cada um dos seus respectivos folds.
        for i in range(0, total_indices): # porque o range pára 1 antes do final
            for f in range(1, folds_qtde+1):

                # Abre o arquivo LBP
                txt = dir_origem + "fold" + str(f) + '/' + indices[i] + '/' + escala + '-' + indices[i] + zona + segmento + '-rotulo'  + early +'.txt'
                arq = open(txt, 'r')
                # Guarda cada linha em uma posição de um array
                conteudo = arq.readlines()
                arq.close()

                # Abre o arquivo SVM
                svm = open(dir_origem + "fold" + str(f) + '-' + escala + zona + segmento + '-' + early + tipo + '.svm', 'a')

                # Quebra as características em posições
                for linha in conteudo:

                    # Escreve a classe
                    svm.write(str(i) + ' ')

                    clinha = linha.split(' ') #gera uma vetor, quebrando a string nos espaços

                    # Para cada uma das características
                    for p in range(1, len(clinha)-1): # tem que contar a partir do 1, o último é o rótulo
                        caract = str(p) + ':' + clinha[p-1] + ' ' # a posição é a partir do 0
                        svm.write(caract)

                    svm.write('\n')

                svm.close()
#####################################################################
# Verifica se é Windows ou Linux
is_win = (sys.platform == 'win32')
# Se n for windows...
if not is_win:
        #dir_origem = '/media/gustavohgm/GustavoMatsushita/Projeto/backup/Resultados/'
        dir_origem = '/home/gustavozf/Documentos/Projeto/Saidas/OUT/'
# Se for Linux...
else:
    dir_origem = 'E:\\'

#####################################################################
# Quantidade de folds
folds_qtde = 4
### Tipo de característica ###
tipo = 'lbp'
# Se a imagem não foi "zoneada" deixe o parâmetro como vazio = ""
# Se foi 'zoneada', defina a quantidade de zonas
zonas = '4' #<<<< vazio
#Qtde de segmentos
segmentos = '1'
# Defina o nome da escala (que está no arquivo)
# Sempre com um menos, ex: -mel ou -bark ou -nome
escala = 'zl'  #limpar para sem zoneamento
# Foi feita a fusão de vetores? (early fusion): 1 = sim, 0 = não
early_fusion = 0
# Este conteúdo será adicionado ao nome do arquivo
if early_fusion:
    early = 'early-'
else:
    early = ''
### Origem da base ###
dir_origem += tipo + '_' + escala + '_' + zonas + 'z_' + segmentos + "s/"
####################################################################y#
#pastas = ['Mono/', 'Spectrograms1/', 'Spectrograms2/']
pastas = ['Spectrograms2/']

tt = ['test/', 'train/']

for i in range(0, 1): #numero de pastas
        for j in range(0, 2):
                dir1 = dir_origem + pastas[i] + tt[j]
                print ('Origem:', dir1)

                # Executa o script várias vezes caso existam diversas zonas
                if zonas != '':
                    # Executa a função para todas as zonas
                    for z in range(0, int(zonas)):
                        # Cria o parâmetro zona pra ser usado na nomeclatura q0_f10_22k_z60_nr_seg_30dos arquivos
                        zona = '-' + str(z)
                        for k in range (0, int(segmentos)):
                            segmento = '-' + str(k)
                            converterSVM(dir1, folds_qtde, tipo, zona, escala, early_fusion, early, segmento)
                # Caso não existam zonas...
                else:
                    converterSVM(dir1, folds_qtde, tipo, zonas, escala, early_fusion, early)
