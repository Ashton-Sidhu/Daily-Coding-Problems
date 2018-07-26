#QUESTION
# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, 
# write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.
# For example, if N is 4, then there are 5 unique ways:
# •	1, 1, 1, 1
# •	2, 1, 1
# •	1, 2, 1
# •	1, 1, 2
# •	2, 2
# What if, instead of being able to climb 1 or 2 steps at a time, 
# you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

#Solution - General Case for any X

#Calculate the number of unique ways to reach Nth step per possible step using the relationship NumWays(N) = N-X1 + .. + N-Xm
#where m is the number of different unique possible steps you can take.

def CountNSteps(N, X):

    if N is 0: return 1

    numWays = [1]        
    for i in range(1,N+1):
        total = 0
        for j in X:
            if i - j >= 0:
                total += numWays[i-j]        
        numWays.append(total)

    return numWays[N]


def main():
    assert(CountNSteps(4, [1,3,5]) == 3)
    assert(CountNSteps(0, [1,3,5]) == 1)

if __name__ == '__main__':
    main()
