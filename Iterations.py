'''
If 
while
'''

# while
''' Display the 1 to n numbers in different line'''
noOfIteration = int(input("Enter the number of iteration"))
startFrom  = 1
def DisplayIterationInDiffLine(startFrom, noOfIteration):
    while startFrom <= noOfIteration:
        print(startFrom)
        startFrom += 1


'''Display the 1 to n numbers in same line '''
def DisplayIterationInSameLine(startFrom, noOfIteration):
    while startFrom <= noOfIteration:
        print(startFrom, end= " ")
        startFrom += 1
    print()

print("Iteration from same line:")
DisplayIterationInSameLine(startFrom, noOfIteration)

print("Iteration from different line:")
DisplayIterationInDiffLine(startFrom, noOfIteration)

'''Display the 1 to n numbers in same line Ascending & Descending'''

# Ascending
def displayIterationInSameLineAscending(startFrom, noOfIteration):
    while startFrom <= noOfIteration:
        print(startFrom, end= " ")
        startFrom += 1
    print()


# Descending
def displayIterationInSameLineDescending(noOfIteration, startFrom):
    while noOfIteration >= startFrom:
        print(noOfIteration, end= " ")
        noOfIteration -= 1
    print()

print("Iteration from same line Ascending:")
displayIterationInSameLineAscending(startFrom, noOfIteration)

print("Iteration from same line Decending:")
displayIterationInSameLineDescending(noOfIteration, startFrom)

''' print iteration ascending and decending with proper alignment'''

# Ascending
def displayIterationInSameLineAscendingAlign(startFrom, noOfIteration):
    while startFrom <= noOfIteration:
        if startFrom < 10:
            print("0", startFrom, end= " ", sep="")
        else:
            print(startFrom, end= " ")
        startFrom += 1
    print()


# Descending
def displayIterationInSameLineDescendingAlign(noOfIteration, startFrom):
    while noOfIteration >= startFrom:
        if noOfIteration < 10:
            print("0", noOfIteration, end= " ", sep="")
        else:
            print(noOfIteration, end= " ")
        noOfIteration -= 1
    print()

print("propertly aligned Asc and Dec")
displayIterationInSameLineAscendingAlign(startFrom, noOfIteration)
displayIterationInSameLineDescendingAlign(noOfIteration, startFrom)