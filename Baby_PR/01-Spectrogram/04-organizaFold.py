import os, sys, shutil

def creat_folders(folds, pastas, saida_atual):
    # cria saida/.../canal/
    if not os.path.exists(saida_atual):
        os.makedirs(saida_atual)

    # cria saida/.../canal/(test ou train)/foldN/classe/
    for i in ["test/", "train/"]:
        saida_tt = saida_atual+ i
        if not os.path.exists(saida_tt):
            os.makedirs(saida_tt)
        for j in range(1, folds+1):
            saida_fold = saida_tt + "fold" + str(j) + "/"
            if not os.path.exists(saida_fold):
                os.mkdir(saida_fold)
            for classe in pastas:
                if not os.path.exists(saida_fold + classe):
                    os.makedirs(saida_fold + classe)

def main(arguments):
    # numero de folds existentes
    folds = 4
    # frequencia ao qual os espectrogramas foram gerados
    frequencia = '32000'
    # limite inferior de amplitude, ao qual os espectrogramas foram gerados
    amplitude = '70'
    # pastas das classes presentes na base
    #pastas = ['Friction/', 'Move/', 'Rest/', 'Pain/']
    pastas = ['Cry_No_Pain_5s/', 'Cry_Pain_5s/']
    # pastas dos canais presentes (esquerdo/direito)
    canais = ['Left_Channel/', 'Right_Channel/']
    # extensao esperada dos arquivos
    extensao = '_noise.png'

    # caminho de entrada dos espectrogramas
    file_path = '/home/gustavozf/Documentos/UEM/Projetos/Baby/base_americana/02_Espectrogramas/audios_04/'
    # caminho de saida com os folds organizados
    saida = '/home/gustavozf/Documentos/UEM/Projetos/Baby/base_americana/03_Folds/audios_04/'
    saida += str(folds) + '_folds/'
    # caminho contendo o arquivo de saida que descreve os folds
    arq_folds = saida + str(folds) + '_folds.txt'

    file_path += 'teste_' + frequencia+'Hz_' +amplitude+'dB/'
    saida += frequencia+'Hz_' +amplitude+'dB/'

    # cria o diretorio de saida
    if not os.path.exists(saida):
        os.makedirs(saida)
        print "Diretorio de saida criado!"

    # realiza a operacao para os dois lados do audio
    for canal in canais:
        arq = open(arq_folds, 'r')
        count = 1

        dir_atual = file_path + canal
        saida_atual = saida + canal

        print "\nCriando pastas em: " + canal + "\n"
        creat_folders(folds,pastas, saida_atual)

        for line in arq:
            caminho_saida = saida_atual + line[:-5] + extensao

            # divide o caminho do arquivo
            line = line.split("/")
            # line[0] = test ou train
            # line[1] = fold1, fold2, ..., foldn
            # line[2] = classe
            # line[3] = arquivo
            caminho_entrada = dir_atual + line[2] + "/" + line[3][:-5] + extensao

            print "Arquivo: " + line[3][:-5] + extensao + " #" + str(count)
            count +=1
            shutil.copy(caminho_entrada, caminho_saida)

        arq.close()

if __name__ == "__main__":
    main(sys.argv)
