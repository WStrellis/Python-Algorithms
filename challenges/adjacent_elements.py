def adjacentElementsProduct(inputArray):
    highest = inputArray[0] * inputArray[1]
    for i in range(1, len(inputArray) - 1):
        p = inputArray[i] * inputArray[i + 1]
        if p > highest:
            highest = p
    return highest
