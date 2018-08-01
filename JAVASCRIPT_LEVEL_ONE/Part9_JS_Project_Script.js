
var first_name = prompt("Hello and Welcome. Please enter your first name:");
var last_name = prompt("Please enter your Last Name:")
var age = prompt("How old are you?")
var height = prompt("How tall are you in centimeters?")
var pet_name = prompt("What is the name of your pet?")

alert("Thank you so much for the information")

var bool_1 = false;
var bool_2 = false;
var bool_3 = false;
var bool_4 = false;

if (first_name[0] === last_name[0]) {
  bool_1 = true;
}

if (age > 20 && age < 30) {
  bool_2 = true;
}

if (height >= 170) {
  bool_3 = true;
}

if (pet_name[pet_name.length - 1] === "y") {
  bool_4 = true;
}

if (bool_1 && bool_2 && bool_3 && bool_4) {
  console.log("Welcome Comrade! You've passed the Spy Test")
}else{
  console.log("Sorry, nothing to see here.")
}
