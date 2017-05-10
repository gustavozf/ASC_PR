"""
@author: Gustavo Zanoni Felipe
@descprition: chamar o easy (smv) para todos os folds
@Date: 19/10/2016
"""
import os, subprocess, shutil

origem = '/home/gustavozf/Documentos/Projeto/Saidas/OUT/'
saida = '/home/gustavozf/Documentos/Projeto/Saidas/Predict/'
easy = "/home/gustavozf/Documentos/Projeto/Teste3/Easy/libsvm-3.21/tools/easy2.py"
#easy = "/home/gustavozf/Documentos/Projeto/Teste3/Easy/libsvm-3.17-GPU_x64-v1.2/tools/easy.py"
#pasta = ['Mono/', 'Spectrograms1/', 'Spectrograms2/']
pasta = ['Spectrograms2/']
tt = ['test/', 'train/']
tipo_zona = 'zl'
tipo_desc = 'lbp'
zonas = 4
segmentos = 1
folds = 4


origem += tipo_desc + '_' + tipo_zona + '_' + str(zonas) + 'z_' + str(segmentos) + "s/"
for i in range(0,len(pasta)): #pastas
    for j in range(1, folds + 1): #folds
        for k in range(0,zonas):
            for w in range(0, segmentos):
                print 'Pasta: ' + pasta[i][:-1] + ' / Fold: ' + str(j) + ' / Zona: ' + str(k) + " / Segmento: " + str(w) +'\n\n'
                train = origem + pasta[i] + "/" + tt[1] + "/fold" + str(j) + '-' + tipo_zona + '-' + str(k) + '-' + str(w) + '-' + tipo_desc +".svm"
                test = origem + pasta[i] + "/" + tt[0] + "/fold" + str(j) + '-' + tipo_zona + '-' + str(k) + '-' + str(w) + '-' + tipo_desc +".svm"
                subprocess.call(["python2", easy, train, test])
                print '\n'
                current = "/home/gustavozf/Documentos/Projeto/Teste3/Easy/"
                destination = saida + "/" + tipo_zona + "_" + tipo_desc + "_" + str(zonas) + "z_" + str(segmentos) + "s/" + pasta[i] + "fold" + str(j) + "/"
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
for files in os.listdir("/home/gustavozf/Documentos/Projeto/Teste3/Easy/"):
    if files.endswith('.png'):
        os.remove(files)
#Desligar o pc apos a execucao do script
#os.system("shutdown now -h")
#raw_input("Pressione qualquer tecla para continuar...")
