import turtle
import time

def displayStatistics(fileAllocationTable):
    clusterKB = 4

    totalSpace = len(fileAllocationTable) * clusterKB
    print("Total Disk Space: " + str(totalSpace) + "KB")

    totalUsed = 0
    for cluster in fileAllocationTable:
        if cluster[0] != "":
            totalUsed += clusterKB
    print("Total Used Space: " + str(totalUsed) + "KB")

    #calculating the total free space
    totalFree = totalSpace - totalUsed

    #calculating percentage used
    percentageUsed = (totalUsed / totalSpace) * 100

def defragmentation(fileAllocationTable):
    print("Defragmenting...")
    #defragmentation code
    print("Defragmenting...")
    newFAT = [["", -1] for _ in range(len(fileAllocationTable))]
    currentIndex = 0

    for i in range(len(fileAllocationTable)):
        if fileAllocationTable[i][0] != "":
            fileName = fileAllocationTable[i][0]
            while i != -1:
                newFAT[currentIndex][0] = fileName
                nextIndex = fileAllocationTable[i][1]
                if nextIndex != -1:
                    newFAT[currentIndex][1] = currentIndex + 1
                i = nextIndex
                currentIndex += 1

    return newFAT

#creating empty FAT wih 100 clusters
fileAllocationTable = []
for i in range(0, 100):
    fileAllocationTable.append(["",-1])

fileAllocationTable[0] = ["file A",1]
fileAllocationTable[1] = ["file A",2]
fileAllocationTable[2] = ["file A",7]
fileAllocationTable[3] = ["file B",4]
fileAllocationTable[4] = ["file B",5]
fileAllocationTable[5] = ["file B",6]
fileAllocationTable[6] = ["file B",26]
fileAllocationTable[7] = ["file A",8]
fileAllocationTable[8] = ["file A",19]
fileAllocationTable[9] = ["file C",10]
fileAllocationTable[10] = ["file C",11]
fileAllocationTable[11] = ["file C",12]
fileAllocationTable[12] = ["file C",13]
fileAllocationTable[13] = ["file C",14]
fileAllocationTable[14] = ["file C",34]
fileAllocationTable[15] = ["file D",16]
fileAllocationTable[16] = ["file D",17]
fileAllocationTable[17] = ["file D",18]
fileAllocationTable[18] = ["file D",22]
fileAllocationTable[19] = ["file A",20]
fileAllocationTable[20] = ["file A",21]
fileAllocationTable[21] = ["file A",35]
fileAllocationTable[22] = ["file D",23]
fileAllocationTable[23] = ["file D",24]
fileAllocationTable[24] = ["file D",25]
fileAllocationTable[25] = ["file D",-1]
fileAllocationTable[26] = ["file B",27]
fileAllocationTable[27] = ["file B",53]
fileAllocationTable[28] = ["file E",29]
fileAllocationTable[29] = ["file E",30]
fileAllocationTable[30] = ["file E",31]
fileAllocationTable[31] = ["file E",32]
fileAllocationTable[32] = ["file E",33]
fileAllocationTable[33] = ["file E",46]
fileAllocationTable[34] = ["file C",49]
fileAllocationTable[35] = ["file A",36]
fileAllocationTable[36] = ["file A",37]
fileAllocationTable[37] = ["file A",64]
fileAllocationTable[38] = ["file F",39]
fileAllocationTable[39] = ["file F",40]
fileAllocationTable[40] = ["file F",41]
fileAllocationTable[41] = ["file F",42]
fileAllocationTable[42] = ["file F",43]
fileAllocationTable[43] = ["file F",44]
fileAllocationTable[44] = ["file F",45]
fileAllocationTable[45] = ["file F",59]
fileAllocationTable[46] = ["file E",47]
fileAllocationTable[47] = ["file E",48]
fileAllocationTable[48] = ["file E",-1]
fileAllocationTable[49] = ["file C",50]
fileAllocationTable[50] = ["file C",51]
fileAllocationTable[51] = ["file C",52]
fileAllocationTable[52] = ["file C",-1]
fileAllocationTable[53] = ["file B",-1]
fileAllocationTable[54] = ["file B",55]
fileAllocationTable[55] = ["file B",56]
fileAllocationTable[56] = ["file B",57]
fileAllocationTable[57] = ["file B",58]
fileAllocationTable[58] = ["file B",-1]
fileAllocationTable[59] = ["file F",60]
fileAllocationTable[60] = ["file F",61]
fileAllocationTable[61] = ["file F",62]
fileAllocationTable[62] = ["file F",63]
fileAllocationTable[63] = ["file F",-1]
fileAllocationTable[64] = ["file A",65]
fileAllocationTable[65] = ["file A",-1]

displayStatistics(fileAllocationTable)
defragmentation(fileAllocationTable)
