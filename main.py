
"""
    Welcome to Elite 101 this program is a starter for your chatbot project.
    The starter prompts the user to enter their name and then greets them with a personalized message.

    Functions:
        get_user_name(): Prompts the user to enter their name and returns it.
        greet_user(name): Prints a greeting message using the provided name.
        main(): Main function that orchestrates the user input and greeting process.

    Execution:
        When the script is run directly (not imported as a module), it will execute the main() function.
"""

listOfRestaurants = ["Taco Bell", "Pizza Hut", "McDonald's", "Panda Express", "KFC", "Subway", "Chipotle", "Wendy's"]


def get_user_name():
    name = input("Please enter your name: ")

# Lesson 6 new add ons, food delivery chatbot



def greet_user(name):
    print(f"Hello, {name}!")
    print("Welcome to the Food Delivery Chatbot. We are partnered with various restaurants to deliver your favorite meals right to your doorstep.")

def problem():
    restaurant = input("What restaurant did you order food from?")

    if (restaurant in listOfRestaurants == False):
        print("Sorry, we cannot find your restaurant in our partner list.")
        return
    else:
        print("Great! We have found your restaurant in our partner list.")

    time = input("How long has it been since you ordered your food")

    print("Checking status of your order...")
    print("You ordered food from {restaurant} ")
    print("It has been {time} minutes since you ordered your food")

    if time <= 15:
        print("Your order is most likely still being prepared. Please wait a bit longer. However, if you want to have other options, please choose one of the following:")

        min15 = input("1. Cancel my order /n 2. Change my delivery address /n 3. Speak to a customer service representative")
        option(min15)

    if time > 15 and time <= 30:
        print("We are sorry about the delay and inconvenience caused. Please choose one of the following options:")

        min30 = input("1. Cancel my order /n 2. Change my delivery address /n 3. Speak to a customer service representative")

        option(min30)

    if time > 30:
        print("We apoligize for the delay. A full refund has been issued you payment account. Please enter a new order for free as a compensation.")
        print("Enter 4 to place a new order, or 2 to speak to a customer service representative.")


def option(number):
    if number == 1:
        print("Your order has been cancelled. A refund will be processed to your original payment account.")
    elif number == 2:
        new_address = input("Please enter your change in delivery address: ")
        print(f"Your delivery address has been updated to: {new_address}. Your order will be delivered to the new address.")
    elif number == 3:
        print("Connecting you to a customer service representative. Please wait...")
        print("Representative connected...")
    elif number == 4:
        print("Place a new order with restaurants currently open:")
        print("1. Pizza from Pizza Hut")
        print("2. Burger from McDonald's")
        print("3. Sushi from Panda Express")
        print("4. Taco from Taco Bell")
        print("5. Torilla from Chipotle")
        print("6. Sandwich from Subway")
        newRestaurant = input("Please enter the number of the restaurant you would like to order from: ")
        print("Redirecting you to the ordering page for your selected restaurant...")

    else:
        print("Invalid option selected. Please try again.")

    def closing():
        print("We hope you have a great day! Thank you for using our Food Delivery Chatbot.")


def main():
    user_name = get_user_name()
    greet_user(user_name)
    problem()
    closing()
