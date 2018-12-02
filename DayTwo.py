import InputReader

####################
# Day two part one #
####################

def GetDuplicates(ids):
    twoPairs = 0
    threePairs = 0

    for id in ids:
        dups = {}
        for c in id:
            if c in dups:
                dups[c] += 1
            else:
                dups[c] = 1
        
        twoPair = False
        threePair = False
        for d in dups:
            if dups[d] == 2:
                twoPair = True
            elif dups[d] == 3:
                threePair = True
        if twoPair == True:
            twoPairs += 1
        if threePair == True:
            threePairs += 1

    return twoPairs, threePairs

def GetChecksum(twoPairs, threePairs):
    return twoPairs * threePairs

def PartOne():
    twoPairs, threePairs = GetDuplicates(['abcdef'])
    assert twoPairs == 0 and threePairs == 0, "{}, {} should be 0, 0".format(twoPairs, threePairs)

    twoPairs, threePairs = GetDuplicates(['bababc'])
    assert twoPairs == 1 and threePairs == 1, "{}, {} should be 1, 1".format(twoPairs, threePairs)

    twoPairs, threePairs = GetDuplicates(['abbcde'])
    assert twoPairs == 1 and threePairs == 0, "{}, {} should be 1, 0".format(twoPairs, threePairs)

    twoPairs, threePairs = GetDuplicates(['abcccd'])
    assert twoPairs == 0 and threePairs == 1, "{}, {} should be 0, 1".format(twoPairs, threePairs)

    twoPairs, threePairs = GetDuplicates(['aabcdd'])
    assert twoPairs == 1 and threePairs == 0, "{}, {} should be 1, 0".format(twoPairs, threePairs)

    twoPairs, threePairs = GetDuplicates(['abcdee'])
    assert twoPairs == 1 and threePairs == 0, "{}, {} should be 1, 0".format(twoPairs, threePairs)

    twoPairs, threePairs = GetDuplicates(['ababab'])
    assert twoPairs == 0 and threePairs == 1, "{}, {} should be 0, 1".format(twoPairs, threePairs)

    ids = InputReader.ReadFileStr("DayTwoInput")
    twoPairs, threePairs = GetDuplicates(ids)
    checksum = GetChecksum(twoPairs, threePairs)
    print("Checksum: {}".format(checksum))

####################
# Day two part two #
####################

def GetMatchingBoxes(ids):
    matchingIds = []
    uniqueIds = []
    for id in ids:
        if len(uniqueIds) == 0:
            uniqueIds.append(id)
            continue
        
        match = False
        for uId in uniqueIds:
            sum = [c for c, d in zip(id, uId) if c == d]
            if len(sum) >= len(ids[0])-1:
                match = True
                if uId not in matchingIds:
                    matchingIds.append(uId)
                if id not in matchingIds:
                    matchingIds.append(id)
                break
            
        if match == False:
            uniqueIds.append(id)

    return matchingIds

def GetMatchingCharacters(ids):
    if len(ids) < 2:
        return ""
    chars = [c for c, d in zip(ids[0], ids[1]) if c == d]
    matchingStr = "".join(str(c) for c in chars)
    return matchingStr
        

def PartTwo():
    testIds = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']
    matchingIds = GetMatchingBoxes(testIds)
    matchingChars = GetMatchingCharacters(matchingIds)
    assert matchingChars == 'fgij', "{} should be fgij".format(matchingChars)

    ids = InputReader.ReadFileStr("DayTwoInput")
    matchingIds = GetMatchingBoxes(ids)
    matchingChars = GetMatchingCharacters(matchingIds)
    print("Matching characters {}".format(matchingChars))


if __name__ == "__main__":
    PartOne()
    PartTwo()