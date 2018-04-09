"""
@author: Gustavo Zanoni Felipe
@descprition: chamar o easy (svm) para todos os folds
@Date: 19/10/2016
"""
import os, subprocess, shutil

origem = '/home/gustavozf/Documentos/UEM/Projetos/Baby/base_americana/04_Features/x1333_y965/audios_04/'
saida = '/home/gustavozf/Documentos/UEM/Projetos/Baby/base_americana/05_Predicts/x1333_y965/audios_04/'
easy = "/home/gustavozf/Documentos/UEM/Projetos/Baby/base_americana/Easy/libsvm-3.21/tools/easy2.py"
pasta = ['Left_Channel/', 'Right_Channel/']
tipo_zona = 'zl'
tipo_desc = 'lbp'
zonas = 1
segmentos = 1
folds = 4
frequencia = '32000'
amplitude = '90'

if not os.path.exists(saida):
    os.mkdir(saida)
    print "Diretorio de saida criado!"

origem += str(folds) + "_folds/" + frequencia + 'Hz_' + amplitude + 'dB/'
saida += str(folds) + "_folds/"

if not os.path.exists(saida):
    os.mkdir(saida)
    print "Diretorio de saida criado!"

saida += frequencia + 'Hz_' + amplitude + 'dB/'

if not os.path.exists(saida):
    os.mkdir(saida)

origem += tipo_desc + '_' + tipo_zona + '_' + str(zonas) + 'z_' + str(segmentos) + "s/"
saida += tipo_desc + '_' + tipo_zona + '_' + str(zonas) + 'z_' + str(segmentos) + "s/"

if not os.path.exists(saida):
    os.mkdir(saida)

for i in range(0,len(pasta)): #pastas
    for j in range(1, folds+1): #folds
        for k in range(0,zonas):
            for w in range(0, segmentos):
                print 'Pasta: ' + pasta[i][:-1] + ' / Fold: ' + str(j) + ' / Zona: ' + str(k) + " / Segmento: " + str(w) +'\n\n'
                train = origem + pasta[i] + 'train/fold'+ str(j) +'-'+ tipo_zona + '-' + str(k) + '-' + str(w) + '-' + tipo_desc +".svm"
                test = origem + pasta[i] + 'test/fold'+ str(j) +'-'+ tipo_zona + '-' + str(k) + '-' + str(w) + '-' + tipo_desc +".svm"
                
                try:
                    subprocess.call(["python2", easy, train, test])
                except AssertionError as e:
                    print "Erro: " + e.value()
                    break

                print '\n'
                current = "/home/gustavozf/Documentos/UEM/Projetos/Baby/base_americana/Easy/"
                destination = saida + pasta[i] + "fold" + str(j) + "/"
                if not os.path.exists(destination):
                    os.makedirs(destination)
                for files in os.listdir(current):
                    if files.endswith('.model'):
                        shutil.move(current + files, destination + files)
                    if files.endswith('.predict'):
                        shutil.move(current + files, destination + files)
                    if files.endswith('.range'):
                        shutil.move(current + files, destination + files)
                    if files.endswith('.scale'):
                        shutil.move(current + files, destination + files)
                    if files.endswith('.out'):
                        shutil.move(current + files, destination + files)

print "Removendo arquivos '.png'..."
for files in os.listdir("/home/gustavozf/Documentos/UEM/Projetos/Baby/base_americana/Easy/"):
    if files.endswith('.png'):
        os.remove(files)

#Desligar o pc apos a execucao do script
#os.system("shutdown now -h")
#raw_input("Pressione qualquer tecla para continuar...")
