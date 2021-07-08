tableData = [['apples', 'oranges', 'cherries', 'banana',],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def findLength(tDataLi):
    numberSpaces = 0
    for i in tDataLi:
        if len(i) >= numberSpaces:
            numberSpaces = len(i)
    return numberSpaces


def printTable(tData):
    colWidths = [0] * len(tData)
    col = 0
    for li in tData:
        colWidths[col] = findLength(li)
        col += 1
    col = 0
    for x in range(len(tData[0])):
        for y in range(len(tData)):
            print(tData[y][x].rjust(colWidths[y]), end = ' ')
        print('')

printTable(tableData)


