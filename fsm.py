#!/usr/bin/python

'''
Title     : Finite State Automata
Author    : Atul Makkar
Created   : Feburary 24th 2019
Problem   : Create a finite state automata that gives a remainder when dividing a number by 3.
'''

##########
## GLOBALS
##########

fsm = {'S0':{'0':'S0', '1':'S1'}, 'S1':{'0':'S2', '1':'S0'}, 'S2':{'0':'S1', '1':'S2'}}
fState=['S0','S1','S2']
iState='S0'

#######
## MAIN
#######

## Helper Functions ##

def fMachine(myString):
    cState = iState
    for item in myString:
        cState = fsm[cState][item]
    if cState in fState:
        print ("Output for state %s = %s") %(cState,myString[len(myString)-1])
    else:
        print "Invalid Input"

def main():
    while True:
        choice = raw_input("Input your choice ('c' to Continue or 'q' to Quit): ")
        if choice == "c":
            rInput=raw_input("Input a string comprising of 1s and 0s: ")
            for character in rInput:
                if character != '0' and character != '1':
                    print ("Incorrect String, exiting!")
                    return
            fMachine(rInput)

        elif choice == "q":
            return

if __name__ == "__main__":
    main()
