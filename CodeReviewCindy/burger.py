# Cindy Cieniek, 04/09/24

from enum import Enum  

DISCOUNT_VALUE = 0.1 # TODO CHANGE IT 
BASE_PRICE = 3.0 # TODO CHANGE IT 

ingredients_list = {
    'chicken' : 11.99,
    'beef' : 12.99,
    'veggie' : 13.99,
    'cheese' : 2.99,
    'lettuce' : 0.99,
    'tomato' : 1.09,
    'coke' : 3.00,
    'juice' : 3.00,
    'water' : 3.00,
    'fries' : 3.00,
    'salad' : 3.00,
    'corn' : 3.00
}

class MENU(Enum):  
    BURGER, DRINK, SIDE, COMBO= range(1, 5)

class Size(Enum):
    S = "S"  
    M = "M"  
    L = "L"  

class Toppings(Enum):
    LETTUCE, TOMATO, CHEESE = range(1, 4)

class FoodItem:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = float(price)
        self.ingredients = ingredients
    
    def __str__(self):
        return f"{self.name} (£{self.price:.2f}), ingredients: {self.ingredients} "

class Burger(FoodItem):
    def __init__(self, name, price, ingredients, patty):
        super().__init__(name, price, ingredients)
        self.patty = patty

class Drink(FoodItem):
    def __init__(self, name, price, ingredients, size):
        super().__init__(name, price, ingredients)
        self.size = size

class Side(FoodItem):
    def __init__(self, name, price, ingredients, size):
        super().__init__(name, price, ingredients)
        self.size = size

class Combo(FoodItem):
    def __init__(self, name, price, items, discount = 0):
        super().__init__(name, price, items)
        self.ingredients = items
        original_price = sum(item.price for item in items)
        self.discounted_price = float(original_price - discount)
class Order:
    def __init__(self):
        self.items = []
        self.total_price = 0

    def addItem(self, item, quantity=1):
        print(type(item))
        print(type(quantity))
        self.items.append((item, quantity))
        self.total_price += item.price * quantity

    def removeItem(self, item, quantity): #TODO extension
        pass

    def getTotalPrice(self):
        return self.total_price
    
    def displayOrder(self):
        print("\n=========== Your Order:")
        for item, quantity in self.items:
            print(f"  {quantity}x {item}")
        print(f"\n=========== Total Price: £{self.total_price:.2f}")
 
def calculatePrice(ingredients):
    base_price = sum([ingredients_list.get(ingredient, 0) for ingredient in ingredients])
    print(f'Ingredient list price is : {base_price} ')
    print("reached")
    return base_price
class UserCancelledException(Exception):
    pass

def allowUserToCancel(input):
    print("Want to cancel order? Type: Cancel")
    if input == "cancel":
        loop_continue = False 
        raise UserCancelledException("\n \nOperation cancelled by user")

def getValidInput(prompt, valid_options):
    loop_continue = True
    while loop_continue:
        user_input = input(prompt).lower().strip()
        allowUserToCancel(user_input)
        if user_input in valid_options:
            return user_input
        print(f'Invalid input.')

def getValidQuantity(prompt):
    loop_continue = True
    while loop_continue:
        try:
            quantity = int(input(prompt))
            if quantity > 0:
                return quantity
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def getValidEnumInput(prompt, enum_class):
    valid_options = [e.name.lower() for e in enum_class]
    user_input = getValidInput(prompt, valid_options)
    return enum_class(user_input.upper())

def userInputBurger():
    patty = getValidInput("Choose your patty (beef/chicken/veggie): ", ['beef', 'chicken', 'veggie'])
    toppings = []
    for topping in Toppings:
        user_input = input(f"Do you want {topping.name.lower()}? (y/n): ").lower()
        allowUserToCancel(user_input)
        if  user_input== 'y':
            toppings.append(topping.name.lower())
    ingredients = [patty] + toppings
    price = calculatePrice(ingredients)
    return Burger("Burger (" + str(patty)+ ")", price, ingredients, patty)
 
def userInputDrink():
    drink = getValidInput("Choose your drink (coke/juice/water): ", ['coke', 'juice', 'water'])
    size = getValidEnumInput(("Choose your size (s/m/l): ").upper(), Size)
    price = BASE_PRICE if size == Size.S else 2.0 if size == Size.M else 3.0 if size == Size.L else 4.0 #FIXME this should not be hardcoded
    return Drink("Drink (" + str(drink)+ ")", price, drink, size)

def userInputSide():
    item = getValidInput("Choose your side item (fries/salad/corn): ", ['fries', 'salad', 'corn'])
    size = getValidEnumInput(("Choose your size (s/m/l): ").upper(), Size)
    price = BASE_PRICE if size == Size.S else 2.0 if size == Size.M else 3.0 if size == Size.L else 4.0 #FIXME this should not be hardcoded
    return Side("Side (" + str(item)+ ")", price, item, size)
 
def orderCombo():
    burger = userInputBurger()
    drink = userInputDrink()
    side = userInputSide()
    items = [burger, drink, side]
    price = burger.price + drink.price + side.price
    return Combo("Custom Combo", price, items, DISCOUNT_VALUE)

def take_order():
    print("Welcome to Burger Shop!")
    name = input("\nPlease enter your name: ")
    order = Order()
    not_done = 1

    while not_done:
        print("\n=========== Menu: ===========")
        for item in MENU:
            print(f"{item.value}. {item.name.title()}")
        print("5. Finish ordering")
        
        choice = int(input("Enter your choice (1-5): "))
        
        if choice == 5:
            not_done = 0
            break
        
        selected_item = MENU(choice)
        
        if selected_item == MENU.BURGER:
            quantity = getValidQuantity("Enter quantity: ")
            order.addItem(userInputBurger(), quantity)
        elif selected_item == MENU.DRINK:
            quantity = getValidQuantity("Enter quantity: ")
            order.addItem(userInputDrink(), quantity)
        elif selected_item == MENU.SIDE:
            quantity = getValidQuantity("Enter quantity: ")
            order.addItem(userInputSide(), quantity)
        elif selected_item == MENU.COMBO:
            quantity = getValidQuantity("Enter quantity: ")
            order.addItem(orderCombo(), quantity)

    order.displayOrder()
    print(f'\nThank you, {name}!')

take_order()