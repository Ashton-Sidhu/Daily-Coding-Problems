#QUESTION
#Given an array of integers, return a new array such that each element at index i of the new array
#is the product of all the numbers in the original array except the one at i.
#For example, if our input was [1, 2, 3, 4, 5], 
#the expected output would be [120, 60, 40, 30, 24].
#If our input was [3, 2, 1], the expected output would be [2, 3, 6].

#Solution

def main():

    print(ListProduct([2,4,6]))
    print(ListProduct([1,2,4,5,3]))
    print(ListProduct([2,4,0]))
    print(ListProduct([2,4,0,9]))
    print(ListProduct([-2,4,6]))
    print(ListProduct([-2,0,6,0]))
    print(ListProduct([1,2,3]))
    print(ListProduct([]))
    print(ListProduct([2]))

def ListProduct(li):
    #If length of li = 1 just return li.
    #From left to right and vice versa,
    #Initialize prodsum array to all 1's
    #L -> R, temp[0] = 1 and R -> temp[n-1] = 1 otherwise
    #prodsum[i] = li[i] * left/right[i-1]
    #Time complexity: O(n) -> traversing the list once
    #Space complexity: O(1) -> Only used a defined length array (prodlist)

    prodlist = [1] * len(li)
    tmp = 1
    ind = 0

    if len(li) == 1: return li
    
    while ind < len(li):
        prodlist[ind] = tmp
        tmp *= li[ind]
        ind += 1

    tmp = 1
    ind = -1
    while ind >= -len(li):        
        prodlist[ind] *= tmp        
        tmp *= li[ind]
        ind -= 1
        

    return prodlist 
        




if __name__ == '__main__':
    main()