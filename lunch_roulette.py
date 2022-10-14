import os
import random
import time
#Main screen window
error_prompt = "If you feel you have made an error, enter 'back' to go to the \nprevious prompt."
mulligan_error = "Oops! You can only use mulligan three times!"
error_input = "Oops! You have used an incorrect input, please try again."

def start ():
    print("Hi there! Who's Hungry?")
    print("Welcome to Work Lunch Roulette!")
    print("This program will compile a list of surrounding \nrestaurants and randomly generate a lunch option\nfor you and your coworkers in the command line!")
    print("Required inputs will be included in the prompts.\nIf you ever need to return to a previous prompt \nenter 'back'.")
    print("If you are in a rush and don't have time for \nthe full user experience, simply enter 'fast'\nand you will be taken straight to a random option.")
    print("Please keep in mind with the fast choice user \ndata will not be saved.")
    start_input = input("Now you can either enter 'slow' to access previous \nuser data or 'fast' to skip the custom process \nand just get to lunch!\n")

    if start_input == 'slow':
        os.system('CLS')
        user_verify()

    elif start_input == 'fast':
        os.system('CLS')
        lunch_roulette_quick()
    
    else:
        os.system('CLS')
        print(error_input)
        time.sleep (1)
        os.system('CLS')
        start()

def user_verify():
    print("Before we get started, have you used Work Lunch Roulette \nbefore?")
    print("By entering 'yes' your previous choice pool can be pulled \nfrom archives so you don't risk having repeats.")
    print("Entering 'no' will give you a fresh choice pool and save your data as a new user.")
    print(error_prompt)
    previous_user = input("Have you used this program before?\n")

    if previous_user == "yes":
        os.system('CLS')
        welcome_back()

    elif previous_user == "no":
        os.system('CLS')
        fresh_run()

    elif previous_user == "back":
        os.system('CLS')
        start()

    else:
        os.system('CLS')
        print(error_input)
        time.sleep (1)
        os.system('CLS')
        user_verify()

def welcome_back():
    print("Welcome back! As a prevous user, would you like to \nkeep your previous choice pool or reset with a new \none?")
    print("It is fine to continue with an old pool, but we \nrecommend resetting every week to keep options for \nthe program up to date.")
    print("Keep in mind that once you have reset your choice \npool it cannot be undone.")
    print("To start over from scratch enter 'reset'")
    print("To continue with previous list enter 'continue'")
    print(error_prompt)
    r_input = input()

    if r_input == 'reset':
        os.system('CLS')
        reset_verify()
    elif r_input == 'continue':
        os.system('CLS')
        user_run()
    
    elif r_input == 'back':
        os.system('CLS')
        user_verify()
    
    else:
        os.system('CLS')
        print(error_input)
        time.sleep(1)
        os.system('CLS')
        welcome_back()

def fresh_run():
    print("Welcome new user!\n")
    print("Now for the fun part, enter 'engage' to begin \nrandom selection of your potential lunch option!")
    print(error_prompt)
    #Insert initialpool.txt here and overwrite custompool.txt with initialpool.txt
    begin = input()
    
    if begin == "engage":
        os.system('CLS')
        lunch_roulette_quick()
        #lunch_roulette()

    elif begin == "back":
        os.system('CLS')
        user_verify()

    else:
        os.system('CLS')
        print(error_input)
        time.sleep(1)
        os.system('CLS')
        fresh_run()

def user_run():
    print("Now for the fun part, enter 'engage' to begin random selection of your potential lunch option from \nyour previous choice pool!")
    print(error_prompt)
    u_input = input()

    if u_input == 'engage':
        os.system('CLS')
        lunch_roulette_quick()

    if u_input == 'back':
        os.system('CLS')
        welcome_back()

    else:
        os.system('CLS')
        print(error_input)
        time.sleep(1)
        os.system('CLS')
        user_run()

    #Initialize custompool.txt here

def reset_verify():
    print("Are you sure you want to reset? Once you reset it cannot be undone.")
    reset = input("Input yes to reset. Input no to continue with current list.\n")
    
    if reset == "yes":
        os.system('CLS')
        fresh_run()
        
    if reset == "no":
        os.system('CLS')
        user_run()

    else:
        os.system('CLS')
        print(error_input)
        time.sleep(1)
        os.system('CLS')
        reset_verify()

#def lunch_roulette():

def lunch_roulette_quick():
    print("Congratulations! Work Lunch Roulette has chosen Burger King as your lunch spot for the day!")
    print("Thank you for using Work Lunch Roulette! Goodbye!")
    
#def mulligan():

#def mulligan_error():

#def farewell():

#def lunch_confirm():

#def sorry():

os.system('CLS')
start()