const Hero1 = {
    name: '',
    level: 0,
    steps: 0,
    maxHealth: 100,
    currentHealth: 100,
    gold: Math.floor(Math.random() * 6), 
    potions: 1
};

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
    }

    displayInfo() {
        return `Hero Name: ${this.name}, Level: ${this.level}, Steps: ${this.steps}, Gold: ${this.gold}, Potions: ${this.potions}`;
    }
}

// Ask's for the user's name to create a new Hero object.
document.addEventListener("DOMContentLoaded", (event) => {
    console.log("DOM fully loaded and parsed");
    const userName = prompt("Please give your name:");
    const hero = new Hero(userName);
    console.log(hero.displayInfo());
});
