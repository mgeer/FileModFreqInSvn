import sys
#from ut_file_checker import *

import os.path
from log_parser import *
from text_combiner import *
class FreqStat:
    def __init__(self, inputLogFile, outputFile):
        self.input = inputLogFile
        self.output = outputFile
        return

    def state(self, suffix):
        parser = LogParser(self.input)
        if suffix == "" :
            files = parser.getModifiedFiles()
        else:
            files = parser.getModifiedFilesWithGivenSuffix(suffix)
        textWithFreq = TextCombiner().combine(files)
        outputHandler = open(self.output, "wb")
        for key in textWithFreq:
            outputHandler.write(key + "," + str(textWithFreq[key]) + "\n")

