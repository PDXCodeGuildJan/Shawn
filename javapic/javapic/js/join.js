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
	//Now write scrubbing
	//[A-Z][a-z]{1,15} [A-Z][a-z]{1,15} should be title case two part
	//names with fewer than 32 characters.

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

	event.preventDefault();
	console.log(theName.value);
	var nextPagePath = "file:///home/shawnwaldow/Documents/CodeSchool/Week1/javapic/javapic/gallery.html?" + theName.value;
	console.log(nextPagePath)
	//setTimeout(window.location.assign, 0, nextPagePath)
	window.location.assign(nextPagePath);
	console.log(nextPagePath);
	//window.open(nextPagePath);
}

//console.log(theName.value);
console.log("Hello");