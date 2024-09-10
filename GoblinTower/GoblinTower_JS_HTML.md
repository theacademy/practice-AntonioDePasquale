# Goblin Tower Instructions 
This exercise asks you to create a Goblin Tower game that demonstrates your ability to use JavaScript to manipulate the DOM of an HTML page.
## Instructions
Create a web page that displays a new hero when the page loads. The hero must include the following attributes:
-	Name (start with an empty value)  
-	Current level (start at 0)  
-	Steps Taken (start at 0)  
-	Max Health (your choice of value)  
-	Current health (start at Max Health)  
-	Amount of gold (start between 0 and 5)  
-	A potion container that holds a max of five potions and that starts with one potion worth two health points.  

Each of these values must be clearly displayed on the page throughout the game and update automatically based on game play.
The game must include the following:
-	Ask for the hero's name via prompt.
-	A button that allows the hero to take a step.
-	Each step has a random chance of encountering a goblin.
    -	Add one health point for each step that does not encounter a goblin, up to the max value.
    -	When the hero encounters a goblin, the hero loses two health points and gains one gold.
-	When the hero has at least one potion and fewer than the max health points, display a button to drink a potion.
    -	When the user clicks the button, the hero loses one potion and recovers two health points.
    -	Hide the button when no potions are available or when the hero has the max health points.
-	Each 15th step the player advances one level. At that point, allow the user to see a button that will allow them to buy potions for 3 gold.
    -	Allow multiple purchases if the hero has enough gold and room in the potion container.
    -	Do not display the button if the hero does not have enough gold or if the hero already has the maximum number of potions.
    -	Hide the button after the user takes the next step, whether or not they purchased a potion.
-	The hero dies when current health reaches zero.
-	When the hero dies, ask the user if they would like to play again.
    -	If yes, start them over with a new character.
    -	If no, end the game and display the following values:
        -	The number of steps the hero took.
        -	The number of goblins the hero encountered.
        -	The amount of gold the hero left to heirs.

## Requirements
The program must include the following features:
-	It must update the screen by selecting elements and manipulating the values.
-	It must be able to hide/show elements based on hero's steps.
-	It must use prompt(), and confirm().
-	It must break code into functions.
