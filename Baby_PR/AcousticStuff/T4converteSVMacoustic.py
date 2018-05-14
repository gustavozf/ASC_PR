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
def converterSVM(dir_origem, folds_qtde, tipo):

        # Lista as classes da pasta
        indices = os.listdir(dir_origem + 'fold1/')
        indices.sort()
        total_indices = len(indices)

        # Para cada um dos folds, cria o arquivo txt
        for f in range(1, folds_qtde+1):
            arq = open(dir_origem + "fold" + str(f) + '-' + tipo + '.svm', 'w') # fold-01-lbp.svm, fold-02-lbp.svm, ...
            arq.close()

        # Copia as características de uma classe para cada um dos seus respectivos folds.
        for i in range(0, total_indices): # porque o range pára 1 antes do final
            for f in range(1, folds_qtde+1):

                # Abre o arquivo LBP
                txt = dir_origem + "fold" + str(f) + '/' + indices[i] + '/' + "fold" + str(f) + '-' + indices[i] +'.' + tipo
                arq = open(txt, 'r')
                # Guarda cada linha em uma posição de um array
                conteudo = arq.readlines()
                arq.close()

                # Abre o arquivo SVM
                svm = open(dir_origem + "fold" + str(f) + '-' + tipo + '.svm', 'a')

                # Quebra as características em posições
                for linha in conteudo:

                    # Escreve a classe
                    svm.write(str(i) + ' ')

                    clinha = linha.split(',') #gera uma vetor, quebrando a string nas virgulas

                    # Para cada uma das características
                    for p in range(2, len(clinha)): # tem que contar a partir do 1, como o proximo é o rotulo, comeca a partir de 2, o último é o rótulo
                        caract = str(p-1) + ':' + clinha[p-1] + ' ' # a posição é a partir do 0
                        svm.write(caract)
                    svm.write(str(p)+ ':' + clinha[p][:-2]+ ' ') #ultima caracteristica estava printando um "\n" junto
                    svm.write('\n')

                svm.close()
#####################################################################
# Verifica se é Windows ou Linux
is_win = (sys.platform == 'win32')
# Se n for windows...
if not is_win:
        #dir_origem = '/media/gustavohgm/GustavoMatsushita/Projeto/backup/Resultados/'
        dir_origem = '/home/gustavozf/Documentos/Projeto/Saidas/OUTacoustic/'
# Se for Linux...
else:
    dir_origem = 'E:\\'

#####################################################################
# Quantidade de folds
folds_qtde = 4
### Tipo de característica ###
tipo = ['rp', 'rh', 'ssd']


####################################################################y#

tt = ['test/', 'train/']

for i in range(0, len(tipo)): #numero de pastas
    for j in range(0, len(tt)):
        dir1 = dir_origem + tt[j]
        print 'Origem:', dir1 + ' Descritor: ' + tipo[i]
        converterSVM(dir1, folds_qtde, tipo[i])