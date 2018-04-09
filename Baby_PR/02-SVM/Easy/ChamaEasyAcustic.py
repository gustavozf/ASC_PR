"""
@author: Gustavo Zanoni Felipe
@descprition: chamar o easy (svm) para todos os folds
@Date: 19/10/2016
"""
import os, subprocess, shutil

origem = '/home/gustavozf/Documentos/Projeto/Saidas/OUTacoustic/'
saida = '/home/gustavozf/Documentos/Projeto/Saidas/Predictacoustic/'
easy = "/home/gustavozf/Documentos/Projeto/Teste3/Easy/libsvm-3.21/tools/easy2.py"
#easy = "/home/gustavozf/Documentos/Projeto/Teste3/Easy/libsvm-3.17-GPU_x64-v1.2/tools/easy.py"
#pasta = ['Mono/', 'Spectrograms1/', 'Spectrograms2/']
tt = ['test/', 'train/']
tipo = ['rh', 'rp', 'ssd']
zonas = 1
segmentos = 1
folds = 4

for i in range(0,len(tipo)): #pastas
    for j in range(1, folds + 1): #folds
        print 'Tipo: ' + tipo[i] + ' / Fold: ' + str(j) +'\n\n'
        train = origem   + tt[1] + "fold" + str(j) + '-' + tipo[i] +".svm"
        test = origem  + tt[0] + "fold" + str(j) + '-' + tipo[i] +".svm"
        subprocess.call(["python2", easy, train, test])
        print '\n'
        current = "/home/gustavozf/Documentos/Projeto/Teste3/Easy/"
        destination = saida + "/" + tipo[i] + "/" + "fold" + str(j) + "/"
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
