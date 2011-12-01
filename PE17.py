#create an empty array
#fill in the array with pascal's triangle like specifications  

'''

one = 3
two = 3
three = 5
four = 4
five = 4
six = 3
seven = 5
eight = 5
nine = 4

ten = 3
eleven = 6
twelve = 6
thirteen = 8
fourteen = 8
fifteen = 7
sixteen = 7
seventeen = 9
eighteen = 8
nineteen = 8

twenty = 6 
thirty = 6
forty = 5
fifty = 5
sixty = 5
seventy = 7
eighty = 6
ninety = 6

one hundred and = 13 

'''
One_Nine = 3+3+5+4+4+3+5+5+4 
print One_Nine

Ten_Nineteen = 3+6+6+8+8+7+7+9+8+8
print Ten_Nineteen 

Twenty_NN = 10*(6+6+5+5+5+7+6+6) + One_Nine*8
print Twenty_NN

FirstHundred = One_Nine+Ten_Nineteen+Twenty_NN
print FirstHundred 

OneHundred = 10 + 99*13 + FirstHundred  
TwoHundred = OneHundred
ThreeHundred = 12 + 99*15 + FirstHundred
FourHundred = 11+ 99*14 +FirstHundred
FiveHundred = FourHundred
SixHundred = OneHundred
SevenHundred = ThreeHundred
EightHundred = ThreeHundred
NineHundred = FourHundred

OneThousand = 11

Answer = FirstHundred + OneHundred*3 + ThreeHundred*3 + FourHundred*3 + OneThousand

print Answer

import math, time
init_time = time.time()





print time.time() - init_time