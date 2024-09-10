function plus1() {
    myValue = document.getElementById("counter").innerHTML;
    document.getElementById("counter").innerHTML = parseInt(myValue) + 1;
}


// Event listeners for button clicks
// Plus 1 button
    document.getElementById("count").addEventListener("click", () => {plus1()});
// Time button
    document.getElementById("timeButton").addEventListener("click", () => {
        const currentTime = new Date().toLocaleTimeString();
        document.getElementById("timeButton").textContent = currentTime;
    });

    const myButton = document.getElementById("myButton");
    const mytext = document.getElementById("textbox");
    const display = document.getElementById("display");

    myButton.addEventListener("mouseover", () => {
        myButton.style.backgroundColor = "lightblue";
    });

    myButton.addEventListener("mouseout", () => {
        myButton.style.backgroundColor = "lightblue";
    });

    mytext.addEventListener("input", () => {
        display.textContent = mytext.value;
    });

    document.getElementById("sayHello").addEventListener("click", () => {
        const userInput = prompt("Enter your name: ");
        if (userInput !== null && userInput !== "") {
            document.getElementById("hello").textContent = `Hello, ${userInput}!`;
        }
    });

    const PersonObj = {firstName: "John", lastName: "Doe", age: 30, eyeColour: "blue"};

    console.log(PersonObj.age);

    const AnotherPersonObj = {firstName: "Jane", lastName: "Doe", age: 50, eyeColour: "brown"};

    class PersonDef {
        constructor(firstName, lastName, age, eyeColour) {
            this.firstName = firstName;
            this.lastName = lastName;
            this.age = age;
            this.eyeColour = eyeColour;
        }

        displayInfo() {
            return `${this.firstName} ${this.lastName}, ${this.age}, ${this.eyeColour}`;
        }
    }

    const person1 = new PersonDef("John", "Doe", 30, "blue");
    const person2 = new PersonDef("Jane", "Doe", 50, "brown");

    console.log(person1.displayInfo());
    console.log(person2.displayInfo());