#PROBLEM
#Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
#For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
#You can assume that the messages are decodable. For example, '001' is not allowed.

#SOLUTION
#Iterate through the message 2 letters at a time and check if the int representation of the string is between 1 and 26 and if so add the number
#of paths from the previous iteration to get the number of unique paths and keep a rolling count of the number of paths to keep space complexity
#constant.

#Time Complexity -> O(n), only going through the string once
#Space Complexity -> O(1)

def decode(msg):
    n1 = 1
    n2 = 1

    if not msg: return 0

    for i in range(2, len(msg) + 1):

        path = n1

        if (int(msg[i-2]) > 0 and int(msg[i-2]) < 3) and int(msg[i-1]) < 7:
            path += n2
        else:
            n2 = 0

        n2 = n1
        n1 = path

    return path

def main():    

    assert decode('1224') == 5
    assert decode('') == 0
    assert decode('1254') == 3
    assert decode('4444') == 1

if __name__ == '__main__':
    main()
