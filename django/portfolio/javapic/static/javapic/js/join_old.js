// Javapic Inc.
// Join (Let's scrub)

function submit(){
	var name = document.getElementsByName("name");
	console.log("Hello 2");
	console.log(name/*.nextSibling.textContent*/);
}
// DONT FORGET TO DISABLE BROWSER SCRUBBING
var grabFormKillDefaultScrub = document.getElementById('signup');
var noValidate = document.createAttribute("novalidate");
grabFormKillDefaultScrub.setAttributeNode(noValidate);


// Catch the submit click
var submitButton = document.getElementById("submit");
submitButton.onclick = submit;

console.log("Hello");