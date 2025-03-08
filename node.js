// let Name="Omid";
//console.log(Name);
// Name="Amir";
//console.log(Name);
// const lname="Jalali";
// console.log(lname);
// lname="Torshizi";
// console.log(lname);
//___________________________________
// function saymyname(name) {
//     (name);
// };saymyname("John Doe")

// const project=function(name) {
//     (name); 
// };project("Walter White")

// const say=(something) => {
//     (something);
// };say("Hello")

const axios= require("axios")
function fetchdata() {
    const response=axios.get('https://jsonplaceholder.typicode.com/todos/1');
    console.log(response);
}fetchdata();
say();