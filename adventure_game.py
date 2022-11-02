import time
import random


def print_pause(string, pause):
    print(string)
    time.sleep(pause)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 == response:
            break
        elif option2 == response:
            break
        else:
            print_pause("Not a valid response!", 2)
    return response


def valid_input_aisle(prompt, option1, option2,
                      option3, option4, option5, option6):
    while True:
        aisle_chosen = input(prompt).lower()
        if option1 == aisle_chosen:
            break
        elif option2 == aisle_chosen:
            break
        elif option3 == aisle_chosen:
            break
        elif option4 == aisle_chosen:
            break
        elif option5 == aisle_chosen:
            break
        elif option6 == aisle_chosen:
            break
        else:
            print_pause("Not a valid choice!", 2)
    return aisle_chosen


def intro(list):
    print_pause(
        "Your mom gives you a list of grocery items"
        " you must buy at the supermarket.", 3)
    print_pause(list, 2)
    print_pause(
        "You only have 25 minutes to get the"
        " groceries before your mom gets mad.", 3)
    print_pause("You enter the supermarket.", 2)
    print_pause("Where do you go?", 2)


def aisle_prompt(list, time_left):
    if time_left <= 0:
        print_pause("YOU'RE OUT OF TIME!", 2)
        print_pause("Your mom disowns you for being late.", 2)
        print_pause("GAME OVER", 2)
        response = valid_input(
            "Would you like to play again? Yes or No\n", "yes", "no")
        if "yes" == response:
            play_game()
        elif "no" == response:
            print_pause("Thanks for playing!", 2)

    elif time_left > 0 and list == []:
        print_pause("You got all of the grocery items on time!", 2)
        print_pause(
            "Your mom is proud of you for not being late "
            "and decides to give you $10,000", 2)
        print_pause("YOU WIN!", 2)
        response = valid_input(
            "Would you like to play again? Yes or No\n", "yes", "no")
        if "yes" == response:
            play_game()
        elif "no" == response:
            return print_pause("Thanks for playing!", 2)

    else:
        aisle_chosen = valid_input_aisle(
            "Pick an aisle number.\n  1 - Produce\n  2 - Dairy\n  3 - Chips\n"
            "  4 - Seasoning\n  5 - Bakery\n  6 - "
            "Drinks\n", "1", "2", "3", "4", "5", "6")
        if aisle_chosen == "1":
            aisle1(list, time_left)
        elif aisle_chosen == "2":
            aisle2(list, time_left)
        elif aisle_chosen == "3":
            aisle3(list, time_left)
        elif aisle_chosen == "4":
            aisle4(list, time_left)
        elif aisle_chosen == "5":
            aisle5(list, time_left)
        elif aisle_chosen == "6":
            aisle6(list, time_left)


def aisle1(list, time_left):
    if "Onions" in list:
        print_pause(
            "You go down aisle 1 and find the onions. "
            "You put the onions in your cart.", 2)
        list.remove("Onions")
        print_pause("Your remaining grocery list", 2)
        print_pause(list, 2)
        time_left -= 4
        print_pause(str(time_left)+" minutes remaining!", 2)
        print_pause(
            "You see your friend from high school standing in the aisle.", 2)
        response = valid_input("Do you approach her? Yes or No\n", "yes", "no")
        if "yes" == response:
            print_pause("You approach your friend from high school.", 2)
            print_pause(
                "She talks to you about her life and "
                "ends up wasting 5 minutes of your time", 2)
            time_left -= 5
            print_pause(str(time_left)+" minutes remaining!", 2)
            aisle_prompt(list, time_left)
        elif "no" == response:
            print_pause("You ignore her and proceed with your duties.", 2)
            aisle_prompt(list, time_left)

    else:
        print_pause("You already have onions.", 2)
        print_pause("You get distracted by the cucumbers.", 2)
        time_left -= random.randint(1, 10)
        print_pause(str(time_left)+" minutes remaining!", 2)
        aisle_prompt(list, time_left)


def aisle2(list, time_left):
    if "Milk" in list:
        print_pause(
            "You go down aisle 2 and find the milk. "
            "You put the milk in your cart.", 2)
        list.remove("Milk")
        print_pause("Your remaining grocery list", 2)
        print_pause(list, 2)
        time_left -= 4
        print_pause(str(time_left)+" minutes remaining!", 2)
        print_pause("You spot something behind a carton of milk", 2)
        response = valid_input(
            "Do you stick your hand behind the carton "
            "of milk to grab it? Yes or No\n", "yes", "no")
        if "yes" == response:
            print_pause("You stick your hand behind the carton of milk.", 2)
            mystery = random.choice(["rat", random.choice(list)])
            if mystery == "rat":
                print_pause("A rat bites your hand!", 2)
                print_pause("You whimper in pain for 5 minutes", 2)
                time_left -= 5
                print_pause(str(time_left)+" minutes remaining!", 2)
                aisle_prompt(list, time_left)

            else:
                print_pause("You grab "+mystery +
                            " from behind the carton of milk!", 2)
                list.remove(mystery)
                print_pause("Your remaining grocery list", 2)
                print_pause(list, 2)
                aisle_prompt(list, time_left)
        elif "no" == response:
            print_pause("You ignore it and proceed with your duties.", 2)
            aisle_prompt(list, time_left)

    else:
        print_pause("You already have milk in your cart", 2)
        print_pause("You get distracted by all of the milkshakes", 2)
        print_pause("Your remaining grocery list", 2)
        print_pause(list, 2)
        time_left -= 4
        print_pause(str(time_left)+" minutes remaining!", 2)
        aisle_prompt(list, time_left)


def aisle3(list, time_left):
    print_pause("You go down aisle 3 to look at all of the yummy chips.", 2)
    if "Salt" in list:
        print_pause(
            "Someone left their cart in the middle of aisle 3.\n"
            "Inside the cart is a container of salt.", 2)
        choice = valid_input(
            "Do you take the container of salt from the "
            "stranger's cart? Yes or No\n", "yes", "no")
        if choice == "yes":
            print_pause("You steal the container of salt.", 2)
            list.remove("Salt")
            print_pause("Your remaining grocery list", 2)
            print_pause(list, 2)
            time_left -= 4
            print_pause(str(time_left)+" minutes remaining!", 2)
            aisle_prompt(list, time_left)
        elif choice == "no":
            print_pause(
                "You don't steal the container of salt and leave aisle 5.", 2)
            print_pause("Your remaining grocery list", 2)
            print_pause(list, 2)
            time_left -= 4
            print_pause(str(time_left)+" minutes remaining!", 2)
            aisle_prompt(list, time_left)
    else:
        print_pause("You look at all of the yummy chips.", 2)
        print_pause("Your remaining grocery list", 2)
        print_pause(list, 2)
        time_left -= 4
        print_pause(str(time_left)+" minutes remaining!", 2)
        aisle_prompt(list, time_left)


def aisle4(list, time_left):
    if "Salt" in list:
        print_pause(
            "You go down aisle 4 and find the salt. "
            "You put the salt in your cart.", 2)
        list.remove("Salt")
        print_pause("Your remaining grocery list", 2)
        print_pause(list, 2)
        time_left -= 4
        print_pause(str(time_left)+" minutes remaining!", 2)
        aisle_prompt(list, time_left)
    else:
        print_pause(
            "Aisle 4 carries salt, but you already have salt in your cart.", 2)
        print_pause("You just wasted precious time.", 2)
        time_left -= random.randint(1, 10)
        print_pause(str(time_left)+" minutes remaining!", 2)
        aisle_prompt(list, time_left)


def aisle5(list, time_left):
    if "Cake" in list and "Bread" in list:
        print_pause(
            "You go down aisle 3 and find the cake and bread!"
            " You put the cake and bread in your cart.", 2)
        list.remove("Bread")
        list.remove("Cake")
        print_pause("Your remaining grocery list", 2)
        print_pause(list, 2)
        time_left -= 4
        print_pause(str(time_left)+" minutes remaining!", 2)
        aisle_prompt(list, time_left)
    elif "Bread" in list:
        print_pause("You go back to aisle 3 to get another loaf of bread.", 2)
        list.remove("Bread")
        print_pause("Your remaining grocery list", 2)
        print_pause(list, 2)
        time_left -= 4
        print_pause(str(time_left)+" minutes remaining!", 2)
        aisle_prompt(list, time_left)
    elif "Cake" in list:
        print_pause("You pick up some cake.", 2)
        list.remove("Cake")
        print_pause("Your remaining grocery list", 2)
        print_pause(list, 2)
        time_left -= 4
        print_pause(str(time_left)+" minutes remaining!", 2)
        aisle_prompt(list, time_left)
    else:
        print_pause("You already have cake and bread.", 2)
        print_pause("You just wasted precious time.", 2)
        print_pause("Your remaining grocery list", 2)
        print_pause(list, 2)
        time_left -= 4
        print_pause(str(time_left)+" minutes remaining!", 2)
        aisle_prompt(list, time_left)


def aisle6(list, time_left):
    print_pause("You go down aisle 6 to look at all of the yummy drinks.", 2)
    while "Bread" not in list:
        print_pause("You decide to buy a carton of Coke.", 2)
        print_pause("You place the carton of coke inside your cart.", 2)
        print_pause("YOU ACCIDENTALLY SQUISH your BREAD.", 2)
        print_pause("Now you have to grab another loaf of bread.", 2)
        list.append("Bread")
    print_pause("Your remaining grocery list", 2)
    print_pause(list, 2)
    time_left -= 5
    print_pause(str(time_left)+" minutes remaining!", 2)
    aisle_prompt(list, time_left)


def play_game():
    list = ["Milk", "Bread", "Cake", "Onions", "Salt"]
    time_left = 25
    intro(list)
    aisle_prompt(list, time_left)


play_game()
