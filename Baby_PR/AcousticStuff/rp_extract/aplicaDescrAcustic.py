"""
@author: Gustavo Zanoni Felipe
@descprition: chamar o descritor acustico RP para todos os folds
@Date: 14/06/2017
"""

import os, shutil

#Pasta de origem dos audios
origem = '/home/gustavozf/Documentos/Projeto/Base/'
saida = '/home/gustavozf/Documentos/Projeto/Saidas/OUT(acustic)/'
rp_extract = "/home/gustavozf/Documentos/Projeto/Teste3/rp_extract/rp_extract-master/rp_extract_batch.py"
classi = ['beach', 'bus', 'cafe-restaurant', 'car', 'city_center', 'forest_path', 'grocery_store',
                'home', 'library', 'metro_station', 'office', 'park', 'residential_area', 'train', 'tram']
tt = ['test/', 'train/']
folds = 4
contRP = 0
contRH = 0
contSSD = 0

#Aplica para train/test
for k in range(0, len(tt)):
    # Aplica para todos os folds
    for j in range(1, folds + 1): #folds
          #aplica para todas as classificacoes
          for w in range(0, len(classi)):
              #ex.: Processando audios... Tipo: test/ Fold: 1 / Folder: beach
              print "Processando audios... Tipo: " + tt[k] + " Fold: " + str(j) + " / Folder: " + classi[w] + "\n"

              #ex.: /home/user/base/test/fold1/beach/
              dir_in = origem + tt[k] + "fold" + str(j) + "/" + classi[w]
              #ex.: fold1-beach
              out_file = "fold" + str(j) + "-" + classi[w]
              #ex.: /home/user/output/test/fold1/beach/
              dir_out = saida + tt[k] + "fold" + str(j) + "/" + classi[w] + "/"
              #python rp_extract_batch.py <input_path> <feature_file_name>
              rp = "python " + rp_extract + " " + dir_in + " " + out_file

              #os.chdir(dir_in)
              os.system(rp)

              if not os.path.exists(dir_out):
                  os.makedirs(dir_out)
                  print "Diretorio criado!"

              current = "/home/gustavozf/Documentos/Projeto/Teste3/rp_extract/"
              for files in os.listdir(current):
                  if files.endswith('.rp'):
                      shutil.move(current + files, dir_out + files)
                      contRP+= 1
                      print "Arquivo RP movido: " +files + " #" + str(contRP)
                  if files.endswith('.rh'):
                      shutil.move(current + files, dir_out + files)
                      contRH += 1
                      print "Arquivo RH movido: " + files + " #" + str(contRH)
                  if files.endswith('.ssd'):
                      shutil.move(current + files, dir_out + files)
                      contSSD += 1
                      print "Arquivo SSD movido: " + files + " #" + str(contSSD)
                  if files.endswith('.log'):
                      shutil.move(current + files, dir_out + files)
print "Executado! Diretorios descritos: RP(" + str(contRP) + "), RH(" + str(contRH) + "), SSD(" + str(contSSD) + ")"