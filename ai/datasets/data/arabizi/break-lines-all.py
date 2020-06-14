"""
Usage: python3 break-lines-all.py [original.arabizi] [original.gold] [newArabizi.arabizi] [new.gold] [new.lines] [chunk-length]
"""

import sys
import math

origArabizi = open(sys.argv[1], "r").readlines()
origGold = open(sys.argv[2], "r").readlines()
newArabizi = open(sys.argv[3], "w")
newGold = open(sys.argv[4], "w")
linesFile = open(sys.argv[5], "w")
length = int(sys.argv[6])

for line in range(len(origArabizi)):
    currArabiziLine = origArabizi[line].strip().split()
    currGoldLine = origGold[line].strip().split()

    currLineNoOfWords = len(currArabiziLine)

    if currLineNoOfWords <= length:
        newArabizi.write(" ".join(currArabiziLine) + "\n")
        newGold.write(" ".join(currGoldLine) + "\n")
        linesFile.write(str(currLineNoOfWords) + " no " + "\n")
    
    else:
        remainder = currLineNoOfWords % length
        totalIterations = math.ceil(currLineNoOfWords / length)
        count = 0
        for i in range(0, currLineNoOfWords, length):
            if currLineNoOfWords - i >= length:
                newArabizi.write(" ".join(currArabiziLine[i:i+length]) + "\n")
                newGold.write(" ".join(currGoldLine[i:i+length]) + "\n")
                if i+length >= currLineNoOfWords:
                    linesFile.write(str(length) + " no " + "\n")
                else:
                    if count == totalIterations - 2 and remainder != 0:
                        linesFile.write(str(remainder) + " yes " + "\n")
                    else:
                        linesFile.write(str(length) + " yes " + "\n")
            else:
                newArabizi.write(" ".join(currArabiziLine[i-(length-remainder):i+remainder]) + "\n")
                newGold.write(" ".join(currGoldLine[i-(length-remainder):i+remainder]) + "\n")
                linesFile.write(str(length) + " no " + "\n")

            count += 1

newArabizi.close()
newGold.close()
linesFile.close()