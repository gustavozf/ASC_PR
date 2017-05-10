"""
@author: Gustavo Zanoni Felipe
@descprition: Abre o .txt que contem o nome do arquivo + classificacao, cria uma pasta com o fold/classificacao e copia o audio para dentro
deste novo diretorio
@Date: 02/09/2016
"""

#shutil usado para copiar arquivos
import os, shutil

#salva o diretorio das amostras
arq_root = "/home/gustavozf/Documentos/Projeto/Acoustic_scene/wav/"

#Repete 4 vezes, pois sao 4 folds
for i in range(1, 5):
    num_arq = 0
    novo_dir = "/home/gustavozf/Documentos/Base/train/fold" + str(i)

    #cria novo diretorio
    if not os.path.exists(novo_dir):
        os.makedirs(novo_dir)
    print "Diretorio criado!"

    #Le linha por linha do arquivo txt
    arq_aberto = "/home/gustavozf/Documentos/Projeto/Acoustic_scene/TUT-acoustic-scenes-2016-development/evaluation_setup/fold" + str(i) + "_train.txt"
    for line in open(arq_aberto, "r"):

        #Caso o final da linha seja um tab+"classificacao"+quebra de linha
        if line.endswith('\tbeach\r\n'):
                #cria novo diretorio
                if not os.path.exists(novo_dir + "/beach"):
                    os.makedirs(novo_dir + "/beach")
                #pega o diretorio + nome do arquivo
                arq_new = arq_root + line [:-8]
                #copia o arquivo para a pasta nova
                shutil.copy2(arq_new, novo_dir + "/beach")
        elif line.endswith('\tbus\r\n'):
                #cria novo diretorio
                if not os.path.exists(novo_dir + "/bus"):
                    os.makedirs(novo_dir + "/bus")

                #pega o diretorio + nome do arquivo
                arq_new = arq_root + line [:-6]
                #copia o arquivo para a pasta nova
                shutil.copy2(arq_new, novo_dir + "/bus")
        elif line.endswith('\tcafe/restaurant\r\n'):
                #cria novo diretorio
                if not os.path.exists(novo_dir + "/cafe-restaurant"):
                    os.makedirs(novo_dir + "/cafe-restaurant")

                #pega o diretorio + nome do arquivo
                arq_new = arq_root + line [:-18]
                #copia o arquivo para a pasta nova
                shutil.copy2(arq_new, novo_dir + "/cafe-restaurant")
        elif line.endswith('\tcar\r\n'):
                #cria novo diretorio
                if not os.path.exists(novo_dir + "/car"):
                    os.makedirs(novo_dir + "/car")

                #pega o diretorio + nome do arquivo
                arq_new = arq_root + line [:-6]
                #copia o arquivo para a pasta nova
                shutil.copy2(arq_new, novo_dir + "/car")
        elif line.endswith('\tcity_center\r\n'):
                #cria novo diretorio
                if not os.path.exists(novo_dir + "/city_center"):
                    os.makedirs(novo_dir + "/city_center")

                #pega o diretorio + nome do arquivo
                arq_new = arq_root + line [:-14]
                #copia o arquivo para a pasta nova
                shutil.copy2(arq_new, novo_dir + "/city_center")
        elif line.endswith('\tforest_path\r\n'):
                #cria novo diretorio
                if not os.path.exists(novo_dir + "/forest_path"):
                    os.makedirs(novo_dir + "/forest_path")

                #pega o diretorio + nome do arquivo
                arq_new = arq_root + line [:-14]
                #copia o arquivo para a pasta nova
                shutil.copy2(arq_new, novo_dir + "/forest_path")
        elif line.endswith('\tgrocery_store\r\n'):
                #cria novo diretorio
                if not os.path.exists(novo_dir + "/grocery_store"):
                    os.makedirs(novo_dir + "/grocery_store")

                #pega o diretorio + nome do arquivo
                arq_new = arq_root + line [:-16]
                #copia o arquivo para a pasta nova
                shutil.copy2(arq_new, novo_dir + "/grocery_store")
        elif line.endswith('\thome\r\n'):
                #cria novo diretorio
                if not os.path.exists(novo_dir + "/home"):
                    os.makedirs(novo_dir + "/home")

                #pega o diretorio + nome do arquivo
                arq_new = arq_root + line [:-7]
                #copia o arquivo para a pasta nova
                shutil.copy2(arq_new, novo_dir + "/home")
        elif line.endswith('\tlibrary\r\n'):
                #cria novo diretorio
                if not os.path.exists(novo_dir + "/library"):
                    os.makedirs(novo_dir + "/library")

                #pega o diretorio + nome do arquivo
                arq_new = arq_root + line [:-10]
                #copia o arquivo para a pasta nova
                shutil.copy2(arq_new, novo_dir + "/library")
        elif line.endswith('\tmetro_station\r\n'):
                #cria novo diretorio
                if not os.path.exists(novo_dir + "/metro_station"):
                    os.makedirs(novo_dir + "/metro_station")

                #pega o diretorio + nome do arquivo
                arq_new = arq_root + line [:-16]
                #copia o arquivo para a pasta nova
                shutil.copy2(arq_new, novo_dir + "/metro_station")
        elif line.endswith('\toffice\r\n'):
                #cria novo diretorio
                if not os.path.exists(novo_dir + "/office"):
                    os.makedirs(novo_dir + "/office")

                #pega o diretorio + nome do arquivo
                arq_new = arq_root + line [:-9]
                #copia o arquivo para a pasta nova
                shutil.copy2(arq_new, novo_dir + "/office")
        elif line.endswith('\tpark\r\n'):
                #cria novo diretorio
                if not os.path.exists(novo_dir + "/park"):
                    os.makedirs(novo_dir + "/park")

                #pega o diretorio + nome do arquivo
                arq_new = arq_root + line [:-7]
                #copia o arquivo para a pasta nova
                shutil.copy2(arq_new, novo_dir + "/park")
        elif line.endswith('\tresidential_area\r\n'):
            if not os.path.exists(novo_dir + "/residential_area"):
                os.makedirs(novo_dir + "/residential_area")

            #pega o diretorio + nome do arquivo
            arq_new = arq_root + line [:-19]
            #copia o arquivo para a pasta nova
            shutil.copy2(arq_new, novo_dir + "/residential_area")
        elif line.endswith('\ttrain\r\n'):
            if not os.path.exists(novo_dir + "/train"):
                os.makedirs(novo_dir + "/train")

            #pega o diretorio + nome do arquivo
            arq_new = arq_root + line [:-8]
            #copia o arquivo para a pasta nova
            shutil.copy2(arq_new, novo_dir + "/train")
        else:
            if not os.path.exists(novo_dir + "/tram"):
                os.makedirs(novo_dir + "/tram")

            #pega o diretorio + nome do arquivo
            arq_new = arq_root + line [:-7]
            #copia o arquivo para a pasta nova
            shutil.copy2(arq_new, novo_dir + "/tram")

        #Para mostrar a quantidade de arquivos movidos
        num_arq += 1
        print "Arquivos movidos: ", num_arq
