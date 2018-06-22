#QUESTION:
# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

#SOLUTION:
#Use a bucket method to order the list where the numbers are > 0 and less than the length of the list, on the left hand side
#Iterate over the list and check if the index+1 (due to 0 index) is equal to the value at the index,
#If it is not, that is the smallest positive value missing.

#Time Complexity: O(2n) -> O(n) due to going through each element in the list once per loop
#Space Complexity: O(1) -> Used the memory given.


def FindSmallest(li):

    if not li: return 1

    for ind,item in enumerate(li):       

        while ind + 1 != li[ind] and 0 < li[ind] <= len(li):
            v = li[ind]      
            li[ind], li[v-1] = li[v-1], li[ind]
            li[v-1] = v
    
            if li[ind] == li[v-1]:
                break

    for ind,item in enumerate(li):
        if li[ind] != ind + 1:
            return ind + 1

def main():
    assert FindSmallest([-2,2,8,0,-10,4,7,1]) == 3
    assert FindSmallest([-2,2,2,0,-10,4,7,1]) == 3
    assert FindSmallest([-2,-4,8,0,-10,4,7]) == 1
    assert FindSmallest([-2,-4,8,0,4,4,7]) == 1
    assert FindSmallest([5]) == 1
    assert FindSmallest([]) == 1
    assert FindSmallest([1,-4]) == 2


if __name__ == '__main__':
    main()



