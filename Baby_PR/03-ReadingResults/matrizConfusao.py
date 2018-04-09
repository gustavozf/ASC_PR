import sys, numpy

############################################################ Variables
dirFeaturesFiles = '/home/gustavozf/Documentos/UEM/Projetos/Baby/base_americana/04_Features/x1500/audios/'
dirPredictsFiles = '/home/gustavozf/Documentos/UEM/Projetos/Baby/base_americana/05_Predicts/x1500/audios/'
numClasses = 2 #(Optional) -- Default = 0

numFolds = 5
descriptor = "lbp"
scale = "zl"
zones = 1
segments = 1
frequency = "32000"
amplitude = "90"
channels = ['Right', "Left"]

############################################################ Functions
def calculateConfMatrix(channel):
    files = 0
    trues = 0
    confMatrixGeneral = None
    for i in range(1, numFolds+1):
        print "\t- Reading from Fold #" + str(i)

        # Ex.: "fold1-zl-0-0-lbp.svm"
        genericFile = ("fold" + str(i) + "-" + scale + "-" + str(zones-1) +
                        "-" + str(segments-1) + "-" + descriptor+ ".svm")
        # Ex.: "/your/path/Left_Channel/test/fold1-zl-0-0-lbp.svm"
        featuresFilePath = (dirFeaturesFiles + channel + "_Channel/test/" + genericFile)
        # Ex.: "/your/path/Left_Channel/fold1/fold1-zl-0-0-lbp.svm.predict"
        predictFilePath = (dirPredictsFiles + channel + "_Channel/fold" + str(i)
                        + "/" + genericFile + ".predict")

        #Open the files and read them
        featuresFile = open(featuresFilePath, 'r')
        predictFile = open(predictFilePath, 'r')

        features = featuresFile.readlines()
        predict = predictFile.readlines()

        featuresFile.close()
        predictFile.close()

        # If variable is null, finds out its value
        global numClasses
        if not numClasses:
            #Takes the first line of the predict file and check the number os classes
            numClasses = len(predict[0].split(' ')) - 1

        # Creates confusion matrix
        confusionMatrix = numpy.zeros((numClasses, numClasses))

        # matrix[true][predicted] -> true X predicted
        for j in range(0, len(features)):
            true = int(features[j].split(' ')[0])
            predicted = int(predict[j+1].split(' ')[0])
            confusionMatrix[true][predicted] += 1
            files += 1 # Count the number os samples

            # if was correctly predicted, counter++
            if true == predicted:
                trues +=1

        # Sum local conf. matrices with the global one
        if confMatrixGeneral is None:
            confMatrixGeneral = numpy.copy(confusionMatrix)
        else:
            confMatrixGeneral += confusionMatrix

    print " \nConfusion Matrix:"
    print  confMatrixGeneral
    print "Accuracy: " +  str(trues/float(files) * 100) + "%\n"
        
        

        

def main(args):
    pathEnd =  (str(numFolds) + "_folds/" + 
                frequency + "Hz_" + amplitude + "dB/" +
                descriptor + "_" + scale + "_" + 
                str(zones) + "z_" + str(segments) + "s/")

    global dirFeaturesFiles
    global dirPredictsFiles

    dirFeaturesFiles += pathEnd
    dirPredictsFiles += pathEnd

    for channel in channels:
        print "status: calculating for " + channel + " Channel"
        calculateConfMatrix(channel)

if __name__ == "__main__":
    main(sys.argv)
