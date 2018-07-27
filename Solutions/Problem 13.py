#QUESTION
#Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
#For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

#SOLUTION
#Use a sliding window technique to count the number of unique characters in a substring, if the number of unique characters 
#exceeds k, move the sliding window from the left and record the substring as the longest substring if its length is longer 
#than the previous longest substring.
#Time Complexity: O(s), Lookup is O(1) and only iterating through the string (s) once.

def LongestSubstring(s, k):

    longestSubStr = ""
    substr = ""
    uniqueChars = set()
    
    if k > len(s): return ''

    for i in range(len(s)):

        substr += s[i]
        uniqueChars = set(substr)    

        if len(uniqueChars) > k:                      
            substr = substr[1:]

        if len(uniqueChars) == k:
            if len(substr) > len(longestSubStr):
                longestSubStr = substr

    return longestSubStr

def main():
    
    assert(LongestSubstring('abcba', 2) == 'bcb')
    assert(LongestSubstring('', 2) == '')
    assert(LongestSubstring('aaa', 2) == '')
    assert(LongestSubstring('aaab', 2) == 'aaab')
    assert(LongestSubstring('abcba', 3) == 'abcba')
    assert(LongestSubstring('abcba', 4) == '')

if __name__ == '__main__':
    main()