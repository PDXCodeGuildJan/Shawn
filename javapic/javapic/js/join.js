// Javapic Inc.
// Author Shawn Waldow
// Join (Let's scrub a basic form.)

// DONT FORGET TO DISABLE BROWSER SCRUBBING
var grabFormKillDefaultScrub = document.getElementById('signup');
var noValidate = document.createAttribute("novalidate");
grabFormKillDefaultScrub.setAttributeNode(noValidate);




//Get a handle on the form in the DOM
var theForm = document.getElementById("signup");

//Select a single element for name
var theName = document.getElementsByName("name")[0];
theName.addEventListener('blur', checkName, false);

function checkName(){

	//See if we are getting everthing we expect. Later scrub.
	if (this.value.length < 2){
		console.log("not long enough")
	}
	else{
		console.log("else")
	}
}



//Get a handle on the submit button
var submitButton = document.getElementById("submit");
submitButton.addEventListener("click", submitForm, false);

function submitForm(){

	console.log(theName[0].value)
	
}

//console.log(theName.value);
console.log("Hello");