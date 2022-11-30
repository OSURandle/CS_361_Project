import os
import random
import time
import requests
import json
import string
import sys

#Error Prompts
error_prompt = "If you feel you have made an error, enter 'back' to go to the \nprevious prompt."
mulligan_error = "Oops! You can only use mulligan three times!"
error_input = "Oops! You have used an incorrect input, please try again."

# Introduction to program provides options for user inputs
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

# Function takes the user input from startmsg to determine next step to take for the user
def start (start_input):
    #Slow mode is normal path through program, fast performs roulette function immediately
    if start_input == "slow":
        user_verify_msg()
    elif start_input == "fast":
        lunch_roulette_quick()
    else:
        os.system('CLS')
        print(error_input)
        time.sleep (1)
        startmsg()

# Prompt for new or current user verification
def user_verify_msg():
    os.system('CLS')
    print("Before we get started, have you used Work Lunch Roulette \nbefore?")
    print("By entering 'yes' your previous choice pool can be pulled \nfrom archives so you don't risk having repeats.")
    print("Entering 'no' will give you a fresh choice pool and save your data as a new user.")
    print(error_prompt)
    previous_user = input("Have you used this program before?\n")
    user_verify(previous_user)

# Function takes the user input from user_verify_msg to determine whether to proceed as new or previous user
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

# Prompt for returning users gives option for a fresh list or previously used list
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

# Function takes user input from welcome_back_msg to determine if the list will be reset
def welcome_back(r_input):
    # 'reset' sends user to confirmation before clearing list
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

# Prompt acts as a final confirmation for previous users resetting to default list
def reset_verify_msg():
    os.system('CLS')
    print("Are you sure you want to reset? Once you reset it cannot be undone.")
    reset = input("Input yes to reset. Input no to continue with current list.\n")
    reset_verify(reset)

# Function takes user input from reset_verify_msg to determine if saved list will be reset
def reset_verify(reset):
    # 'yes' takes user to fresh run and effectively makes them a new user
    if reset == "yes":
        fresh_run_msg()
    # 'no' takes user back to previous user run without resetting the list
    elif reset == "no":
        user_run_msg_1()  
    else:
        os.system('CLS')
        print(error_input)
        time.sleep(1)
        reset_verify_msg()

# Prompt for giving the user the option to customize their list by adding or removing
def user_run_msg_1():
    os.system('CLS')
    print("As a previous user, would you like to take this opportunity to add/remove options from your current list?\n Input 'custom' to customize your list.\n Input 'continue' to move on without customization")
    print(error_prompt)
    u_input = input()
    custom(u_input)

#Prompt for giving the user the option to use the roulette prompt
def user_run_msg_2():    
    os.system('CLS')
    print("Now for the fun part, enter 'engage' to begin random selection of your potential lunch option from \nyour previous choice pool!")
    print(error_prompt)
    u_input = input()
    user_run(u_input)

# Function takes user input from user_run_msg_1 to determine if the list will be customized
def custom(u_input):
    # 'custom' input takes user to function for adding and removing items from the list
    if u_input == "custom":
        add_or_remove()
    # 'continue' input takes user to next step of user input for lunch_roulette
    elif u_input == "continue":
        user_run_msg_2()
    elif u_input == "back":
        welcome_back_msg()
    else:
        os.system('CLS')
        print(error_input)
        time.sleep(1)
        user_run_msg_1()

# Function that accepts input from user to add or remove items from the list 
def add_or_remove():
    input_custom = input("Would you like to add or remove an item from the current user list? Input 'add' or 'remove'?\nIf you have reached this page in error please input 'back' to return to the previous selection\n")
    if input_custom == 'add':
        add_new()
    elif input_custom == 'remove':
        remove()
    elif input_custom == 'back':
        user_run_msg_1()
    else:
        os.system('CLS')
        print(error_input)
        time.sleep(1)
        add_or_remove()

# Adds a new restaurant to the current list
def add_new():
    os.system('CLS')
    #generate_list displays list before item has been added
    generate_list()
    print("Please choose restaurant you would like to add to your list.")
    #user input is applied to the database from microservice
    requests.post('https://web-production-16ee.up.railway.app/add', data = {"name":input()+"\n"})
    # new list is displayed with added input for user verification
    generate_list()
    print("Restaurant has been added!")
    #function returns to add_or_remove() if further customization is necessary
    add_or_remove()

# Removes restaurant from the current list
def remove():
    os.system('CLS')
    # list is displayed prior to modification
    generate_list()
    print("Please choose which restaurant you would like to remove")
    # User input removes item from the database
    requests.delete('https://web-production-16ee.up.railway.app/remove', data = {"name":input()+"\n"})
    # The updated list is displayed as user verification
    generate_list()
    print("Restaurant has been removed!")
    # Return to add_or_remove if more customization is necessary
    add_or_remove()

# Function takes user input from user_run_msg_2 to determine if lunch_roulette will be enabled
def user_run(u_input):
    # 'engage' moves on to lunch_roulette function
    if u_input == "engage":
        lunch_roulette()
    elif u_input == "back":
        welcome_back_msg()
    else:
        os.system('CLS')
        print(error_input)
        time.sleep(1)
        user_run_msg_2()

# Prompt for new user to enable lunch_roulette
def fresh_run_msg():
    os.system('CLS')
    print("Welcome new user!\n")
    print("Now for the fun part, enter 'engage' to begin \nrandom selection of your potential lunch option!")
    print(error_prompt)
    begin = input()
    fresh_run(begin)

# Function takes user input from fresh_run_msg to begin lunch_roulette run
def fresh_run(begin):
    if begin == "engage":  
    # Only with new user, the list is reset to default values before lunch_roulette initializes
        reset()
        lunch_roulette()
    elif begin == "back":
        user_verify_msg()
    else:
        os.system('CLS')
        print(error_input)
        time.sleep(1)
        fresh_run_msg()

# Function takes random selection from microservice database
def lunch_roulette():
    os.system('CLS')
    response = requests.get("https://web-production-16ee.up.railway.app/")
    roulette = response.text
    # Microservice database is converted into list that can be manipulated by function
    parsed = json.loads(roulette)
    roulette_list = parsed ['Restaurants']
    roulette_list = roulette_list.translate(str.maketrans('', '', string.punctuation))
    d_input = random.choice(roulette_list.splitlines())
    # Result is pushed along to decision_msg prompt for user verification
    decision_msg(d_input)
    
# Function for user to utilize mulligan function
def mulligan_msg(d_input):
    os.system('CLS')
    print("So you want a do over eh? Well here you go! Keep in mind this can only be done three times with the third choice being the default")
    mull = 0
    max_mull = 3
    # This loop counts up to 3 attempts of mulligan and then ends the loop
    while mull < max_mull:
        mulligan()
        mull += 1
    print(mulligan_error)
    time.sleep(1)
    # Whatever the result of mulligan is is carried over to farewell_m
    farewell_m(d_input)

# Helper function for mulligan_msg that runs extra roulette option for the user 
def mulligan():
    response = requests.get("https://web-production-16ee.up.railway.app/")
    roulette = response.text
    parsed = json.loads(roulette)
    roulette_list = parsed ['Restaurants']
    roulette_list = roulette_list.translate(str.maketrans('', '', string.punctuation))
    d_input = random.choice(roulette_list.splitlines())
    print(d_input)
    mull_d = input("Are you satisfied? Input 'yes' or 'no'")
    # 'yes' takes user to farewell_m with successful decision
    if mull_d == 'yes':
        farewell_m(d_input)
    # 'no' takes user back to mulligan_msg to cycle through loop again
    if mull_d == 'no':
        return
    else:
        mull_error()

# Displays error message for incorrect input from mulligan
def mull_error():
        os.system('CLS')
        print(error_input)
        time.sleep(1)
    # Returns user to previous function to use correct input
        mulligan()

# Prompt that displays result of lunch_roulette and gives option for mulligan
def decision_msg(d_input):
    os.system('CLS')
    print(f"Congratulations! Work Lunch Roulette has chosen {d_input} as your lunch spot for the day!")
    print("If you are not satisfied with this option, you may opt for a redo up to 3 times per session by entering 'mulligan'")
    print("If you are satisfied with this decision enter 'done' and the list will update and the program will close")
    f_input = input("Input 'mulligan' for a do over, input 'done' to finish\n")
    decision (f_input, d_input)

# Function takes input from decision_msg to determine if the lunch_roulette result is accepted or if mulligan will occur
def decision(f_input, d_input):
    # 'mulligan' takes user to mulligan function for up to 3 new attempts
    if f_input == "mulligan":
        mulligan_msg(d_input)
    # 'done' takes user to farewell function 
    if f_input == "done":
        farewell(d_input)
    else:
        os.system('CLS')
        print(error_input)
        time.sleep(1)
        decision_msg()

# Function removes the final decision from lunch_roulette from the list
def remove_decision(d_input):
    requests.delete('https://web-production-16ee.up.railway.app/remove', data = {"name":d_input+"\n"})
    return
    
# Removes modified lists and returns initial list
def reset():
    requests.delete("https://web-production-16ee.up.railway.app/remove-all")
    # Generate default list
    initial()

# Sets the initial set of restaurants
def initial():
    requests.post('https://web-production-16ee.up.railway.app/add', data = {"name":"Burger King\n"})
    requests.post('https://web-production-16ee.up.railway.app/add', data = {"name": "Taco Bell\n"})
    requests.post('https://web-production-16ee.up.railway.app/add', data = {"name": "Hardees\n"})
    requests.post('https://web-production-16ee.up.railway.app/add', data = {"name": "The Grill\n"})
    requests.post('https://web-production-16ee.up.railway.app/add', data = {"name": "The Camphouse\n"})
    requests.post('https://web-production-16ee.up.railway.app/add', data = {"name": "Obys\n"})
    requests.post('https://web-production-16ee.up.railway.app/add', data = {"name": "Buffalo Wild Wings\n"})
    requests.post('https://web-production-16ee.up.railway.app/add', data = {"name": "Stagger Inn\n"})
    requests.post('https://web-production-16ee.up.railway.app/add', data = {"name": "Moes\n"})

# Function generates the current list from the microservice database
def generate_list():
    response = requests.get("https://web-production-16ee.up.railway.app/")
    roulette = response.text
    parsed = json.loads(roulette)
    roulette_list = parsed ['Restaurants']
    roulette_list = roulette_list.translate(str.maketrans('', '', string.punctuation))
    print(roulette_list)

# Similar to lunch_roulette function but only provides result with no option for modification
def lunch_roulette_quick():
    os.system('CLS')
    response = requests.get("https://web-production-16ee.up.railway.app/")
    roulette = response.text
    parsed = json.loads(roulette)
    roulette_list = parsed ['Restaurants']
    roulette_list = roulette_list.translate(str.maketrans('', '', string.punctuation))
    d_input = random.choice(roulette_list.splitlines())
    print(f"Congratulations! Work Lunch Roulette has chosen {d_input} as your lunch spot for the day! Goodbye!")
    time.sleep(4)
    sys.exit()

# Function displays result from mulligan function and closes program
def farewell_m(d_input):
    os.system('CLS')
    print(f"Congratulations! Work Lunch Roulette has chosen {d_input} as your lunch spot for the day! Goodbye!")
    sys.exit()

# Function takes result from lunch_roulette and removes it from the current list
def farewell(d_input):
    os.system('CLS')
    # The result given by a standard lunch_roulette run is removed from the user list to avoid repeats in the future
    remove_decision(d_input)
    print("Thank you for using Work Lunch Roulette! Goodbye!") 
    time.sleep(1)
    sys.exit()

    

startmsg()


