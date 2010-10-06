#!/usr/local/bin/python

# combine final snapshots from multiple NEB dump files into 1 dump file
# Syntax: neb2.py dfinal dfile1 dfile2 ...
#         dfinal = new combined dump file
#         dfile1, dfile2, ... = NEB output dump files from each replica,
#                               in correct order

# for M replicas, final snapshots are renumbered in final file from 1 to M

import sys,os
path = os.environ["LAMMPS_PYTHON_TOOLS"]
sys.path.append(path)
from dump import dump

if len(sys.argv) < 5:
  print "Syntax: neb2.py dfinal dfile1 dfile2 ..."
  sys.exit()

dfinal = sys.argv[1]
files = sys.argv[2:]

if os.path.exists(dfinal): os.remove(dfinal)

n = 1
for file in files:
  one = dump(file)
  t = one.time()
  one.tselect.one(t[-1])
  one.snaps[-1].time = n
  one.write(dfinal,1,1)
  n += 1