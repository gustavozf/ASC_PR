import os, sys, shutil
import cv2

#dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = '/home/gustavozf/Documentos/UEM/Projetos/Baby/base_americana/Base/audios_04/'

frequencia = sys.argv[1]
amplitude = sys.argv[2]
#pastas = ['Cry_No_Pain_5s/', 'Cry_Pain_5s/', 'Cry_No_Pain_10s/', 'Cry_Pain_10s/']
#pastas = ['Cry_No_Pain_5s/', 'Cry_Pain_5s/']
pastas = os.listdir(dir_path)
canais = ['Left_Channel/', 'Right_Channel/']

print "Criando arquivos com frequencia: " + str(frequencia) + " e amplitude: "+ str(amplitude)
dir_saida = "/home/gustavozf/Documentos/UEM/Projetos/Baby/base_americana/02_Espectrogramas/x1500/audios_04/teste_"+frequencia+"Hz_"+amplitude+"dB/"

if not os.path.exists(dir_saida):
    os.makedirs(dir_saida)
    print "Diretorio de saida criado: " + dir_saida

print "Gerando Espectrogramas..."
contador = 0
for i in range(0, len(canais)):
    saida = dir_saida + canais[i]

    for j in range(0, len(pastas)):
        entrada = dir_path + pastas[j] + "/"
        os.chdir(entrada)
        for arquivo in os.listdir(entrada):
            if arquivo.endswith(".mp3"):
                contador+=1
                saida_path = saida + pastas[j]
                sox = "sox " + arquivo + " -n remix "+ str(i+1)+" rate -v "+ frequencia + " spectrogram -x 1500 -z "+ amplitude +" -r -o "+ arquivo[:-3] + "png"
                os.system(sox)

                image = cv2.imread(arquivo[:-4] + '.png')
                gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                cv2.imwrite(arquivo[:-4] + '.png',gray_image)

                if not os.path.exists(saida_path):
                    os.makedirs(saida_path)
                    print "Diretorio Criado: " + saida_path
                shutil.move(entrada + "/" + arquivo[:-3] + "png", saida_path + "/" + arquivo[:-3] + "png")
                print "Espectrogramas gerados: " + str(contador)
