#encoding: utf-8

'''
Autor: Gustavo Zanoni Felipe
Data: 06/10/2017
Este algoritmo tem por objetivo, dado um numero de classes,
criar um numero X de folds que contenha os arquivos das classes.
Separando-os em teste e treino
'''

from random import shuffle
import os, sys

def write_output(fold, classe, lista, todos_arquivos, extensao, output_file):
    print "  -> Criando teste..."

    for arquivos in lista:
        if arquivos.endswith(extensao):
            output_file.write('test/fold'+str(fold)+'/'+ classe+'/' +arquivos+'\n')

    print "  -> Criando treino..."

    outros_arquivos = list(set(todos_arquivos) - set(lista))
    for arquivos in outros_arquivos:
        if arquivos.endswith(extensao):
            output_file.write('train/fold' + str(fold) + '/'+ classe +'/' + arquivos + '\n')

def list_files(folds, dir_input, dir_output, classes, extensao):

    dir_output += str(folds) + "_folds/"

    if not os.path.exists(dir_output):
        os.mkdir(dir_output)
        print "Diretorio de saida criado! (Fold "+str(folds) +")"

    # Cria o arquivo de saida " N_folds.txt"
    output_file = open(dir_output+ str(folds)+'_folds.txt', 'w')

    # Para as classes existentes
    for i in classes:
        print "\nClasse: " + i
        # Pega o nome dos arquivos existentes na classe
        dirIn = dir_input + i
        arquivos = os.listdir(dirIn)
        quantidade = len(arquivos)

        # Embaralha os arquivos
        shuffle(arquivos)

        # N = numero de arquivos por fold
        n = quantidade/folds


        limitador = n
        count = 0

        for z in range(0, folds):
            print "-> Fold: #" + str(z+1)

            listas = []
            if z != (folds-1):
                listas.extend(arquivos[count:limitador])
                count += n
                limitador += n
            else:
                listas.extend(arquivos[count:])

            write_output(z+1, i, listas, arquivos, extensao, output_file)


    output_file.close()

def main(arguments):
    folds = [5]
    extensao = '.mp3'
    dir_input = "/home/gustavozf/Documentos/UEM/Projetos/Baby/base_americana/Base/audios_02/"
    dir_output = "/home/gustavozf/Documentos/UEM/Projetos/Baby/base_americana/03_Folds/x1333_y965/audios_02/"
    #classes = ['Cry_No_Pain_5s/', 'Cry_Pain_5s/']
    classes = os.listdir(dir_input)

    if not os.path.exists(dir_output):
        os.mkdir(dir_output)
        print "Diretorio de saida criado!"

    for fold in folds:
        list_files(fold, dir_input, dir_output, classes, extensao)


if __name__ == "__main__":
    main(sys.argv)
