import unittest
import os
import os.path
import sys

sys.path.append('../../src/')

from freq_stat import *

class FreqStatTest(unittest.TestCase):
    def testCombinesAndSortFilesByModificationTimes(self):
        logFile = "fixture/svn.lo"
        outputFile = "file_freq"
        freqState = FreqStat(logFile, outputFile)
        freqState.state("")
        self.assertEqual("/trunk/impala/be/src/exec/exchange-node.cc,1\n/trunk/src/client/src/java/com/baidu/queryengine/client/CliDriver.java,1\n/trunk/impala/be/src/runtime/disk-io-mgr.cc,2\n",
                         self._read(outputFile))

    def _read(self, file):
        return open(file).read()

# MAIN program ---------------------------------------------------
if __name__ == "__main__":
    unittest.main()
