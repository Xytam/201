#getSum calculates the sum of all values in the given list
#Input: gradesList, a list of grades
#Output: sumValue, the sum of all grades
def getSum(gradesList):
    sumValue = 0
    #loops over all values, incrementally adding each one
    for i in range(0,len(gradesList)):
        sumValue = sumValue + gradesList[i]

    return sumValue

#getMedian finds the median for a given list. Accounts for two cases:
# 1) If the list has an odd amount of numbers, the median is the middle number
# 2) If the list has an even amount of numbers, the median is the average
# of the two numbers closest to the middle of the list
#Input: gradesList, a list of grades
#Output: the median value of the input list
def getMedian(gradesList):
    sortedGrades = sorted(gradesList)

    #Case for if the amount of elements in the list is odd
    if len(sortedGrades) % 2 == 1:
        return sortedGrades[int((len(sortedGrades))/2)]
    #otherwise case for when the list is even
    else:
        lower = sortedGrades[int(len(sortedGrades)/2-1)]
        upper = sortedGrades[int(len(sortedGrades)/2)]

    return (float(lower + upper)) / 2

#getAverage calculates the average of a given list- uses
#getSum() to calculate the sum
#Input: gradesList, a list of grades
#Output: average, the average value of the input list
def getAverage(gradesList):
    sumValue = getSum(gradesList)

    average = sumValue/len(gradesList)

    return average

#getAverageIfPresent calculates the average of a given list, minus
#any values that are zero
#Input: gradesList, a list of grades
#Output: average, the average value of the input list
def getAverageIfPresent(gradesList):
    
    #loops over every grade, checking for a 0
    #if a 0 is found, it will be removed
    for grade in gradesList:
        if(grade==0):
            gradesList.remove(grade)

    sumValue = getSum(gradesList)
    average = sumValue/len(gradesList)

    return average

def main():
    #If a student was absent, they got a zero.
    grades = [0,90,52,75,66,88,0,100]

    #Calculates values
    average = getAverage(grades)
    median = getMedian(grades)
    averageOfPresent = getAverageIfPresent(grades) 

    print("The average of the grades is:",average)
    print("The average of the grades (minus any absent students) is:",averageOfPresent)
    print("The median of the grades is:",median)

main()
