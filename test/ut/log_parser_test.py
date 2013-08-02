import unittest
import os
import os.path
import sys

sys.path.append('../../src/')

from log_parser import *

class LogParserTest(unittest.TestCase):
    def testGetModifiedFiles(self):
        logFile = "fixture/svn.lo"
        parser = LogParser(logFile)
        files = parser.getModifiedFiles()
        self.assertEqual(4, len(files))
        self.assertEqual(["/trunk/impala/be/src/exec/exchange-node.cc",
                          "/trunk/impala/be/src/runtime/disk-io-mgr.cc",
                          "/trunk/impala/be/src/runtime/disk-io-mgr.cc",
                          "/trunk/src/client/src/java/com/baidu/queryengine/client/CliDriver.java"], files)

    def testGetModifiedFilesWithGivenSuffix(self):
        logFile = "fixture/svn.lo"
        parser = LogParser(logFile)
        files = parser.getModifiedFilesWithGivenSuffix(".cc")
        self.assertEqual(3, len(files))
        self.assertEqual(["/trunk/impala/be/src/exec/exchange-node.cc",
                          "/trunk/impala/be/src/runtime/disk-io-mgr.cc",
                          "/trunk/impala/be/src/runtime/disk-io-mgr.cc"], files)

    def _read(self, file):
        return open(file).read()

# MAIN program ---------------------------------------------------
if __name__ == "__main__":
    unittest.main()
