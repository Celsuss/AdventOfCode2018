import InputReader

######################
# Day three part one #
######################

def ParseInputTransform(input):
    top_left = input.split()[2][0:-1]   # Remove the ':' at the end
    height_width = input.split()[3]

    n_left = int(top_left.split(',')[0])
    n_top = int(top_left.split(',')[1])
    n_width = int(height_width.split('x')[0])
    n_height = int(height_width.split('x')[1])

    return n_left, n_top, n_width, n_height

def PrintFabric(fabric):
    for column in fabric:
        rowStr = ""
        for row in column:
            rowStr += str(row)
        print(rowStr)

def GetOverlaps(fabric, inputs):
    overlaps = 0
    for input in inputs:
        n_left, n_top, n_width, n_height = ParseInputTransform(input)
        y = n_top
        for h in range(n_height):
            x = n_left
            for w in range(n_width):
                fabric[y][x] += 1
                if fabric[y][x] == 2:
                    overlaps += 1
                x += 1
            y += 1
    return fabric, overlaps

def CreateFabric(width, height):
    return [[0 for x in range(width)] for y in range(height)]

def PartOne():
    inputs = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']
    fabric = CreateFabric(8, 8)
    fabric, overlaps = GetOverlaps(fabric, inputs)
    PrintFabric(fabric)
    assert overlaps == 4, "{} should be 4"
    
    inputs = InputReader.ReadFileStr("DayThreeInput")
    fabric = CreateFabric(1000, 1000)
    fabric, overlaps = GetOverlaps(fabric, inputs)
    print("Overlaps: {}".format(overlaps))

######################
# Day three part two #
######################

def ParseInputId(input):
    return input.split()[0]

def PrintFabricWithId(fabric):
    for column in fabric:
        rowStr = ""
        for row in column:
            rowStr += str(row[0])
        print(rowStr)

def GetIdSet(inputs):
    ids = []
    for input in inputs:
        ids.append(ParseInputId(input))
    return set(ids)

def GetNoneOverlapingId(fabric, inputs):
    ids = GetIdSet(inputs)
    for input in inputs:
        n_left, n_top, n_width, n_height = ParseInputTransform(input)
        id = ParseInputId(input)
        y = n_top
        for h in range(n_height):
            x = n_left
            for w in range(n_width):
                fabric[y][x][0] += 1
                fabric[y][x].append(id)
                
                if fabric[y][x][0] > 1:
                    for id in fabric[y][x]:
                        ids.discard(str(id))

                x += 1
            y += 1

    return fabric, str(ids.pop())

def CreateFabricWithId(width, height):
    return [[[0] for x in range(width)] for y in range(height)]

def PartTwo():
    inputs = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']
    fabric = CreateFabricWithId(8, 8)
    fabric, id = GetNoneOverlapingId(fabric, inputs)
    PrintFabricWithId(fabric)
    print(id)
    assert id == "#3", "{} should be #3"

    inputs = InputReader.ReadFileStr("DayThreeInput")
    fabric = CreateFabricWithId(1000, 1000)
    fabric, id = GetNoneOverlapingId(fabric, inputs)
    print("Id: {}".format(id))


if __name__ == "__main__":
    PartOne()
    PartTwo()