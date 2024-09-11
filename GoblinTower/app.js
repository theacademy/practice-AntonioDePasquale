// Hero object constructor (takes a name from prompt)
class Hero {
    constructor(name) {
        this.name = name;
        this.level = 0;
        this.steps = 0;
        this.maxHealth = 100;
        this.currentHealth = 100;
        this.gold = Math.floor(Math.random() * 6);
        this.potions = 1;
        this.luck = 0; // more gold
        this.defence = 0    
        this.goblinEncounters = 0;
    }

    displayInfo() {
        return `Hero Name: ${this.name}, Level: ${this.level}, Steps: ${this.steps}, Gold: ${this.gold}, Potions: ${this.potions}, Health: ${this.currentHealth}/${this.maxHealth}, Luck: ${this.luck}, Defence: ${this.defence}, Goblin Encounters: ${this.goblinEncounters}`;
    }

    addPotion(){
        if(this.potions < 5){
            this.potions++;
            console.log(`You have added a potion. Now you have ${this.potions} potions.`);
        } else {
            console.log("You can't add more potions. You already have 5.");
        }
    }
    
    usePotion() {
        if(this.potions > 0){
            this.potions--;
            this.currentHealth += 2;
            if (this.currentHealth > this.maxHealth) {
                this.currentHealth = this.maxHealth;
            }
            updateGameBoard(`You used a potion (+2 Health). Now you have ${this.potions} potions and ${this.currentHealth} health points.`);
            console.log(`You used a potion (+2 Health). Now you have ${this.potions} potions and ${this.currentHealth} health points.`);
        } else {
            console.log("You don't have any potions.");
            updateGameBoard("You don't have any potions.");
        }
    }    
        
    removePotion() {
        if(this.potions > 0){
            this.potions--;
            console.log(`You removed a potion. Now you have ${this.potions} potions.`);
        } else {
            console.log("You don't have any potions.");
        }
        
    }
    buyPotion(){
        if(this.potions < 5){
            if (this.gold >= 3){
                this.potions++;
                this.gold -= 3;
                updateGameBoard(`You have added a potion. Now you have ${this.potions} potions and ${this.gold} gold.`);
                console.log(`You have added a potion. Now you have ${this.potions} potions and ${this.gold} gold.`);
            } else {
                console.log("You can't add more potions. You don't have enough gold.");
                updateGameBoard("You can't add more potions. You don't have enough gold.");
            }
        }else {
                console.log("You can't add more potions. You already have 5.");
                updateGameBoard("You can't add more potions. You already have 5.");
        }

    }
    gainGold(amount) {
        this.gold += amount;
        console.log(`You gained ${amount} gold. Now you have ${this.gold} gold.`);
    }
}

// Function to toggle visibility of an element
function toggleVisibility(elementId) {
    let element = document.getElementById(elementId);
    if (element.style.display === "none") {
        element.style.display = "inline-block";
    } else {
        element.style.display = "none";
    }
}
function hideButton(elementId) {
    let element = document.getElementById(elementId);
    element.style.display = "none";
}

function displayButton(elementId) {
    let element = document.getElementById(elementId);
    element.style.display = "inline-block";
}

// Function to toggle visibility of an element according to the potion requirements
function togglePotionVisibility(elementId) {
    let element = document.getElementById(elementId);
    if ((hero.potions > 0) && (hero.currentHealth < hero.maxHealth)){
        element.style.display = "inline-block";
    } else if  ((hero.potions == 0) || (hero.currentHealth == hero.maxHealth)){
        element.style.display = "none";
    } else {
        element.style.display = "none";
    }
}

const potionEvent = new Event("showPotionButton");
let hero; // the hero object created by the user in the DOMContentLoaded event listener.

// Ask's for the user's name to create a new Hero object.
document.addEventListener("DOMContentLoaded", (event) => {
    console.log("DOM fully loaded and parsed");
    const userName = prompt("Please give your name:");
    hero = new Hero(userName);
    console.log(hero.displayInfo());
    displayHeroInfo(hero);
});

// Attach event listeners for Yes and No buttons after DOM is loaded
document.addEventListener("DOMContentLoaded", () => {
    const yesRestartButton = document.getElementById("yesRestartButton");
    const noRestartButton = document.getElementById("noRestartButton");

    if (yesRestartButton && noRestartButton) {
        yesRestartButton.addEventListener("click", () => {
            restartGame();
        });

        noRestartButton.addEventListener("click", () => {
            endGame();
        });
    }
});


// Function to roll a d20
function rollD20() {
    return Math.floor(20 * Math.random()) + 1;
}

// Goblin encounter function
function checkIfGoblinEncountered(hero) {
    let goblinBool = false;
    const diceRoll = rollD20();

    if (diceRoll <= 6) {
        updateGameBoard("Goblin encountered!");
        console.log("Goblin encountered!");
        hero.currentHealth -= (10-(hero.defence));
        hero.gold += (1+(hero.luck));
        hero.goblinEncounters += 1;
        goblinBool = true;
        updateGameBoard(`You lost ${10-hero.defence} health and gained ${1+hero.luck} gold.`);
    } else {
        // updateGameBoard("No goblin encountered.");
        console.log("No goblin encountered.");
        if (hero.currentHealth < hero.maxHealth) {
            hero.currentHealth += 1;
            updateGameBoard("You recovered 1 health point.");
        }
    }
    displayHeroInfo(hero);
    return goblinBool;
}

// The hero takes a step
document.getElementById("takeStepButton").addEventListener("click", () => {
    hero.steps++;
    document.getElementById("stepCounter").textContent = `${hero.steps}`;
    console.log("Before encounter.")
    console.log(hero.displayInfo());
    if (checkIfGoblinEncountered(hero)) {
        console.log("After encounter.")
        console.log(hero.displayInfo());
        if (checkIfHeroIsDead(hero)) {
            //toggleVisibility("gameOverScreen");
        }
    }
    
    document.dispatchEvent(potionEvent);
    
    if (hero.steps % 15 == 0 ) {
        advanceLevel(hero); 
        console.log("Would you like to visit the shop?");
        if (hero.gold >= 3 && hero.potions < 5) {
            displayButton("goToShopButton");}
    } else {
        hideButton("goToShopButton");
        // hideButton("buyShopButton");
        // hideButton("buyPotionButton");
        // hideButton("buyShieldButton");
        // hideButton("learnShopMenuButton");
    }
});

// hero death
function checkIfHeroIsDead(hero) {
    if (hero.currentHealth <= 0) {
        console.log(`${hero.name} has died!`);
        document.getElementById("gameOverScreen").style.display = "block"; // show game over screen
        document.querySelector('.character-card').style.display = "none";
        document.querySelector('.shop-buttons').style.display = "none";

        return true;
    }
    return false;
}

// Restart the game after Hero death
function restartGame() {
    const userName = prompt("Please give your name:");
    hero = new Hero(userName);

    document.getElementById("gameOverScreen").style.display = "none";
    document.querySelector('.character-card').style.display = "block";
    document.querySelector('.shop-buttons').style.display = "flex";

    console.log(hero.displayInfo());
    displayHeroInfo(hero);
};

// End the game
function endGame() {
    document.getElementById("finalMessage").style.display = "block";
    document.getElementById("deathMessage").style.display = "block";
    document.getElementById("yesRestartButton").style.display = "none";
    document.getElementById("noRestartButton").style.display = "none";

    document.getElementById("finalStats").style.display = "block";
    document.getElementById("finalSteps").textContent = hero.steps;
    document.getElementById("finalGoblins").textContent = hero.goblinEncounters;
    document.getElementById("finalGold").textContent = hero.gold;
}

// Level up 
function advanceLevel(hero) {
    hero.level++;
    displayHeroInfo(hero);
    updateGameBoard(`${hero.name} has advanced to level ${hero.level}!`);}

function updateGameBoard(message) {
    const gameBoardInfo = document.getElementById('gameBoardInfo');
    gameBoardInfo.innerHTML += `<p>${message}</p>`;
}

// to display info on the page after the object initalization
function displayHeroInfo(hero) {
    const nameElement = document.querySelector('.name');
    const levelElement = document.querySelector('.level');
    const stepsElement = document.querySelector('.steps');
    const healthElement = document.querySelector('.health');
    const goldElement = document.querySelector('.gold');
    const potionsElement = document.querySelector('.potions');
    const luckElement = document.querySelector('.luck');
    const defenceElement = document.querySelector('.defence');

    if (nameElement) nameElement.textContent = hero.name;
    if (levelElement) levelElement.textContent = hero.level;
    if (stepsElement) stepsElement.textContent = hero.steps;
    if (healthElement) healthElement.textContent = `${hero.currentHealth}`; // Only current health here
    if (document.querySelector('.maxHealth')) document.querySelector('.maxHealth').textContent = hero.maxHealth;
    if (goldElement) goldElement.textContent = hero.gold;
    if (potionsElement) potionsElement.textContent = hero.potions;
    if (luckElement) luckElement.textContent = hero.luck;
    if (defenceElement) defenceElement.textContent = hero.defence;
}

document.addEventListener("showPotionButton", () => {
    console.log("The potion event was triggered and user needs to decide to take the potion")
    togglePotionVisibility("drinkPotionButton");
})

drinkPotionButton.addEventListener('mouseover', () => {
    drinkPotionButton.title = "Use a potion to recover 2 health points";
    drinkPotionButton.style.backgroundColor = "yellow";
});

drinkPotionButton.addEventListener('mouseout', () => {
    drinkPotionButton.title = "";
    drinkPotionButton.style.backgroundColor = "";
});
takeStepButton.addEventListener("mouseover", () => {
    takeStepButton.title = "Take a step forward in the game";
    takeStepButton.style.backgroundColor = "#228e61";
})

takeStepButton.addEventListener("mouseout", () => {
    takeStepButton.title = "";
    takeStepButton.style.backgroundColor = ""
    takeStepButton.style.color = "";
})

document.getElementById("drinkPotionButton").addEventListener("click", () => { 
    if (confirm("Are you sure you want to drink the potion (-1 Potion)?")) { 
        hero.usePotion();
        displayHeroInfo(hero);
        hideButton("drinkPotionButton");
    }
});

goToShopButton.addEventListener("click", () => {
    console.log("Go to shop button clicked")
    toggleVisibility("buySwordButton");
    toggleVisibility("buyShieldButton");
    toggleVisibility("buyPotionButton");
    toggleVisibility("leaveShopMenuButton");
    hideButton("goToShopButton");
    displayHeroInfo(hero);
})
buyPotionButton.addEventListener("click", () => {
    if (confirm("Are you sure you want to buy a potion (-3 Gold)?")) {
        hero.buyPotion();
        displayHeroInfo(hero);
    }
})

leaveShopMenuButton.addEventListener("click", () => {
    console.log("Leave shop button clicked")
    toggleVisibility("buySwordButton");
    toggleVisibility("buyShieldButton");
    toggleVisibility("buyPotionButton");
    toggleVisibility("leaveShopMenuButton");
    displayHeroInfo(hero);
})

buySwordButton.addEventListener("click", () => {
    if (hero.gold >= 2) {
        if (confirm("Are you sure you want to buy a sword (-2 Gold)?")) {
            hero.luck += 1; //TODO ADD FUNCTION INSTEAD
            hero.gold -=2
            console.log("Sword bought!")
            updateGameBoard("Sword bought! Your luck has increased.");
            displayHeroInfo(hero);
        }
    } else {
        console.log("Not enough gold!")
        updateGameBoard("Not enough gold to buy a sword!");
    }
})

buyShieldButton.addEventListener("click", () => {
    if (hero.gold >= 2) {
        if (confirm("Are you sure you want to buy a shield (-2 Gold)?")) {
            hero.defence += 1;
            hero.gold -=2;
            console.log("Shield bought!")
            updateGameBoard("Shield bought! Your defence has increased.");
            displayHeroInfo(hero);
        }
    } else {
        console.log("Not enough gold!")
        updateGameBoard("Not enough gold to buy a shield!");
    }
})