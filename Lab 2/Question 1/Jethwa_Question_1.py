# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 22:21:14 2022

@author: premj
"""
def main():
    print('Enter Five Test Scores between (0-100):')
    print()
    score1 = get_valid_score()                #Calling get_valid_score
    print('Final Test 1 score :', score1)
    score2 = get_valid_score()                #Calling get_valid_score
    print('Final Test 2 score :', score2)
    score3 = get_valid_score()                #Calling get_valid_score
    print('Final Test 3 score :', score3)
    score4 = get_valid_score()                #Calling get_valid_score
    print('Final Test 4 score :', score4)
    score5 = get_valid_score()                #Calling get_valid_score
    print('Final Test 5 score :', score5)
    print()
    print('Grade for Test 1 : ', determine_grade(score1))       #Calling determine_grade
    print('Grade for Test 2 : ', determine_grade(score2))       #Calling determine_grade
    print('Grade for Test 3 : ', determine_grade(score3))       #Calling determine_grade
    print('Grade for Test 4 : ', determine_grade(score4))       #Calling determine_grade
    print('Grade for Test 5 : ', determine_grade(score5))       #Calling determine_grade
    print('Average test score : {:.2f}'.format(calc_average(score1, score2, score3, 
          score4, score5)))
    print('Letter grade for Average :', determine_grade(calc_average(score1, 
          score2, score3, score4, score5)))
    
#Function definition for calc_average       
def calc_average(score1, score2, score3, score4, score5):
    return (score1 + score2 + score3 + score4 + score5) / 5.0

#Function definition for determine_grade
def determine_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score <= 89:
        return 'B'
    elif 70 <= score <= 79:
        return 'C'
    elif 60 <= score <= 69:
        return 'D'
    else:
        return 'F'

#Function definition for get_valid_score
def get_valid_score():
    score = input('Enter score : ')
    while not is_valid_score(score):        # calling is_valid_score
        score = input('Enter valid score : ')
    return int(score)

#Function definition for is_valid_score
def is_valid_score(s):
    isValid = False
    try:
        num = int(s)
        if not s.isdigit():
            raise ValueError()
        elif num < 0 or num > 100:
            raise ValueError()
        else:
            isValid = True
    except ValueError:
        isValid = False
    return isValid
 
#Calling main method   
main()