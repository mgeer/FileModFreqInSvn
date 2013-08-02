import sys
import os.path

from xml.dom import minidom

class LogParser:
    def __init__(self, inputLogFile):
        self.input = inputLogFile
        return

    def getModifiedFiles(self):
        files = []
        for path in self._getPaths():
            if path.getAttribute("action") == "M":
                files.append(path.firstChild.nodeValue)
        return files

    def getModifiedFilesWithGivenSuffix(self, suffix):
        files = []
        for path in self._getPaths():
            value = path.firstChild.nodeValue
            if path.getAttribute("action") == "M" and value.endswith(suffix):
                files.append(value)
        return files

    def _getPaths(self):
        xmldoc = minidom.parse(self.input)
        return xmldoc.getElementsByTagName('path')

