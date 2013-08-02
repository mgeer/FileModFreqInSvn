import sys
import os.path

class TextCombiner:
    # def __init__(self, inputLogFile):
    #     self.input = inputLogFile
    #     return

    def combine(self, textInList):
        fileMap = {}
        for text in textInList:
            if fileMap.has_key(text):
                fileMap[text] = fileMap[text] + 1
            else:
                fileMap[text] = 1
        return fileMap

