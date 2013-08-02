import sys

sys.path.append("./src")

from freq_stat import *

args = sys.argv
if (len(args) != 4):
    raise Exception("invalid arguments!")

svnLogFile = args[1]
output = args[2]
suffix = args[3]


stat = FreqStat(svnLogFile, output)
stat.state(suffix)
