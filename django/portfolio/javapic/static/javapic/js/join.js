// Javapic Inc.
// Author Shawn Waldow
// Join (Let's scrub a basic form.)
// Housekeeping post MVP: Do we need to delete event listners after use?

// DONT FORGET TO DISABLE BROWSER SCRUBBING
var grabFormKillDefaultScrub = document.getElementById('signup');
var noValidate = document.createAttribute("novalidate");
grabFormKillDefaultScrub.setAttributeNode(noValidate);


//Select a single element for name
var theName = document.getElementsByName("name")[0];
theName.addEventListener('blur', checkName, false);

//add a style for the class error
errorCSS = ".error {font-size: .6em; color: red; padding: 0; border: 0;}"
document.styleSheets[0].insertRule(errorCSS, 0);


//Select a single element for username
var theUserName = document.getElementsByName("username")[0];
theUserName.addEventListener('blur', checkUserName, false);

//Select a single element for email
var theEmail = document.getElementsByName("email")[0];
theEmail.addEventListener('blur', checkEmail, false);



//I THINK THIS TYPE OF THIS USE IS CORNY. IMPROVE LATER.
// Remove input error messages we might have placed as 
// as currently designed which child of a label thats an older sibling.
function removeErrorSpan(athis){
//Check to see if we've added an error span here. Stop if null.
	if (athis.previousSibling.previousSibling.lastChild) {
		//There looks to be an error span. Make sure and then remove it.
		if  (athis.previousSibling.previousSibling.lastChild.className 
				=== "error"){
			console.log("preexisting error");
			athis.previousSibling.previousSibling.lastChild.remove();
		}
	}
}

//I THINK THIS TYPE OF THIS USE IS CORNY. IMPROVE LATER.
//Add a span with a error message, mssgStr, to an input elements label
//which as currently designed is a label thats an older sibling
function addErrorSpan(aThis, mssgStr){

		//Make a div for the error message
		var errorSpan = document.createElement("span");
		errorSpan.classList.add("error");
		//OKAY make a placeholder eventually.
		errorSpan.textContent = mssgStr;
		//Insert it to the dom
		console.log(aThis.previousSibling.previousSibling)
		aThis.previousSibling.previousSibling.appendChild(errorSpan);



		console.log("User name invalid. Letters or numbers 4 to 15 long.");
		//Reset value from invalid user input to empty
		aThis.value ="";
}


function checkName(){

	//See if we are getting everthing we expect.

	//Remove any pre-existing error messages
	removeErrorSpan(this);
	// Make a regex to detect a name with first and last
	// Modified from a stack overflow  post. I made sure to exclude
	// names that start with a space.
	patt = /^[^\s][a-z ,.'-]+$/;
	//Let user names have spaces in last name and apostrophes and hyphens.
	if (!(patt.test(this.value))){

		addErrorSpan(this, "-->Req'd: Firstname Lastname");
	}

	else{
		console.log("Name good.");
	}
}

function checkUserName(){

	//Remove any pre-existing error messages
	removeErrorSpan(this);
	// Make a regex to detect username less than 15 more than 4
	patt = /[A-Za-z\d]{4,15}/;
	//Handle a username that's too long, too short, or has weird characters.
	if (!(patt.test(this.value))){

		addErrorSpan(this, "-->Req'd: 4-15 characters");
	}

	else{
		console.log("Username good.");
	}
}


function checkEmail(){

	
	//Remove any pre-existing error messages
	removeErrorSpan(this);

	//Look for an email address that has no spaces and at least 1 char
	//followed by an @ followed by at least 1 char followed by a . 
	//ending with at least 1 non space char.
	//Note the carrot before the expression that requires the eval starts at the
	//begining of the string. The $ sign says the string has to end with the
	//specified expression.
	
	var patt = /^[^\s]+@[^\s]+\.[^\s]+$/
	if (!(patt.test(this.value))){
		//Add an error alert
		addErrorSpan(this, "<--Email address not valid.");
	}
	else{
		console.log("Email ok");
	}
}



//Get a handle on the submit button
var submitButton = document.getElementById("submit");
submitButton.addEventListener("click", submitForm, false);

function submitForm(){

	//Mysterious bit necesarry for custom form submission not covered very well 
	//by Google results or the text book.
	event.preventDefault();

	//Remove any previous error messages.
	removeErrorSpan(grabFormKillDefaultScrub);

	//If each field has valid input...
	if(theName.value && theUserName.value && theEmail.value){

		//Build up a URL to pass user name on to browser.
		var nextPagePath = (/*"file:///home/shawnwaldow/Documents/CodeSchool/"+
			"Week1/javapic/*/"gallery?" + theName.value);
		window.location.assign(nextPagePath);
	}
	else{
		var fillEmAll ="  ...but first please fill out all fields as required.";
		addErrorSpan(grabFormKillDefaultScrub, fillEmAll);
	}
}

//console.log(theName.value);
console.log("Hello");