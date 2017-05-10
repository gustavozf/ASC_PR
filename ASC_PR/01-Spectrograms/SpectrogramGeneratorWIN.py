"""
@author: Gustavo Zanoni Felipe
@descprition: Gera espectrogramas e os converte para cinza, para todos os arquivos de audio dentro de cada pasta de classificacao
que estao dentro de cada fold
@Date: 15/09/2016
"""

#shutil: para copiar os arquivos
import os, shutil, subprocess, time, sys
import cv2

t0 = time.clock()

#Lista com todas as clissificacoes
classi = ['beach', 'bus', 'cafe-restaurant', 'car', 'city_center', 'forest_path', 'grocery_store', 'home', 'library', 'metro_station', 'office', 'park', 'residential_area', 'train', 'tram']

num_arq = 0

tt=['test', 'train']
for w in range(0,2):
    #Para Stereo -> in range (1,3), para Mono -> in range (1,2) e verificar linha 43!
    #for k in range(1,3):
    for k in range(1,2):
        #Repete 4 vezes, pois sao 4 folds
        for i in range(1, 5):
            #diretorio aonde estao os folds
            dir1 = "/home/gustavozf/Documentos/Projeto/Base/" + tt[w] +"/fold" + str(i)
            #diretorio de saida (para onde os espectrogramas serao copiados)
            #novo_dir = "/home/gustavozf/Documentos/Projeto/Spectrograms" + str(k) + "/" + tt[w] + "/" + "fold" + str(i)
            novo_dir = "/home/gustavozf/Documentos/Projeto/Saidas/Espectrogramas/513new/Spectrograms1/" + tt[w] + "/" + "fold" + str(i)
            #Repete 15 vezes, pois sao 15 classificacoes
            for j in range(0, 15):
                #Diretorio do fold + classificacao
                dir2 = dir1 + '/' + classi[j]
                #Diretorio de saida + cassificacao
                novo_dir1 = novo_dir + "/" + classi[j]
                #Muda o diretorio para o fold + classicacao, caso contrario nao sera possivel gerar o espectrograma
                os.chdir(dir2)

                #Para todos os arquivos no dir2
                for filename in os.listdir(dir2):
                    #Para Stereo, descomentar a linha a baixo:
                    #sox = 'sox ' + filename + " -n remix " + str(k) + " rate -v  44100  spectrogram -y 1025 -z 150 -r -o " + filename [:-4] + '.png'
                    #Para Mono, descomentar a linha a baixo:
                    sox = 'sox ' + filename + " -n remix 1 rate -v  44100  spectrogram -z 150 -r -o " + filename [:-4] + '.png'
                    #Aplica o sox
                    os.system(sox)
                    #Converte o espectrograma para cinza
                    image = cv2.imread(filename [:-4] + '.png')
                    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    cv2.imwrite(filename [:-4] + '.png',gray_image)

                    #img = cv2.imread(filename [:-4] + '.png', 0)
                    #cv2.imwrite(filename [:-4] + '.png', img)

                    #Se nao exste o diretorio, ele eh criado
                    if not os.path.exists(novo_dir1):
                        os.makedirs(novo_dir1)
                        print ("Diretorio criado!")
                    arq_new = dir2 + '/' + filename [:-4] + ".png"
                    #copia o novo arquivo para o novo diretorio
                    shutil.move(arq_new, novo_dir1 + '/' + filename [:-4] + ".png")
                    num_arq += 1
                    print ("Espectrograma criado a partir de: " + filename + " #" + str(num_arq))

print("\n")
print(time.clock() - t0, "seconds process time")
