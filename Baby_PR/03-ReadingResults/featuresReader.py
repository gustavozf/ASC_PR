import os, sys

'''
Convert a list of features to the SVM file pattern
featuresList => list: each position is a feature but the last one (the name of the file /label)
'''
def svmConverter(featuresList):
    # Excludes the last position (label)
    listSize = len(featuresList) - 1
    aux = ""

    for i in range(listSize):
        aux += "{0}:{1} ".format(i, featuresList[i])

    return str(aux[:-1])

def featureReader(inputFile, outputDir, foldsFile, outFileName, delimiterFeatures, delimiterFolds):
    inFile = open(inputFile, 'r')
    infoFile = open(foldsFile, 'r')
    foldCount = [] # count the number of folders
    classCount = 0 # count the number of classes
    filesCount = 0 # count the number of files
    classes = {} 
    outputFiles = {}
    features = {} # save every feature in the format => features[nameOfFile] = [feature1, feature2, ... , featureN]

    # if no delimiter param was passed, change it to default
    if delimiterFeatures == "":
        delimiterFeatures = " "

    if delimiterFeatures == "":
        delimiterFeatures = "/"

    print("Status: Importing features...")
    for line in inFile:
        filesCount += 1

        if line.endswith('\n'):
            line = line[:-1]

        info = line.split(delimiterFeatures)
        # remove all unwanted stuff
        info = list(filter(lambda x: ((x != ' ') and (x != '\n') and (x != delimiterFeatures)), info))
        
        features[info[len(info)-1]] = svmConverter(info)
    
    print("Creating SVM Files...")
    for line in infoFile:
        if line.endswith('\n'):
            line = line[:-1]

        #expected example: "test/fold1/someClass/someFile.mp3"
        foldInfo = line.split(delimiterFolds)
        # remove all unwanted stuff
        foldInfo = list(filter(lambda x: ((x != ' ') and (x != '\n') and (x != delimiterFolds)), info))

        # if it's the first appearance of this fold
        if not foldInfo[1] in foldCount:
            foldCount.append(foldInfo[1])
            outputFiles[foldInfo[1]] = open("{0}{1}-{2}-{3}.svm".format(outputDir, foldInfo[0], foldInfo[1], outFileName), 'w')

         # if it's the first appearance of this class
        if not foldInfo[2] in classes:
            classes[foldInfo[2]] = classCount
            classCount += 1

        outputFiles[foldInfo[1]].write("{0} {1}\n".format(classes[foldInfo[2]], features[foldInfo[3]]))

    inFile.close()
    infoFile.close()
    for fileOpen in outputFiles.values():
        fileOpen.close()

    print("All Done!\nNumber of Files: {0}\nNumber of Folds: {1}\nNumber of Classes: {2}\n".format(filesCount, len(foldCount), classCount))
