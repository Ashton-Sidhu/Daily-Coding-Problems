#QUESTION:
#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

#SOLUTION:

def AddToK(li, k):

    #Go through each element and check if the compliment of itself has been seen before and store it in a set.
    #Lookup in Set is O(1), Iterate through list is O(N)
    #Complexity is O(N)
    nummap = set([])
        
    for item in li:
        #Calculate compliment of number and if it exists in set return true.        
        compliment = k - item
        if item in nummap:            
            return True
        nummap.add(compliment)

    return False

def main():  
    
    print(AddToK([8], 8))
    print(AddToK([1,2,4,4], 8))
    print(AddToK([1,2,4,5], 8))
    print(AddToK([1,2,4,6,7], 8))
    print(AddToK([], 8))

if __name__ == '__main__':
    main()
