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
    print("Required inputs will be included in the prompts. If \nyou ever need to return to a previous prompt input \n'back'.")
    input("Now press enter to get started!")
    os.system('CLS')
    user_verify()

def user_verify():
    print("Before we get started, have you used Work Lunch Roulette \nbefore?")
    print("By entering 'yes' your previous choice pool can be pulled \nfrom archives so you don't risk having repeats.")
    print("Entering no will give you a fresh choice pool and save your data as a new user.")
    print(error_prompt)
    previous_user = input("Have you used this program before? ")
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
    print("It is fine to continue with an old pool, but we \nrecommend resetting every week to keep option for \nthe program up to date.")
    print("Keep in mind that once you have reset your choice \npool it cannot be undone.")
    print("To start over from scratch enter 'reset'")
    print("To continue with previous list enter 'continue'")
    print(error_prompt)

def fresh_run():
    print("Now for the fun part, enter 'engage' to begin \nrandom selection of your potential lunch option!")
    print(error_prompt)
    #Insert initialpool.txt here and overwrite custompool.txt with initialpool.txt
    begin = input()
    if begin == "engage":
        os.system('CLS')
        #lunch_roulette()
    else:
        os.system('CLS')
        print(error_input)
        time.sleep(1)
        os.system('CLS')
        fresh_run()

def user_run():
    print("Now for the fun part, enter 'engage' to begin random selection of your potential lunch option from \nyour previous choice pool!")
    print(error_prompt)
    #Initialize custompool.txt here

def reset_verify():
    print("Are you sure you want to reset? Once you reset it cannot be undone.")
    reset = input("Input yes to reset. Input no to continue with current list.")
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


start()