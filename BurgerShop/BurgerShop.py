from enum import Enum, auto

# implement the classes listed below 
class FoodItem:
    def __init__(self, foodName, allergen, price):
        self.foodName = foodName
        self.allergen = allergen
        self.price = price

    def __str__(self):
        return f"Food Item: {self.foodName}, Allergen: {self.allergen}"

class Burger(FoodItem):
    def __init__(self, foodName, allergen, size, meatType, price, condiments):
        super().__init__(foodName, allergen, price)
        self.meatType = meatType
        self.size = size
        self.price = price
        self.condiments = condiments

    def __str__(self):
        return (f"Burger: {self.foodName}, Allergen: {self.allergen}, Size: {self.size}, "
                f"Meat Type: {self.meatType}, Condiments: {', '.join(self.condiments)}, Price: ${self.price:.2f}")

class Drink(FoodItem):
    def __init__(self, foodName, allergen, size, beverageType, price):
        super().__init__(foodName, allergen, price)
        self.size = size
        self.beverageType = beverageType
        self.price = price

    def __str__(self):
        return (f"Drink: {self.foodName}, Allergen: {self.allergen}, Size: {self.size}, "
                f"Beverage Type: {self.beverageType}, Price: ${self.price:.2f}")

        
class Side(FoodItem):
    def __init__(self, foodName, allergen, size, sideType, price):
        super().__init__(foodName, allergen, price)
        self.size = size
        self.sideType = sideType
        self.price = price

    def __str__(self):
        return (f"Side: {self.foodName}, Allergen: {self.allergen}, Size: {self.size}, "
                f"Side Type: {self.sideType}, Price: ${self.price:.2f}")

class Combo(FoodItem):
    def __init__(self, foodName, allergen, size, comboType, price, burger, side, drink):
        super().__init__(foodName, allergen, price)
        self.comboSize = size
        self.comboType = comboType
        self.price = price
        self.burger = burger
        self.side = side
        self.drink = drink

    def __str__(self):
        return (f"Combo: {self.foodName}, Allergen: {self.allergen}, Size: {self.comboSize}, "
                f"Combo Type: {self.comboType}, Price: ${self.price:.2f}, "
                f"\n  Includes: \n  {self.burger}\n  {self.side}\n  {self.drink}")

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


def user_input_burger():
    b = Burger()
    #ask user for input and store it in burger object 
    return b
 
def user_input_drink():
    d = Drink()
    #ask user for input and store it in drink object 
    return d
 
def user_input_side():
    s = Side()
    #ask user for input and store it in side object 
    return s
 
def user_input_combo():
    c = Combo()
    #ask user for input and store it in combo object 
    #a combo must include one burger, one side, and one drink
    return c
 
def take_order():
    print("\nWelcome to Burger Shop\n")
    #ask user for name for the order 
    hasUserOrdered = False

    userInput = input("Enter your name to make an Order: \n\n").strip()
    userOrder = Order(userInput)

    #repeat taking order until client is done 
    while hasUserOrdered == False:
        print("\nMenu")
        print("1) Add a Burger")
        print("2) Add a Side")
        print("3) Add a Drink")
        print("4) Add a Combo")
        print("5) Add a Finish Order (you wont be able to add anymore items)\n")

        userItemChoice = input("Please choose an item from the menu (1-5): \n").strip()

        if userItemChoice == "1":
            newBurger = user_input_burger
            #userOrder.addToOrder(newBurger)
            userOrder.addToOrder("newBurger")

        elif userItemChoice == "2":
            newSide = user_input_side
            #userOrder.addToOrder(newSide)
            userOrder.addToOrder("newSide")

        elif userItemChoice == "3":
            newDrink = user_input_drink
            #userOrder.addToOrder(newDrink)
            userOrder.addToOrder("newDrink")

        elif userItemChoice == "4":
            newCombo = user_input_combo
            #userOrder.addToOrder(newCombo)
            userOrder.addToOrder("newCombo")

        elif userItemChoice == "5":
            print("\nTake a look at your order\n")
            hasUserOrdered = True

        else:
            print("please enter a valid menu number\n")

    #display order 
    userOrder.displayOrder()

    #display a thank you messageBi
    print("\nThank you for eating with us!\n")
 
take_order()


newDrink = Drink("pepsi", "none", "large", "diet", 2.0)
print(newDrink)