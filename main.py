import collections
import copy

class Munkres:

    coveredX = []
    coveredY = []

    def __init__(self, costs):
        self.costs = costs

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

    def addToCovered(self, value):
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

    def getCosts(self):
        return self.costs


def main():
    costs = [
        [30, 25, 10],
        [15, 10, 20],
        [25, 20, 15],
    ]

    costs = Munkres(costs)
    costs.fillWithZero()
    costs.subRowMin()
    costs.subColMin()
    
    print(costs.coverZeros())

    matrixMin = costs.getMatrixMin()

    costs.subFromUncovered(matrixMin)
    costs.addToCovered(matrixMin)

    for row in costs.getCosts():
        print(row)

    
main()