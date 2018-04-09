import os, sys, shutil
import cv2

dir_input = '/home/gustavozf/Documentos/UEM/Projetos/Baby/base_americana/01-1_Testes_Frames/'
dir_output = '/home/gustavozf/Documentos/UEM/Projetos/Baby/base_americana/01-2_Testes_Frames_Cinza/'
classes = os.listdir(dir_input)
contador = 0

if not os.path.exists(dir_output):
    os.mkdir(dir_output)

for classe in classes:
    classe += "/"
    print "Convertendo arquivos da classe: " + classe
    arquivos = os.listdir(dir_input + classe)
    saida = dir_output + classe
    entrada = dir_input + classe

    if not os.path.exists(saida):
        os.mkdir(saida)
        print "Diretorio criado!"


    for arquivo in arquivos:
        contador +=1
        print "Imagens convertidas: " +str(contador)
        image = cv2.imread(entrada + arquivo)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(saida + arquivo[:-4] + '.png',gray_image)
