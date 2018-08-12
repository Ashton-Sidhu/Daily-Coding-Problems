#QUESTION
# Suppose we represent our file system by a string in the following manner:
# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
# dir
#     subdir1
#     subdir2
#         file.ext
# The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.
# The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
# dir
#     subdir1
#         file1.ext
#         subsubdir1
#     subdir2
#         subsubdir2
#             file2.ext
# The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.
# We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).
# Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.
# Note:
# The name of a file contains at least a period and an extension.
# The name of a directory or sub-directory will not contain a period.

#SOLUTION

#First step is to split the string by \n to separate items and then count the number of \t to determine the level of the directory or file.
#If the current tab count is greate than the previous you are one level lower so set the length of the directory up to this point to subLength and then add the item to the count
#If there is a period in the item, then it is a file so check if the total length to this point is greater than the previous total length and then set the total length.
#Then set the count to the directory length before you added the length of the file (variable: subLength)
#If the item is on the same level as the previous item, set the count to length of one directory higher (variable: sublength) and then add the length of the item
#Finally, set the directory level of the current item.

#Time Complexity: O(N) iterating through the split string list once.
#Space Complexity: O(X) where x is the number of total items in a directory.


def LongestPath(s):

    pathList = s.split('\n')

    init = len(pathList[0])
    subLength = init
    tabCount = 0
    total = 0
    count = 0
    
    for item in pathList:

        tempTabCount = item.count('\t')
        
        if tempTabCount == 1:
            count = init
            subLength = init
            tabCount = 1

        if tempTabCount > tabCount:
            subLength = count
            count += len(item.strip()) + 1       
           
        if '.' in item:           
            if count > total:
                total = count
            count = subLength

        if tempTabCount == tabCount:
            count = subLength
            count += len(item.strip()) + 1
        
        tabCount = tempTabCount

    return total

def main():
    assert(LongestPath('dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext') == 20)
    assert(LongestPath('dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext') == 32)
    assert(LongestPath('dir\n\tsubdir1\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2') == 0)

if __name__ == '__main__':
    main()
