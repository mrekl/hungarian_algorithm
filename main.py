class Munkres:
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
            print(rowMin)

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
        xZeroCount = []
        yZeroCount = []
        for _ in self.costs:
            xZeroCount.append(0)
            yZeroCount.append(0)

        for i, row in enumerate(self.costs):
            for j, item in enumerate(row):
                if(item == 0):
                    xZeroCount[j] += 1
                    yZeroCount[i] += 1

        while(max(xZeroCount) + max(yZeroCount)):
            xMax = [0, 0]
            yMax = [0, 0]
            
            for i, item in enumerate(xZeroCount):
                if(item > xMax[0]):
                    xMax[0] = item
                    xMax[1] = i

            for i, item in enumerate(xZeroCount):
                if(item > yMax[0]):
                    yMax[0] = item
                    yMax[1] = i

            if(xMax[0] >= yMax[0]):
                pass
            else:
                pass


    def getCosts(self):
        return self.costs


def main():
    costs = [
        [2, 5, 8],
        [7, 0, 6],
        [2, 1, 6]
    ]

    costs = Munkres(costs)
    costs.fillWithZero()
    costs.subRowMin()
    costs.subColMin()
    print(costs.getCosts())
    costs.coverZeros()

main()