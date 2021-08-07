
import re #imports the built-in module of regular expressiom

fhand = open('regex_sum_920497.txt') #opens the given file 
numbers_list=list() #creates and defines that numbers_list is of type list
sum=0 #creates variable sum as soon as we assign value 0 to it


for line in fhand: #goes through each line in the file
    line=line.rstrip()
    '''rstrip removes the white spaces from the
    right of the string'''
    numbers=re.findall('[0-9]+',line)
    '''.findall returns a list with all matches
        0-9 means of type number
        + means one or more occurences
        '''
    numbers_list=numbers_list + numbers
    '''appends the numbers found in the string line
       to a list i.e. numbers_list'''

for number in numbers_list:
    sum = sum + int(number)
    '''casting the number which is of type string into
       type int
       In order to find sum of all the numbers
       we add all the numbers up '''

  


print('Sum of the numbers in the text is',sum)

    
