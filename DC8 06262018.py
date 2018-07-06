#QUESTION
# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
# Numbers can be 0 or negative.
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10,
# since we pick 5 and 5.
# Follow-up: Can you do this in O(N) time and constant space?

#SOLUTION

#Iterate through list and keep a history of the sum you just calculated (newSum) and the sum
#you calculated before (oldSum). At each iteration keep note of which one is the biggest (newOldest) from 
#the previous iteration and that will keep track of your largest sum and ensure you are not adding
#adjacent elements.

#Each iteration add the new element to your old sum, which will always be largest sum from the previous
#iterations by keeping its history through the variable newOldest, which will lead you to the largest
#sum of non adjacent elements.

#Time COmplexity -> O(N), going through list once
#Space Complexity -> O(1)

def LargestSum(arr):

    newSum = 0
    oldSum = 0

    for item in arr:

        if oldSum > newSum:
            newOldest = oldSum
        else:
            newOldest = newSum

        newSum = oldSum + item
        oldSum = newOldest

    if oldSum > newSum:
        return oldSum
    else:
        return newSum

def main():
    assert LargestSum([2,4,6,2,5]) == 13
    assert LargestSum([5,1,1,5]) == 10
    assert LargestSum([6,5,1,5]) == 11
    assert LargestSum([1]) == 1
    assert LargestSum([]) == 0
    assert LargestSum([5,4,7,12,9]) == 21

if __name__ == '__main__':
    main()
