import unittest
import os
import os.path
import sys

sys.path.append('../../src/')

from text_combiner import *

class TextCombinerTest(unittest.TestCase):
    def testCombineTextInList(self):
        combiner = TextCombiner()
        textWithFreq = combiner.combine(["a", "b", "a"])
        self.assertEqual(2, textWithFreq["a"])
        self.assertEqual(1, textWithFreq["b"])

# MAIN program ---------------------------------------------------
if __name__ == "__main__":
    unittest.main()
