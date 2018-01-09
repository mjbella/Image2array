#!/usr/bin/env python

import sys
from PIL import Image
import numpy

# Turn on debugging?
if len(sys.argv) > 2:
    DBG = (sys.argv[2] == "dbg")
else:
    DBG = False

# Open the image file give as the first arg to this script
imgdata = numpy.asarray(Image.open(sys.argv[1]))

# Print out the raw data if you want to debug
if DBG:
   print imgdata


# Calculate the size of our image!
shape = list(imgdata.shape)

if DBG:
    print shape

a = 1
for e in shape:
    a *= e

print "Size in BYTES: ", a

result = "{"
for i in range(shape[0]):                               # Iterate over the ROWs
    result = result + "{"
    for j in range(shape[1]):                           # Iterate over the COLs
        result = result + "{"
        for k in range(shape[2]):                       # Iterate over the RGBs
            result = result + str(imgdata[i][j][k])
            if (k < (shape[2]-1)):
                result = result + ", "
        result = result + "}"
        if (j < (shape[1]-1)):
            result = result + ",\n "
    result = result + "}"
    if (i < (shape[0]-1)):
        result = result + ",\n "

result = result + "}"

print result
