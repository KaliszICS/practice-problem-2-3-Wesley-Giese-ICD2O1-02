'''
    Lesson:  Else If
    Author: Wesley Giese
    Date Created: October 16, 2024
    Date Last Modified: December 3, 2024
'''


def q1(): 
  #Write Assignment code here
  word1 = input("In: ")


  if (word1[-2:] == "ey"):
    print("-eys")
  elif (word1[-1:] == "y"):
    print("-ies")
  elif (word1[-3:] == "ife"):
    print("-ives") 


  else:
    print("-s")

def q2(): 
  #Write Assignment code here
  num1 = int(input("In: "))
  if num1 > 0:
    print(f"{num1} is positive")
  elif (num1 < 0):
    print(f"{num1} is negative")

def q3(): 
  #Write Assignment code here
  word2 = float(input("Input a number: "))
  word3 = float(input("Input a number: "))
  word4 = float(input("Input a number: "))

  if word2 == word3 == word4:
    print("Equilateral")
  
  elif word2 == word3 or word2 == word4 or word3 == word4:
    print("Isosceles")
  elif word2 + word3 < word4 or word2 + word4 < word3 + word4 < word2 or word3 + word4 < word2:
    print("No Triangle")  

  elif word2 != word3 and word4 or word3 != word4 and word2 or word4 != word2 and word3:
    print("Scalene")



  else:                                                   
    print("Invalid Input")

#Do not alter the following code
#Comment out the following code when running your tests

# q1()
# q2()
# q3()