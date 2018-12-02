import InputReader

####################
# Day one part one #
####################

def Calibrate(frequencyChanges):
    frequency = 0
    for freq in frequencyChanges:
        frequency += freq
    return frequency

def PartOne():
    input = InputReader.ReadFileInt("DayOneInput")

    # Test cases
    frequency = Calibrate([1, 1, 1])
    assert frequency == 3
    frequency = Calibrate([1, 1, -2])
    assert frequency == 0
    frequency = Calibrate([-1, -2, -3])
    assert frequency == -6

    # Get the answer
    frequency = Calibrate(input)
    print("Part one: {}".format(frequency))

####################
# Day one part two #
####################

def FindRepeatedFrequency(frequencyChanges):
    n_maxIterations = 1000

    frequency = 0
    frequencies = {frequency}

    for iteration in range(n_maxIterations):
        for freq in frequencyChanges:
            frequency += freq

            if frequency in frequencies:
                return frequency
            else:
                frequencies.add(frequency)

def PartTwo():
    input = InputReader.ReadFileInt("DayOneInput")

    # Test cases
    frequency = FindRepeatedFrequency([1, -1])
    assert frequency == 0, "{} should be 0".format(frequency)
    frequency = FindRepeatedFrequency([3, 3, 4, -2, -4])
    assert frequency == 10, "{} should be 10".format(frequency)
    frequency = FindRepeatedFrequency([-6, 3, 8, 5, -6])
    assert frequency == 5, "{} should be 5".format(frequency)
    frequency = FindRepeatedFrequency([7, 7, -2, -7, -4])
    assert frequency == 14, "{} should be 14".format(frequency)

    # Get the answer
    frequency = FindRepeatedFrequency(input)
    print("Part two: {}".format(frequency))

if __name__ == "__main__":
    PartOne()
    PartTwo()