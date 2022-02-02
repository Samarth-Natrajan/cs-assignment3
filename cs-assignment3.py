# Q.1)

string1 = input("enter a string: ") 
string2 = string1.split()# to convert a string into a list with each of its element of the list being a word from string1 

# when input is a single word
if len(string2) == 1:   
    uniquelist = []      # to have a unique sequence of input elements
    for element in string1:
        if element not in uniquelist:
            uniquelist.append(element)
    for letter in uniquelist:
        counter = 0      # to count the occurence of each word
        for index in range(len(string1)):
            if letter == string1[index]:
                counter+=1
        print("Occurence of",letter,":",counter)
        
# when input is a sentence
else:
    uniquelist2 = []     # to have a unique sequence of input elements
    for element in string2:
        if element not in uniquelist2:
            uniquelist2.append(element)
    for word in uniquelist2:
        counter = 0      # to count the occurence of each word
        for index in range(len(string2)):
            if word == string2[index]:
                counter+=1
        print("Occurence of",word,":",counter) 

# Q.2)

day = int(input("Enter day in DD format: "))
month = int(input("Enter month in MM format: "))
year = int(input("Enter the year in YYYY format: "))

# various conditions on input date
if (1<=day<=31) == False:                            # condition for day
    print("Error: day out of range")    
elif (1<=month<=12) == False:                        # condition for month
    print("Error: month out of range")
elif (1800<=year<=2025) == False:                    # condition for year
    print("Error: year out of range")
elif (year%4 == 0) & (day > 29 & month == 2):        # some other conditions
    print("Error: day out of range")
elif (year%4 != 0) & (day > 28 & month == 2):
    print("Error: day out of range")
elif (month in [4 , 6 , 9 , 11]) & (day == 31):
    print("Error: day out of range")

# various conditions for next day as output
else:
    if (day<=29) & (month!=2):
        print("The next day:- ")
        print(day+1,month,year,sep='/')
    elif (day == 30) & (month in  [4 , 6 , 9 , 11]):  
        print("The next day:- ")
        print("01",month+1,year,sep='/')
    elif (day == 31) & (month in [1 , 3 , 5 , 7 , 8 , 10]):
        print("The next day:- ")
        print("01",month+1,year,sep='/')
    elif (day == 31) & (month == 12):
        print("The next day:- ")
        print("01/01",year+1,sep='/')
    elif (day == 29) & (month == 2) & (year%4==0):   # february and leap year
        print("The next day:- ")
        print("01",month+1,year,sep='/')
    elif (day == 28) & (month == 2) & (year%4==0):
        print("The next day:- ")
        print(day+1,month,year,sep='/')
    elif (day == 28) & (month == 2) & (year%4!=0):
        print("The next day:- ")
        print("01",month+1,year,sep='/')
    else:
        print("Error: wrong input or date out of range")


# Q.3)
limit = int(input("enter number of elements you want in list: "))     # for number of elements in list
list1 = []
for i in range(limit):                                                # for repetetive insertion of elements
    a = int(input("enter a number: "))
    list1.append(a)
list3 = []
for element in list1:                                                 # for storing number and it's square
    a = (element,element**2)
    list3.append(a)
print("output\n",list3)

    
# Q.4)

# to have a mapped sequence of letter-grade,performance & grade-point
dictionary = {10:["A+","Outstanding"],9:["A","Excellent"],8:["B+","Very Good"],7:["B","Good"],6:["C+","Average"],5:["C","Below Average"],4:["D","Poor"]}
gradepoint_input = int(input("Enter a grade point in(4-10): "))

try:
    result = dictionary[gradepoint_input]
    letter_grade = result[0]
    performance = result[1]
    print("Your Grade is",letter_grade,"and",performance,"performance")

except:                                     # to show error if number out of range
    print("Error: input out of range!")     
    
# Q.5)
for column in range(6):
    l = ''                         # used to store letters in a row
    for row in range(65,76-2*i):  
        l+=chr(row)                # using ASCII code and converting into letter 
    print(" "*i,l," "*i) 


# Q.6)
choice = 'Y'
student_details = {}    
while (choice == 'Y'):                           # for iterative input till user says No 
    SID = int(input("Enter SID of student: "))
    name = input("Enter their name: ")
    student_details[SID] = name                  # for storing and displaying student details
    choice = input("Do you want to continue(Y/N): ")
    
# part a)
print("NAME",'\t',"SID")                                
for row in student_details.keys():
    print(student_details[row],row)
print() 

# part b)
print("Sorted dictionary on basis of names:-")      
c = []             # to create a dictionary with interchanged key-value pairs
d = []
student_details2 = {}
for i in student_details.keys():
    c.append(i)
for j in  student_details.values():
    d.append(j)
for k in range(len(d)):
    student_details2[d[k]] = c[k]


for name in sorted(student_details2.keys()):
    print(name,student_details2[name],sep=':',end=',')
print('\n')

# part c)
print("Sorted dictonary on basis of SIDs:-")  
for SID in sorted(student_details.keys()):
    print(SID,student_details[SID],sep=':',end=',') 
print('\n')
    

# part d)
SID_search = int(input("enter the SID for the student to be searched: ")) # to search for a student using SID
print("Student found!!!")
print(student_details[SID_search])'''

'''# Q.7)

limit = int(input("enter the limit till which the series is to be printed: "))

# initial 2 terms of fibbonacci series 
a = 0
b = 1
print("Fibonacci series: ")
print(a,b,sep=",",end=",")
sum_for_avg = 1                 # for counting sum of fibbonacci series

#printing the series
for counter in range(limit-2):
    c = a+b
    sum_for_avg+=c
    print(c,end=",")
    a = b
    b = c
avg = sum_for_avg/limit         # for average of series
print("\naverage of fibbonaci series is",avg)


'# Q.8)
set1 = {1,2,3,4,5}
set2 = {2,4,6,8}
set3 = {1,5,9,13}

newset1 = (set1|set2) - (set1&set2)      # part a)
print(newset1,'\n')

newset2 = (set1|set2|set3) - (set2&set3)-(set3&set1)-(set1&set2)-(set1&set2&set3)  # part b)
print(newset2,'\n')

newset3 = ((set1&set2) | (set1&set3) | (set2&set3)) - (set1&set2&set3)  #part c)
print(newset3,'\n')

newset4 = {1,2,3,4,5,6,7,8,9,10} - set1     # part d)
print(newset4,'\n')

newset5 = {1,2,3,4,5,6,7,8,9,10} - (set1|set2|set3)   # part e)
print(newset5,'\n')
 
