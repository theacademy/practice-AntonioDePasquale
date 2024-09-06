# Antonio De Pasquale, 05/09/2024
from enum import Enum, auto

# implement the classes listed below 
class FoodItem:
    def __init__(self, foodName, allergen, price, size):
        self.foodName = foodName
        self.allergen = allergen
        self.price = price
        self.size = size

    def changeSize(self):
        print("\nCustomise your item")
        # Allow user to change the size
        newSize = input(f"Current size is '{self.size}'. Choose new size (Small, Medium, Large) or press any other key to keep current size: ").strip().capitalize()

        if newSize in ["Small", "Medium", "Large"]:
            self.size = newSize
            print(f"Food size has been changed to '{self.size}'.\n")

            if self.size == "Large":
                self.price += 1

            elif self.size == "Small":
                self.price -= 1

        else:
            print("Size remains unchanged.\n")

    def __str__(self):
        return f"Food Item: {self.foodName}, Allergen: {self.allergen}"

class Burger(FoodItem):
    def __init__(self, foodName, allergen, size, meatType, price, condiments):
        super().__init__(foodName, allergen, price, size)
        self.meatType = meatType
        self.size = size
        self.price = price
        self.condiments = condiments

    def displayBurger(self):
        print(f"\nBurger: {self.foodName}")
        print(f"Patty: {self.meatType}")
        print(f"Size: {self.size}")
        print(f"Price: £{self.price}")
        print(f"Ingredients and condiments: {', '.join(self.condiments)}")
        print(f"Allergens: {', '.join(self.allergen)}\n")

    def customise(self):
        potentialIngredients = ["Lettuce", "Tomato", "Onions", "Pickles", "Cheese slice", "Mayonnaise", "Ketchup", "Mustard"]

        # Allow user to change the condiments
        changeCondiments = input("\nWould you like to add or remove ingredients? (y/n): \n").strip().lower()

        if changeCondiments in ["yes", "y"]:
            # Remove condiments
            while True:  # Continue until user decides to stop removing
                print("\nCurrent ingredients:", ", ".join(self.condiments))
                removeCondiment = input("Enter the ingredient you want to remove or type 'done' to stop removing: ").strip().capitalize()

                if removeCondiment == "Done":
                    print("Finished removing ingredients.")
                    break  # Exit removal loop

                elif removeCondiment in self.condiments:
                    self.condiments.remove(removeCondiment)
                    print(f"{removeCondiment} has been removed.")

                else:
                    print(f"{removeCondiment} not found in ingredients.")

            # Add condiments
            while True:  # Continue until user decides to stop adding
                available_to_add = [ingredient for ingredient in potentialIngredients if ingredient not in self.condiments]
                print("\nIngredients you can add:", ", ".join(available_to_add))

                addCondiment = input("Enter an ingredient you want to add or type 'done' to stop adding: ").strip().capitalize()

                if addCondiment == "Done":
                    print("Finished adding ingredients.")
                    break  # Exit addition loop

                elif addCondiment in available_to_add:
                    self.condiments.append(addCondiment)
                    print(f"{addCondiment} has been added.")

                else:
                    print(f"{addCondiment} already in the burger or not available to add.")


    def __str__(self):
        return (f"Burger: {self.foodName}, Allergen: {self.allergen}, Size: {self.size}, "
                f"Meat Type: {self.meatType}, Condiments: {', '.join(self.condiments)}, Price: ${self.price:.2f}")

class Drink(FoodItem):
    def __init__(self, foodName, allergen, size, beverageType, price):
        super().__init__(foodName, allergen, price, size)
        self.size = size
        self.beverageType = beverageType
        self.price = price
        
    def customise(self):

        newType = input(f"Would you like to make your drink diet or regular\n").strip().capitalize()

        if newType in ["Regular", "Diet"]:
            self.beverageType = newType
            print(f"Drink type has been changed to '{self.beverageType}\n'.")

        else:
            print("Drink type remains unchanged.\n")

    def displayDrink(self):
        print(f"\nDrink: {self.foodName}")
        print(f"Drink Type: {self.beverageType}")
        print(f"Size: {self.size}")
        print(f"Price: £{self.price}")
        print(f"Allergens: {', '.join(self.allergen)}\n")

    def __str__(self):
        return (f"Drink: {self.foodName}, Allergen: {self.allergen}, Size: {self.size}, "
                f"Beverage Type: {self.beverageType}, Price: ${self.price:.2f}")

        
class Side(FoodItem):
    def __init__(self, foodName, allergen, size, sideType, price):
        super().__init__(foodName, allergen, price, size)
        self.size = size
        self.sideType = sideType
        self.price = price

    def displaySide(self):
        print(f"\nSide: {self.foodName}")
        print(f"Side Type: {self.sideType}")
        print(f"Size: {self.size}")
        print(f"Price: £{self.price}")
        print(f"Allergens: {', '.join(self.allergen)}\n")

    def __str__(self):
        return (f"Side: {self.foodName}, Allergen: {self.allergen}, Size: {self.size}, "
                f"Side Type: {self.sideType}, Price: ${self.price:.2f}")

class Combo(FoodItem):
    def __init__(self, foodName, allergen, size, price, burger, side, drink):
        super().__init__(foodName, allergen, price, size)
        self.comboSize = size
        self.price = price
        self.burger = burger
        self.side = side
        self.drink = drink


    def changeSize(self):
        print("\nCustomise your item")
        # Allow user to change the size
        newSize = input(f"Current size is '{self.size}'. Choose new size (Small, Medium, Large) or press any other key to keep current size: ").strip().capitalize()

        if newSize in ["Small", "Medium", "Large"]:
            self.size = newSize
            print(f"Food size has been changed to '{self.size}'\n")

            if self.size == "Large":
                self.price += 2.50

            elif self.size == "Small":
                self.price -= 2.50

        else:
            print("Size remains unchanged.\n")

    def changeTypeToDiet(self):
        updateDrink = input("Do you want to make the drink diet? (y/n): \n").strip().lower()
        
        if updateDrink in ["yes", "y"]:
            if isinstance(self.drink, Drink):
                self.drink.beverageType = "Diet"
                print("\nThe drink has been updated to diet.\n")
            else:
                print("No drink found in the combo to update.")

    def changeDrink(self):
        if isinstance(self.drink, Drink):
            while True:
                print("\nAvailable drink options:")
                print("1) Coke")
                print("2) Pepsi")
                print("3) Lemonade")
                print("4) Fanta")
                print("Enter 'done' to keep current drink.\n")

                choice = input("Enter the number of the drink you want to choose: ").strip().lower()

                if choice == 'done':
                    print("\nThe drink remains unchanged.\n")
                    break

                drink_options = {
                    "1": ("Coke", 1.99),
                    "2": ("Pepsi", 1.99),
                    "3": ("Lemonade", 1.40),
                    "4": ("Fanta", 1.99)
                }

                if choice in drink_options:
                    drink_name, drink_price = drink_options[choice]
                    self.drink.foodName = drink_name
                    self.drink.price = drink_price
                    print(f"\nThe drink has been updated to {drink_name}.\n")
                    break
                else:
                    print("\nInvalid choice. Please enter a valid number or 'done' to keep the current drink.\n")
        else:
            print("\nNo drink found in the combo to update.\n")




    def displayCombo(self):
        print(f"\nCombo name: {self.foodName}")
        print(f"Burger: {self.burger.foodName}")
        print(f"Side: {self.side.foodName}")
        print(f"Drink: {self.drink.foodName}")
        print(f"Drink Type: {self.drink.beverageType}")
        print(f"Size: {self.size}")
        print(f"Price: ${self.price:.2f}")

    def __str__(self):
        return (f"Combo: {self.foodName}, Allergen: {self.allergen}, Size: {self.comboSize}, "
                f"Price: ${self.price:.2f}, "
                f"\n  Includes: \n  Burger: {self.burger.foodName}\n  Side: {self.side.foodName}\n  Drink: {self.drink.beverageType} {self.drink.foodName}")
    

class Order:
    def __init__(self, customerName):
        self.customerName = customerName
        self.orderItems = []

    def addToOrder(self, singleFoodItem):
        """
        function to add a single item to the order list
        """
        self.orderItems.append(singleFoodItem)

    def displayOrder(self):
        """
        Function to display the order details.
        """
        print(f"Order for {self.customerName}:")
        for item in self.orderItems:
            print(f"- {item}")

    def calculateTotalPrice(self):
        """
        Function to calculate and return the total price of the order.
        """
        total = 0
        for item in self.orderItems:
            total += item.price
        return total



def user_input_burger():
    #ask user for input and store it in burger object 
    burgerFinished = False
    burger = None

    while burgerFinished == False:
        print("\nBurger options")
        print("1) The Chicken zinger")
        print("2) The Big Beefy")
        print("3) The Veggie stack")

        userItemChoice = input("Please choose an item from the menu (1-3): \n").strip()

        if userItemChoice == "1":
            burger = Burger("The Chicken zinger", ["Gluten", "Dairy"], "Medium", "Chicken", 8.99, ["Lettuce", "Cheese slice", "Mayonaise"])
            
        elif userItemChoice == "2":
            burger = Burger("The Big Beefy", ["Gluten"], "medium", "beef", 9.99, ["Lettuce", "Tomatoe", "Ketchup", "Mustard"])
            
        elif userItemChoice == "3":
            burger = Burger("The Veggie stack", ["Gluten"], "medium", "veggie", 7.99, ["Lettuce", "Onions", "Pickles"])

        else:
            print("Please choose a valid burger from the menu (1-3).")
            continue

        print("You chose:")
        burger.displayBurger()

        confirmBurger = input("Do you want to customise this burger? (y/n): ").strip().lower()

        if confirmBurger in ["yes", "y"]:
            burger.changeSize()
            burger.customise()  # Call the customise function to allow user to make changes
            burger.displayBurger()
            burgerFinished = True

        else:
            print(f"{burger.foodName} has been added to your order.")
            burgerFinished = True

    return burger  # Return the burger object
 
def user_input_drink():
    #ask user for input and store it in drink object 
    drinkFinished = False
    drink = None

    while drinkFinished == False:
        print("\nDrink options")
        print("1) Coke")
        print("2) Pepsi")
        print("3) Lemonade")
        print("4) Fanta\n")

        userItemChoice = input("Please choose an item from the menu (1-4): \n").strip()

        if userItemChoice == "1":
            drink = Drink("Coke", ["Gluten"], "medium", "regular", 1.99)
            
        elif userItemChoice == "2":
            drink = Drink("Pepsi", ["Gluten"], "medium", "regular", 1.99)
            
        elif userItemChoice == "3":
            drink = Drink("Lemonade", ["Gluten"], "medium", "regular", 1.40)

        elif userItemChoice == "4":
            drink = Drink("Fanta", ["Gluten"], "medium", "regular", 1.99)

        else:
            print("Please choose a valid drink from the menu (1-4).")
            continue

        print("You chose:")
        drink.displayDrink()

        confirmDrink = input("Do you want to customise this Drink? (y/n): ").strip().lower()

        
        if confirmDrink in ["yes", "y"]:
            drink.changeSize()  # Call the changesize function to allow user to make changes
            drink.customise()  # Call the customise function to allow user to make changes
            drinkFinished = True

        else:
            print(f"{drink.foodName} has been added to your order.")
            drinkFinished = True

    return drink  # Return the drink object
 
def user_input_side():
        #ask user for input and store it in side object 
        sideFinished = False
        side = None

        while sideFinished == False:
            print("\nSide options")
            print("1) Regular Fries")
            print("2) Veggie Fries")
            print("3) Onion Rings")
            print("4) Hot Wings")
            print("5) Ice Cream")

            userItemChoice = input("Please choose a side from the menu (1-5): \n").strip()

            if userItemChoice == "1":
                side = Side("Regular Fries", ["Gluten"], "medium", "regular", 1.99)

            elif userItemChoice == "2":
                side = Side("Veggie Fries", ["Gluten"], "medium", "vegan", 2.99)

            elif userItemChoice == "3":
                side = Side("Onion Rings", ["Gluten"], "medium", "vegan", 2.49)

            elif userItemChoice == "4":
                side = Side("Hot Wings", ["Gluten"], "medium", "regular", 2.99)

            elif userItemChoice == "5":
                side = Side("Ice Cream", ["Gluten"], "medium", "regular", 2.99)

            else:
                print("Please choose a valid side from the menu (1-5).")
                continue

            print("You chose:")
            side.displaySide()

            confirmDrink = input("Do you want to customise this side? (y/n): ").strip().lower()

            
            if confirmDrink in ["yes", "y"]:
                side.changeSize()  # Call the changesize function to allow user to make changes
                sideFinished = True

            else:
                print(f"{side.foodName} has been added to your order.")
                sideFinished = True

        return side  # Return the Side object
 
def user_input_combo():
    #ask user for input and store it in combo object 
     
    comboFinished = False
    combo = None

    while comboFinished == False:
        print("\nCombo options")
        print("1) The Chicken zinger meal")
        print("2) The Full stack combo")
        print("3) The Veggie feast combo")

        userItemChoice = input("Please choose an item from the menu (1-3): \n").strip()

        if userItemChoice == "1":
            burger = Burger("The Chicken zinger", ["Gluten", "Dairy"], "Medium", "Chicken", 8.99, ["Lettuce", "Cheese slice", "Mayonnaise"])
            side = Side("Regular Fries", ["Gluten"], "Medium", "Fries", 1.99)
            drink = Drink("Coke", ["None"], "Medium", "Regular", 1.99)
            combo = Combo("The Chicken zinger meal", ["Gluten", "Dairy"], "Medium", 12.00, burger, side, drink)

        elif userItemChoice == "2":
            burger = Burger("The Big Beefy", ["Gluten"], "Medium", "Beef", 9.49, ["Lettuce", "Tomato", "Ketchup", "Mustard"])
            side = Side("Onion Rings", ["None"], "Medium", "Onion Rings", 2.49)
            drink = Drink("Pepsi", ["None"], "Medium", "Regular", 1.99)
            combo = Combo("The Full stack combo", ["Gluten"], "Medium", 13.00, burger, side, drink)

        elif userItemChoice == "3":
            burger = Burger("The Veggie stack", ["Gluten"], "Medium", "Veggie", 7.99, ["Lettuce", "Onions", "Pickles"])
            side = Side("Veggie Fries", ["None"], "Medium", "Fries", 2.99)
            drink = Drink("Lemonade", ["None"], "Medium", "Regular", 1.40)
            combo = Combo("The Veggie feast combo", ["Gluten"], "Medium", 11.00, burger, side, drink)
        
        else:
            print("Please choose a valid combo from the menu (1-3).")
            continue


        print("You chose:")
        combo.displayCombo()

        confirmCombo = input("\nDo you want to customise this Combo? (y/n): \n").strip().lower()

        if confirmCombo in ["yes", "y"]:
            combo.changeSize()
            combo.changeDrink()
            combo.changeTypeToDiet()
            combo.displayCombo()
            comboFinished = True

        else:
            print(f"{combo.foodName} has been added to your order.")
            comboFinished = True

    return combo  # Return the combo object
 
def take_order():
    print("\nWelcome to Burger Shop\n")
    #ask user for name for the order 
    hasUserOrdered = False

    while True:
        userInput = input("Enter your name to make an Order: \n\n").strip()

        if userInput:
            userOrder = Order(userInput)
            break

        else:
            print("Please enter a name, input cannot be empty")

    #repeat taking order until client is done 
    while not hasUserOrdered:
        print("\nMenu")
        print("1) Add a Burger")
        print("2) Add a Side")
        print("3) Add a Drink")
        print("4) Add a Combo")
        print("5) Finish or view your Order")
        print("6) Cancel the Order and Exit\n")
        

        userItemChoice = input("Please choose an item from the menu (1-6): \n").strip()

        if userItemChoice == "1":
            newBurger = user_input_burger()
            userOrder.addToOrder(newBurger)

        elif userItemChoice == "2":
            newSide = user_input_side()
            userOrder.addToOrder(newSide)

        elif userItemChoice == "3":
            newDrink = user_input_drink()
            userOrder.addToOrder(newDrink)

        elif userItemChoice == "4":
            newCombo = user_input_combo()
            userOrder.addToOrder(newCombo)

        elif userItemChoice == "5":
            print("\nTake a look at your order\n")
            userOrder.displayOrder()
            confirmOrderFinished = input("\nDo you want to confirm this order (the order cannot be changed after this (y/n))\n").strip().lower()

            if confirmOrderFinished in ["yes", "y"]:
                hasUserOrdered = True

            else:
                continue

        elif userItemChoice == "6":
            exitInput = input("\nAre you sure you want to cancel the order? (y/n): ").strip().lower()
            
            if exitInput in ["yes", "y"]:
                print("\nOrder has been canceled. Exiting the program.")
                print("\nThank you for eating with us!\n")
                return  # Exit the function and end the program
        
        else:
            print("\nplease enter a valid menu number\n")

    # Display order 
    userOrder.displayOrder()

    # Display a thank you message
    print("\nThank you for eating with us!\n")

 
take_order()
