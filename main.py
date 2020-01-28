import collections
import copy

class Munkres:

    coveredX = []
    coveredY = []

    def __init__(self, costs):
        self.costs = costs
        self.costsValues = copy.deepcopy(self.costs)

    def fillWithZero(self):
        maxXLength = 0

        for i in self.costs:
            if(len(i) > maxXLength):
                maxXLength = len(i)

        for i in range(maxXLength):

            if(len(self.costs) > i):
                for _ in range(maxXLength - len(self.costs[i])):
                    self.costs[i].append(0)
            else:
                self.costs.append([])
                for _ in range(maxXLength):
                    self.costs[i].append(0)

    def subRowMin(self):
        i = 0
        for row in self.costs:
            rowMin = min(row)

            for j in range(len(row)):
                if(self.costs[i][j] != 0):
                    self.costs[i][j] -= rowMin
            i += 1

    def subColMin(self):
        for i in range(len(self.costs)):
            colMin = self.costs[0][i]
            for j in range(len(self.costs)):
                if(self.costs[j][i] < colMin):
                    colMin = self.costs[j][i]

            for j in range(len(self.costs)):
                if(self.costs[j][i] != 0):
                    self.costs[j][i] -= colMin

    def coverZeros(self):
        maxZeros = len(self.costs)
        tempCosts = copy.deepcopy(self.costs)
        
        while(maxZeros):
            for i, row in enumerate(tempCosts):
                if(collections.Counter(row)[0] == maxZeros):
                    self.coveredY.append(i)
                    for j in range(len(row)):
                        tempCosts[i][j] += 1

            for i in range(len(tempCosts)):
                col = []
                for j in range(len(tempCosts)):
                    col.append(tempCosts[j][i])
                if(collections.Counter(col)[0] == maxZeros):
                    self.coveredX.append(i)
                    for j in range(len(tempCosts)):
                        tempCosts[j][i] += 1

            maxZeros -= 1

        return len(self.coveredX) + len(self.coveredY)

    def getMatrixMin(self):
        rowMins = []
        for row in self.costs:
            for item in row:
                if(item != 0):
                    rowMins.append(item)

        return min(rowMins)

    def subFromUncovered(self, value):
        for i, row in enumerate(self.costs):
            if(self.isContain(self.coveredY, i) == 0):
                for j in range(len(row)):
                    if(self.isContain(self.coveredX, j) == 0):
                        self.costs[i][j] -= value

    def addToCoveredTwice(self, value):
        for i, row in enumerate(self.costs):
            if(self.isContain(self.coveredY, i) == 1):
                for j in range(len(row)):
                    if(self.isContain(self.coveredX, j) == 1 and self.costs[i][j] != 0):
                        self.costs[i][j] += value

    def isContain(self, array, value):
        for item in array:
            if(item == value):
                return 1
        return 0

    def calculate(self):
        self.fillWithZero()
        self.subRowMin()
        self.subColMin()

        while(self.coverZeros() < len(self.costs)):
            matrixMin = self.getMatrixMin()
            self.subFromUncovered(matrixMin)
            self.addToCoveredTwice(matrixMin)

    def getMinCostsValues(self):

        used = []
        usedIndexes = []
        ret = []

        for _ in range(len(self.costs)):
            
            leastZeros = len(self.costs[0])
            leastIndex = 0
            for j, row in enumerate(self.costs):

                if(self.isContain(usedIndexes, j) == 0):
                    zerosCount = 0
                    for item in row:
                        if(item == 0):
                            zerosCount += 1

                    if(zerosCount < leastZeros):
                        leastZeros = zerosCount
                        leastIndex = j

            for j, item in enumerate(self.costs[leastIndex]):
                if(item == 0 and self.isContain(used, j) == 0):
                    used.append(j)
                    ret.append(self.costsValues[leastIndex][j])

            usedIndexes.append(leastIndex)
            

        return ret

    def getSumOfMinCosts(self):
        sum = 0
        for value in self.getMinCostsValues():
            sum += value

        return sum