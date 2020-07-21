'''
To see how much PyInputPlus is doing for you, try re-creating the multiplication quiz project 
on your own without importing it. This program will prompt the user with 10 multiplication 
questions, ranging from 0 × 0 to 9 × 9. You’ll need to implement the following features:

    If the user enters the correct answer, the program displays “Correct!” for 1 second and moves on to the next question.
    The user gets three tries to enter the correct answer before the program moves on to the next question.
    Eight seconds after first displaying the question, the question is marked as incorrect even if the user enters the correct answer after the 8-second limit.
'''

#basically the same code as proposed in chapter 8, but with f-strings instead of %s - replacement
#and added +1 to question number, so that the first question desn't start at 0

import pyinputplus as pyip
import random, time

num_of_questions = 10
num_correct_answers = 0

for question_number in range (num_of_questions):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    correct_answer = num1*num2
    prompt = f"{question_number+1}: {num1} x {num2} = "

    try:
        pyip.inputStr   (prompt, allowRegexes = [f"{correct_answer}"],
                         blockRegexes = [(".*", "Incorrect!")],
                         timeout = 8, limit = 3)
    except pyip.TimeoutException:
        print ("Out of time!")
    except pyip.RetryLimitException:
        print ("Out of tries!")
    else:                                                                   #try-except statement can use a [else:] statement at the end, entering if no exception was raised --- ALTHOUGH: it would probably make no difference to just put it under the pyip.inputStr function
        print ("Correct!")
        num_correct_answers += 1
    
    time.sleep(1)
    print (f"Score: {num_correct_answers}/{num_of_questions}\n")