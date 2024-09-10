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
        this.strength = 0; // more gold
        this.defence = 0    
    }

    displayInfo() {
        return `Hero Name: ${this.name}, Level: ${this.level}, Steps: ${this.steps}, Gold: ${this.gold}, Potions: ${this.potions}, Health: ${this.currentHealth}/${this.maxHealth}, Strength: ${this.strength}, Defence: ${this.defence}`;
    }

    createPotions() {
        pass
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
            console.log(`You used a potion. Now you have ${this.potions} potions and ${this.currentHealth} health points.`);
        } else {
            console.log("You don't have any potions.");
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
}


const potionEvent = new Event("showPotionButton");


// Function to toggle visibility of an element
function toggleVisibility(elementId) {
    let element = document.getElementById(elementId);
    if (element.style.display === "none") {
        element.style.display = "inline-block";
    } else {
        element.style.display = "none";
    }
}

let hero; // the hero object created by the user in the DOMContentLoaded event listener.

// Ask's for the user's name to create a new Hero object.
document.addEventListener("DOMContentLoaded", (event) => {
    console.log("DOM fully loaded and parsed");
    const userName = prompt("Please give your name:");
    hero = new Hero(userName);
    console.log(hero.displayInfo());
    displayHeroInfo(hero);
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
        console.log("Goblin encountered!");
        hero.currentHealth -= 5;
        hero.gold += 1;
        goblinBool = true;
    } else {
        console.log("No goblin encountered.");
        if (hero.currentHealth < hero.maxHealth) {
            hero.currentHealth += 1;
        }
    }
    displayHeroInfo(hero);
    return goblinBool;
}

// The hero takes a step
document.getElementById("takeStepButton").addEventListener("click", () => {
    hero.steps++;
    document.getElementById("stepCounter").textContent = `Steps: ${hero.steps}`;
    console.log("Before encounter.")
    console.log(hero.displayInfo());
    if (checkIfGoblinEncountered(hero)) {
        console.log("After encounter.")
        console.log(hero.displayInfo());
    }
});

// to display info on the page after the object initalization
function displayHeroInfo(hero) {
    const nameElement = document.querySelector('.name');
    const levelElement = document.querySelector('.level');
    const stepsElement = document.querySelector('.steps');
    const healthElement = document.querySelector('.health');
    const goldElement = document.querySelector('.gold');
    const potionsElement = document.querySelector('.potions');
    const strengthElement = document.querySelector('.strength');
    const defenceElement = document.querySelector('.defence');

    if (nameElement) nameElement.textContent = hero.name;
    if (levelElement) levelElement.textContent = hero.level;
    if (stepsElement) stepsElement.textContent = hero.steps;
    if (healthElement) healthElement.textContent = `${hero.currentHealth}`; // Only current health here
    if (document.querySelector('.maxHealth')) {
        document.querySelector('.maxHealth').textContent = hero.maxHealth;
    }
    if (goldElement) goldElement.textContent = hero.gold;
    if (potionsElement) potionsElement.textContent = hero.potions;
    if (strengthElement) strengthElement.textContent = hero.strength;
    if (defenceElement) defenceElement.textContent = hero.defence;
}

// event listener triggered when there is showPotionButton event is dispatched
// TODO add document.dispatchEvent(potionEvent) where needed in the game;
document.addEventListener("showPotionButton", () => {
    console.log("The potion event was triggered and user needs to decide to take the potion")
    toggleVisibility("drinkPotionButton");
})


document.getElementById("drinkPotionButton").addEventListener("click", () => { 
    hero.usePotion();
});


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
    takeStepButton.style.backgroundColor = "green";
})

takeStepButton.addEventListener("mouseout", () => {
    takeStepButton.title = "";
    takeStepButton.style.backgroundColor = "";
})