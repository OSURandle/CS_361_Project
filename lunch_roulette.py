import os
import random
import time
import requests
import json
import string

#Main screen window
error_prompt = "If you feel you have made an error, enter 'back' to go to the \nprevious prompt."
mulligan_error = "Oops! You can only use mulligan three times!"
error_input = "Oops! You have used an incorrect input, please try again."

def startmsg():
    os.system('CLS')
    print("Hi there! Who's Hungry?")
    print("Welcome to Work Lunch Roulette!")
    print("This program will compile a list of surrounding \nrestaurants and randomly generate a lunch option\nfor you and your coworkers in the command line!")
    print("Required inputs will be included in the prompts.\nIf you ever need to return to a previous prompt \nenter 'back'.")
    print("If you are in a rush and don't have time for \nthe full user experience, simply enter 'fast'\nand you will be taken straight to a random option.")
    print("Please keep in mind with the fast choice user \ndata will not be saved.")
    start_input = input("Now you can either enter 'slow' to access previous \nuser data or 'fast' to skip the custom process \nand just get to lunch!\n")
    start(start_input)

def start (start_input):
    
    if start_input == "slow":
        user_verify_msg()

    elif start_input == "fast":
        lunch_roulette_quick()
    
    else:
        os.system('CLS')
        print(error_input)
        time.sleep (1)
        startmsg()

def user_verify_msg():
    os.system('CLS')
    print("Before we get started, have you used Work Lunch Roulette \nbefore?")
    print("By entering 'yes' your previous choice pool can be pulled \nfrom archives so you don't risk having repeats.")
    print("Entering 'no' will give you a fresh choice pool and save your data as a new user.")
    print(error_prompt)
    previous_user = input("Have you used this program before?\n")
    user_verify(previous_user)

def user_verify(previous_user):
    if previous_user == "yes":
        welcome_back_msg()

    elif previous_user == "no":
        fresh_run_msg()

    elif previous_user == "back":
        startmsg()

    else:
        os.system('CLS')
        print(error_input)
        time.sleep (1)
        user_verify_msg()

def welcome_back_msg():
    os.system('CLS')
    print("Welcome back! As a prevous user, would you like to \nkeep your previous choice pool or reset with a new \none?")
    print("It is fine to continue with an old pool, but we \nrecommend resetting every week to keep options for \nthe program up to date.")
    print("Keep in mind that once you have reset your choice \npool it cannot be undone.")
    print("To start over from scratch enter 'reset'")
    print("To continue with previous list enter 'continue'")
    print(error_prompt)
    r_input = input()
    welcome_back(r_input)

def welcome_back(r_input):
    if r_input == "reset":
        reset_verify_msg()

    elif r_input == "continue":
        user_run_msg_1()
    
    elif r_input == "back":
        user_verify_msg()
    
    else:
        os.system('CLS')
        print(error_input)
        time.sleep(1)
        welcome_back_msg()

def fresh_run_msg():
    os.system('CLS')
    print("Welcome new user!\n")
    print("Now for the fun part, enter 'engage' to begin \nrandom selection of your potential lunch option!")
    print(error_prompt)
    begin = input()
    fresh_run(begin)

def fresh_run(begin):

    if begin == "engage":  
        reset()
        lunch_roulette()
        

    elif begin == "back":
        user_verify_msg()

    else:
        os.system('CLS')
        print(error_input)
        time.sleep(1)
        fresh_run_msg()

def user_run_msg_1():
    os.system('CLS')
    print("As a previous user, would you like to take this opportunity to add/remove options from your current list?\n Input 'custom' when prompted to customize your list.")
    print(error_prompt)
    u_input = input()
    custom(u_input)

def user_run_msg_2():    
    print("Now for the fun part, enter 'engage' to begin random selection of your potential lunch option from \nyour previous choice pool!")
    print(error_prompt)
    u_input = input()
    user_run(u_input)

def custom(u_input):
    if u_input == "custom":
        add_or_remove()
    elif u_input == "continue":
        user_run_msg_2()
    elif u_input == "back":
        welcome_back_msg()
    else:
        os.system('CLS')
        print(error_input)
        time.sleep(1)
        user_run_msg_1()

def user_run(u_input):
    if u_input == "engage":
        lunch_roulette()

    elif u_input == "back":
        welcome_back_msg()

    else:
        os.system('CLS')
        print(error_input)
        time.sleep(1)
        user_run_msg_2()

def reset_verify_msg():
    os.system('CLS')
    print("Are you sure you want to reset? Once you reset it cannot be undone.")
    reset = input("Input yes to reset. Input no to continue with current list.\n")
    reset_verify(reset)

def reset_verify(reset):
    if reset == "yes":
        fresh_run_msg()
        
    elif reset == "no":
        user_run_msg_1()  

    else:
        os.system('CLS')
        print(error_input)
        time.sleep(1)
        reset_verify_msg()

def farewell(d_input):
    os.system('CLS')
    remove(d_input)
    print("Thank you for using Work Lunch Roulette! Goodbye!") 
    time.sleep(1)
    os.system('CLS')

def farewell_m(d_input):
    os.system('CLS')
    print(f"Congratulations! Work Lunch Roulette has chosen {d_input} as your lunch spot for the day! Goodbye!")
    time.sleep(5)
    os.system('CLS')
    
def mulligan():
    response = requests.get("https://web-production-16ee.up.railway.app/")
    roulette = response.text
    parsed = json.loads(roulette)
    roulette_list = parsed ['Restaurants']
    roulette_list = roulette_list.translate(str.maketrans('', '', string.punctuation))
    d_input = random.choice(roulette_list.splitlines())
    print(d_input)
    mull_d = input("Are you satisfied? Input 'Yes' or 'No'")
    if mull_d == 'Yes':
        farewell_m(d_input)
    if mull_d == 'No':
        return
    else:
        mull_error()

    
def mulligan_msg(d_input):
    print("So you want a do over eh? Well here you go! Keep in mind this can only be done three times with the third choice being the default")
    mull = 0
    max_mull = 3
    while mull < max_mull:
        mulligan()
        mull += 1
    print(mulligan_error)
    time.sleep(1)
    farewell_m(d_input)

def mull_error():
        os.system('CLS')
        print(error_input)
        time.sleep(1)
        mulligan()

def decision_msg(d_input):
    os.system('CLS')
    print(f"Congratulations! Work Lunch Roulette has chosen {d_input} as your lunch spot for the day!")
    print("If you are not satisfied with this option, you may opt for a redo up to 3 times per session by entering 'mulligan'")
    print("If you are satisfied with this decision enter 'done' and the list will update and the program will close")
    f_input = input("Input 'mulligan' for a do over, input 'done' to finish\n")
    decision (f_input, d_input)
    
def decision(f_input, d_input):
    if f_input == "mulligan":
        mulligan_msg(d_input)

    if f_input == "done":
        farewell(d_input)
    
    else:
        os.system('CLS')
        print(error_input)
        time.sleep(1)
        decision_msg()

def add_or_remove():
    input_custom = input("Would you like to add or remove and item from the current user list? Input 'add' or 'remove'?\n If you have reached this page in error please input 'back' to return to the previous selection")
    if input_custom == 'add':
        add_new()
    elif input_custom == 'remove':
        remove()
    elif input_custom == 'back':
        custom()
    else:
        os.system('CLS')
        print(error_input)
        time.sleep(1)
        add_or_remove()

# Adds a new restaurant to the current list
def add_new():
    os.system('CLS')
    print("Please choose restaurant you would like to add to your list.")
    requests.post('https://web-production-16ee.up.railway.app/add', data = {"name":input()+"\n"})
    print("Restaurant has been added!")
    add_or_remove()

# Sets the initial set of restaurants
def initial():
    
    requests.post('https://web-production-16ee.up.railway.app/add', data = {"name":"Burger King\n"})
    requests.post('https://web-production-16ee.up.railway.app/add', data = {"name": "Taco Bell\n"})
    requests.post('https://web-production-16ee.up.railway.app/add', data = {"name": "Hardees\n"})
    requests.post('https://web-production-16ee.up.railway.app/add', data = {"name": "The Grill\n"})
    requests.post('https://web-production-16ee.up.railway.app/add', data = {"name": "The Camphouse\n"})
      
def remove():
    os.system('CLS')
    response = requests.get("https://web-production-16ee.up.railway.app/")
    roulette = response.text
    parsed = json.loads(roulette)
    roulette_list = parsed ['Restaurants']
    roulette_list = roulette_list.translate(str.maketrans('', '', string.punctuation))
    print(roulette_list)
    print("Please choose which restaurant you would like to remove")
    requests.delete('https://web-production-16ee.up.railway.app/remove', data = {"name":input()+"\n"})

# Removes modified lists and returns initial list
def reset():
    requests.delete("https://web-production-16ee.up.railway.app/remove-all")
    initial()

def lunch_roulette():
    os.system('CLS')
    response = requests.get("https://web-production-16ee.up.railway.app/")
    roulette = response.text
    parsed = json.loads(roulette)
    roulette_list = parsed ['Restaurants']
    roulette_list = roulette_list.translate(str.maketrans('', '', string.punctuation))
    d_input = random.choice(roulette_list.splitlines())
    decision_msg(d_input)
    
def lunch_roulette_quick():
    os.system('CLS')
    response = requests.get("https://web-production-16ee.up.railway.app/")
    roulette = response.text
    parsed = json.loads(roulette)
    roulette_list = parsed ['Restaurants']
    roulette_list = roulette_list.translate(str.maketrans('', '', string.punctuation))
    d_input = random.choice(roulette_list.splitlines())
    print(f"Congratulations! Work Lunch Roulette has chosen {d_input} as your lunch spot for the day! Goodbye!")
    time.sleep(5)
    os.system('CLS')


    
os.system('CLS')
startmsg()


