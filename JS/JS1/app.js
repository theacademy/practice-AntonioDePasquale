x = 11;
let y = "Some text";
const z = 42;
var w = "Joe";


const loadpage = function updatePage() {
    document.getElementById("display").innerHTML = 
    `<p>The value of w is: ${w}</p>
    <p>The value of x is: ${x}</p>
    <p>The value of y is: ${y}</p>
    <p>The value of z is: ${z}</p>
    `
};

loadpage();

//console.log(`The value of x is: ${x}`);
/*
Multi
line
comment
*/