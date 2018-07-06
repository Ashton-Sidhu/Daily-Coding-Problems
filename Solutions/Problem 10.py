#QUESTION:
#Implement a job scheduler which takes in a function f and an integer n,
#and calls f after n milliseconds.

#Solution:
import time

def JobScheduler(f, n):

    while(True):
        #Uncomment below line to verify scheduler is running.
        #print(time.localtime()[5])
        f()
        time.sleep(n/1000)
        
def fnc():
    print('I am doing something...')

def main():
    JobScheduler(fnc, 2000)

if __name__ == '__main__':
    main()