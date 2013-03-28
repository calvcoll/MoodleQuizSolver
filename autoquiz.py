#!/usr/bin/python

import dryscrape as ds
import sys

# Has the website code go here.
code = '''
'''

def main():
    start = (code.find('I=new Array();'))
    end = (code.find('function StartUp()'))
    arrays = ''
    for x in range(start,end):
    	arrays+=code[x]
    print arrays
    arraylinesplit = arrays.splitlines()
    questionno=0
    weighting = str(100)
    #goes through the questions finding those with a weighting of 100
    for x in range(0, len(arraylinesplit)):
		#checks to see if it is correct answer
        if (weighting in arraylinesplit[x]) and (not ('= ' + weighting) in arraylinesplit[x]):
        	#Splits the arrays up and selects the question array
            stringarray = arraylinesplit[x].split('[')
            questiondigit = stringarray[3][0]
            answer = ''
            questionarray = ['A','B','C','D']
            answer = questionarray[int(questiondigit)]
            if questionno + 1 < 10:
                print ('0' + str(questionno + 1) + '       ' + answer)
            else:
                print (str(questionno + 1) + '       ' + answer)
            questionno += 1

if __name__ == '__main__':
    main()