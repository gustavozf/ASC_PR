import os, shutil

def raw2svm(featuresFile, outputDir, foldsFile, OutputExtension, config):
    """
    This function ...
    """

    print "Features Reader is now working!"
    if (OutputExtension != ""):
        ext = OutputExtension
    else:
        ext = ".svm"
    
    fileInfo = open(foldsFile, 'r')
    '''
    Expected content format example:
        test/fold1/Class_One/MyFile.ext
        train/fold2/Class_Two/MyFile2.ext
    '''
    fileFeatures = open(featuresFile, 'r')
    '''
    Expected content format example:
        feature0 feature1 feature2 ... featureN MyFileName(label)
    '''

    files = {}
    folds = []
    foldsCount = 0

    outputs = {}

    classes = {}
    classesCount = 0

    info = fileInfo.readlines()
    features = fileFeatures.readlines()
    fileInfo.close()
    fileFeatures.close()

    print "\tstatus: reading info..."
    for line in info:
        # read line, excluding the last "\n"
        aux = line[:-1].split("/")
        name = aux[3]
        preName = "{0}-{1}-".format(aux[0], aux[1]) # Ex.: test-fold1-
        
        # if the file doesnt exist in the dictionary
        if not name in files:
            files[name] = []
        # count the number of folds
        if not aux[1] in folds:
            folds.append(aux[1])
            foldsCount +=1
        # count the number of classes
        if not aux[2] in classes:
            classes[aux[2]] = classesCount
            classesCount += 1
        
        files[name].append([preName, classes[aux[2]]]) # Ex.: ['test-fold1-', 0], where "0" refers to the first class found
    
    for i in range(1, foldsCount+1):
        test = 'test-fold' + str(i) + "-"
        train = 'train-fold' + str(i) + "-"
        outputs[test] = open(outputDir + test + config + ext, 'w')
        outputs[train] = open(outputDir + train + config + ext, 'w')

    print "\tfound: {0} folds, {1} classes and {2} files".format(foldsCount, classesCount, len(files))
    print "\tstatus: creating outputs..."
    for i in range(0, len(features)):
        features[i] = features[i].split(' ')
        name = features[i][len(features[i])-1]

        for List in files[name]:
            outputs[List[0]].write(List[1] + " ") # write the class number.
            for j in range(0, len(aux)-1):
                outputs[List[0]].write("{0}:{1} ".format(j, features[i][j])) # write the features
            outputs[List[0]].write("\n") # Ex.: "2 0:feature1 1:fature2 ... (N-1):featureN"
            
    for openedFile in outputs.keys():
        outputs[openedFile].close()

    print "\tstatus: done!"
        

