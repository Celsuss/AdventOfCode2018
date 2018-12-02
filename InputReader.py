
def ReadFileInt(fileName):
    data = []
    f = open(fileName+".txt", "r")

    lines = f.readlines()
    for l in lines:
        n = int(l)
        data.append(n)

    return data

def ReadFileStr(fileName):
    data = []
    f = open(fileName+".txt", "r")

    lines = f.readlines()
    for l in lines:
        n = l
        if '\n' in n:
            n = n[0:-1]
        data.append(n)

    return data
    
if __name__ == "__main__":
    # data = ReadFileInt("DayOneInput")
    data = ReadFileStr("DayTwoInput")
    print(data)
