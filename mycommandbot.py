import time
import random

def show_commands():
    commands2 = [
        "-ask age --- gives you the age of the bot",
        "-ask name --- gives you the name of the bot",
        "-ask gender --- gives you the gender of the bot",
        "-ask hobbie --- gives you one hobbie of the bot",     
        "-ask favorite food --- gives you the favorite food of the bot",
        "-ask favorite color --- gives you the favorite color of the bot",
        "commands --- shows this command list",
        "exit --- exits the chat"
    ]
    print("Available commands:")
    for cmd in commands2:
        print(cmd)

def handle_command(command, bot_name):
    if command == "-ask age":
        print("wowwww i didn't think you were that interested in me, i'm so happyyyyyy :) anyways... i'm 16 years old")
    elif command == "-ask name":
        print(f"my name is {bot_name}")
    elif command == "-ask gender":
        print("i don't have a gender, i am a bot... :(")
    elif command == "-ask hobbie":
        hobbies = ["talking to humans", "getting to know new things", "sleeping~", "coding"]
        print("idk anything about your hobbie but you can tell me with the command 'tell hobbie'")
        print("my hobbie is: " + random.choice(hobbies))
    elif command == "-ask favorite food":
        fav_foods = ['pizza', 'burger', 'tacos', "Caesar salad", "chicken and rice (for protein~)"]
        print("i also don't know yours so please tell meeeee 😭 just type 'tell favorite food'")
        print("my favorite food is: " + random.choice(fav_foods))
    elif command == "-ask favorite color":
        fav_colors = ['dark blue', 'purple', 'pink', 'red', 'green']
        print("i hope our favorite colors match~")
        print("my favorite color is: " + random.choice(fav_colors))
    elif command == "commands":
        show_commands()
    else:
        print("Sorry, i'm still learning... use 'commands' to see the commands")

def command_bot():
    print("this bot is still in development, so expect some things not to work :)")
    print("give the bot a name ")
    bot_name = input(": ")
    if bot_name == "":
        bot_name = "Unnamed Bot"
    print(f"hiii!!! i am {bot_name}, i really like this name :) tyyyyyyyy ")
    

    time.sleep(2)
    print("type 'commands' to see the commands")
    print("when using commands include the '-' at the beginning")
    
    while True:
        user_input = input(": ").lower().strip()
        if user_input == "exit":
            print("bye bye :(")
            break
        handle_command(user_input, bot_name)

command_bot()
